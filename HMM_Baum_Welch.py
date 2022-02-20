##Shayna Mallett
##CSE 598 Algorithms in CompBio
##ASU Fall 2021
import math


##Helper functions
def printMatrixWithColumnsAndRows(matrix, rows, columns):
        print('\t'+'\t'.join(columns))
        for x in range(len(matrix)):
            print(str(rows[x])+'\t' + '\t'.join(map(str,matrix[x])) )

def printMatrix(matrix):
    for row in matrix:
        print(row) 
def roundMatrix(matrix, decimals):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix[x][y] = normal_round(matrix[x][y], decimals)
    return matrix
            
def normal_round(n, decimals=0):#Obtained verbatim from stack overflow
    expoN = n * 10 ** decimals
    rounded = -1
    if abs(expoN) - abs(math.floor(expoN)) < 0.5:
        rounded = math.floor(expoN) / 10 ** decimals
    else:
        rounded = math.ceil(expoN) / 10 ** decimals
    if rounded == 1.0:
        return '1.000'
    elif rounded == 0.0:
        return '0.000'
    return rounded 

def occurrences(text, sub):
        return len(re.findall('(?={0})'.format(re.escape(sub)), text))

def printResults(parameters, alphabet, states):
    emission = parameters[0]
    transition = parameters[1]
    emission = roundMatrix(emission,3)
    transition = roundMatrix(transition,3) 
    printMatrixWithColumnsAndRows(transition, states, states)
    print('--------')
    printMatrixWithColumnsAndRows(emission, states, alphabet)
    


#############
#Estimation step - Soft decoding
def apply_forward( emission, transition, observed, alphabet):
    forwardMatrix = [[0 for x in range(len(transition))] for y in range(len(observed))]
    for y in range(len(transition)):
        forwardMatrix[0][y] = math.exp(math.log(1/len(transition)) + math.log(float(emission[y][alphabet.index(observed[0])])))
    last_column = forwardMatrix[0]
    for i in range(1, len(observed)):
        cur_column = []
        for j in range(len(transition)):
            toCurrent = 0#change to summation not max
            for x in range(len(last_column)):#same
                toCurrent = toCurrent + math.exp(math.log(last_column[x]) + math.log(float(transition[x][j])) + math.log(float(emission[j][alphabet.index(observed[i])])))
            cur_column.append(toCurrent)
            forwardMatrix[i][j] = toCurrent 
        last_column = cur_column        
    forwardToSink = 0
    for x in range(len(transition)):
        forwardToSink = forwardToSink + last_column[x]    
    return forwardMatrix, forwardToSink

def apply_backward(emission, transition, observed, alphabet):
    backwardMatrix = [[0 for x in range(len(transition))] for y in range(len(observed))]
    for y in range(len(transition)):
        backwardMatrix[len(observed)-1][y] = 1
    last_column = backwardMatrix[len(observed)-1]
    for i in range(len(observed)-2, -1, -1):
        cur_column = []
        for j in range(len(transition)-1, -1, -1):
            toCurrent = 0#change to summation not max
            for x in range(len(last_column)-1, -1,-1):#same
                toCurrent= toCurrent + math.exp(math.log(last_column[x]) + math.log(float(transition[j][x])) + math.log(float(emission[x][alphabet.index(observed[i+1])])))
            cur_column.insert(0, toCurrent)
            backwardMatrix[i][j] = toCurrent
        last_column = cur_column 
    return backwardMatrix

def node(forwardMatrix, backwardMatrix, transition, observed, emission, alphabet, forwardToSink):
    nodeResponsibility = [[0 for x in range(len(transition))] for y in range(len(forwardMatrix))]   
    for i in range( len(forwardMatrix)):
        for x in range(len(forwardMatrix[i])):
            nodeResponsibility[i][x] = math.exp(math.log(forwardMatrix[i][x]) + math.log(backwardMatrix[i][x]) - math.log(forwardToSink))
    return nodeResponsibility

def edge(forwardMatrix, backwardMatrix, transition, observed, emission, alphabet, forwardToSink):
    edgeResponsibility = [[0 for x in range(len(transition)**2)] for y in range( len(forwardMatrix)-1)] 
    for i in range(len(forwardMatrix)-1):
        for x in range(len(forwardMatrix[i])**2):
            edgeResponsibility[i][x] = math.exp(math.log(forwardMatrix[i][math.floor(x/len(transition))]) + math.log(backwardMatrix[i+1][x%len(transition)]) + math.log(float(emission[x%len(transition)][alphabet.index(observed[i+1])]))+ math.log(float(transition[math.floor(x/len(transition))][x%len(transition)])) - math.log(forwardToSink))
    return edgeResponsibility
