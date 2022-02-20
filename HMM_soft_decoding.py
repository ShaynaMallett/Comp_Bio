##Shayna Mallett
##CSE 598 Algorithms in CompBio
##ASU Fall 2021
import math

def apply_forward( emission, transition, observed, alphabet):
    forwardMatrix = [[0 for x in range(len(transition))] for y in range(len(observed))]
    for y in range(len(states)):
        forwardMatrix[0][y] = math.exp(math.log(1/len(transition)) + math.log(float(emission[y][alphabet.index(observed[0])])))
    last_column = forwardMatrix[0]
    for i in range(1, len(observed)):
        cur_column = []
        for j in range(len(states)):
            toCurrent = 0#change to summation not max
            for x in range(len(last_column)):#same
                toCurrent = toCurrent + math.exp(math.log(last_column[x]) + math.log(float(transition[x][j])) + math.log(float(emission[j][alphabet.index(observed[i])])))
            cur_column.append(toCurrent)
            forwardMatrix[i][j] = toCurrent 
        last_column = cur_column        
    forwardToSink = 0
    for x in range(len(states)):
        forwardToSink = forwardToSink + last_column[x] 
    
    return forwardMatrix, forwardToSink

def apply_backward(emission, transition, observed, alphabet):
    backwardMatrix = [[0 for x in range(len(transition))] for y in range(len(observed))]
    for y in range(len(states)):
        backwardMatrix[len(observed)-1][y] = 1
    last_column = backwardMatrix[len(observed)-1]
    for i in range(len(observed)-2, -1, -1):
        cur_column = []
        for j in range(len(states)-1, -1, -1):
            toCurrent = 0#change to summation not max
            for x in range(len(last_column)-1, -1,-1):#same
                toCurrent= toCurrent + math.exp(math.log(last_column[x]) + math.log(float(transition[j][x])) + math.log(float(emission[x][alphabet.index(observed[i+1])])))
            cur_column.insert(0, toCurrent)
            backwardMatrix[i][j] = toCurrent
        last_column = cur_column
  
    return backwardMatrix

def combine(forwardMatrix, backwardMatrix, transition, observed, emission, alphabet, forwardToSink):
    combinedMatrix = [[0 for x in range(len(transition))] for y in range(len(forwardMatrix))]   
    for i in range( len(forwardMatrix)):
        for x in range(len(forwardMatrix[i])):
            combinedMatrix[i][x] = math.exp(math.log(forwardMatrix[i][x]) + math.log(backwardMatrix[i][x]) - math.log(forwardToSink))

    return combinedMatrix

def normalize(combinedMatrix):
    normalizedMatrix = [[0 for x in range(len(combinedMatrix[0]))] for y in range(len(combinedMatrix))]
    for i in range(len(combinedMatrix)):
        col_normalizer = 0
        for x in range(len(combinedMatrix[i])):
            if col_normalizer ==0:            
                for y in range(len(combinedMatrix[i])):
                    col_normalizer = col_normalizer + combinedMatrix[i][y]
            normalizedMatrix[i][x] = math.exp(math.log(combinedMatrix[i][x]) - math.log(col_normalizer))
    return normalizedMatrix

def normal_round(n, decimals=0):
    expoN = n * 10 ** decimals
    if abs(expoN) - abs(math.floor(expoN)) < 0.5:
        return math.floor(expoN) / 10 ** decimals
    return math.ceil(expoN) / 10 ** decimals

with open('../../Downloads/rosalind_ba10j.txt') as data:
    observed = data.readline().strip('\n')
    data.readline()#----line
    alphabet = data.readline().strip('\n').split("\t")
    data.readline()#---line
    states = data.readline().strip('\n').split("\t")
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

    forwardMatrix,forwardToSink = apply_forward(emission, transition, observed, alphabet)
    backwardMatrix = apply_backward(emission, transition, observed, alphabet)
    combinedMatrix = combine(forwardMatrix, backwardMatrix, transition, observed, emission, alphabet, forwardToSink)
    #normalizedMatrix = normalize(combinedMatrix)

    print('\t'.join(states))
    for row in combinedMatrix:
        print('\t'.join(map(lambda s: str(normal_round(s,4)), row)))