'''
def edge(forwardMatrix, backwardMatrix, transition, observed, emission, alphabet, forwardToSink):
    print("Forward to sink: " , forwardToSink)
    edgeResponsibility = [[[0 for z in range(len(transition))] for x in range(len(transition))] for y in range( len(forwardMatrix)-1)] 
    for i in range(len(forwardMatrix)-1):
        for x in range(len(forwardMatrix[i])):
            for z in range(len(forwardMatrix[i])):
                print("To sink: " , forwardToSink)
                print("Values: ", forwardMatrix[i][x])
                print( backwardMatrix[i+1][z])
                print(transition[x][z])
                print(emission[z][alphabet.index(observed[i])])
                edgeResponsibility[i][x][z] = math.exp(math.log(forwardMatrix[i][x])+ math.log(backwardMatrix[i+1][z]) + math.log(float(emission[z][alphabet.index(observed[i+1])]))+ math.log(float(transition[x][z]))- math.log(forwardToSink))
    return edgeResponsibility
'''
def soft_decoding(alphabet, observed, parameters):
    emission = parameters[0]
    transition = parameters[1] 
    forwardMatrix,forwardToSink = apply_forward(emission, transition, observed, alphabet)
    backwardMatrix = apply_backward(emission, transition, observed, alphabet)
    nodeResponsibility = node(forwardMatrix, backwardMatrix, transition, observed, emission, alphabet, forwardToSink)
    edgeResponsibility =  edge(forwardMatrix, backwardMatrix, transition, observed, emission, alphabet, forwardToSink)
    return nodeResponsibility, edgeResponsibility


#############
#Maximization step - parameter estimation
def getTransitionMatrix( states, observed, edgeResponsibility ):
    transition = [[0 for x in range(len(states))] for y in range(len(states))]
    for x in range(len(states)**2):
        w = x % len(states)
        for y in range(len(observed)-1):
            transition[math.floor(x/len(states))][w] = transition[math.floor(x/len(states))][w] + edgeResponsibility[y][x]
    #normalize works correctly
    for x in range(len(states)):
        normalizer = 0
        for y in range(len(states)):
            if normalizer == 0:
                for z in range(len(states)):
                    normalizer = normalizer + transition[x][z]
            transition[x][y] = transition[x][y]/normalizer
    return transition

def getEmissionMatrix(alphabet, states, observed, nodeResponsibility):
    emission = [[0 for x in range(len(alphabet))] for y in range(len(states))]
    for x in range(len(states)):
        for y in range(len(observed)):
            w = alphabet.index(observed[y])
            emission[x][w] = emission[x][w] + nodeResponsibility[y][x]
    #normalize works correctly
    for x in range(len(states)):
        normalizer = 0
        for y in range(len(alphabet)):
            if normalizer == 0:
                for z in range(len(alphabet)):
                    normalizer = normalizer + emission[x][z]
            emission[x][y] = emission[x][y]/normalizer
    return emission

def parameter_estimation(alphabet, states, observed, PI):
    nodeResponsibility = PI[0]
    edgeResponsibility = PI[1]
    emission = getEmissionMatrix(  alphabet,states, observed, nodeResponsibility)
    transition = getTransitionMatrix( states, observed, edgeResponsibility)

    return emission, transition
    

##Main
def main():
    with open('../../Downloads/rosalind_ba10k.txt') as data:
        iterations = data.readline().strip('\n')
        data.readline()#----line
        observed = data.readline().strip('\n')
        data.readline()#----line
        alphabet = data.readline().strip('\n').split("\t")
        data.readline()#---line
        states = data.readline().strip('\n').split("\t")
        print(states) 
        data.readline()#---line
        transition = []
        emission = []
        data.readline()#column names
        for i in range(len(states)):
            transition_row = data.readline().strip('\n').split('\t')
            transition.append([])
            for x in range(len(states)):
                transition[i].append(transition_row[x+1])

            
        data.readline()#---line
        data.readline()#column names
        for i in range(len(states)):
            emission_row = data.readline().strip('\n').split('\t')
            emission.append([])
            for x in range(len(alphabet)):
                emission[i].append(emission_row[x+1])
        
        ##Baum Welch:
        parameters = emission, transition

        for x in range(int(iterations)):
            ##Expectation step
            PI = soft_decoding(alphabet, observed, parameters)
            ##Maximization step
            parameters = parameter_estimation(alphabet, states, observed, PI)


        printResults(parameters, alphabet, states) 

        


if __name__ == "__main__":
    main()