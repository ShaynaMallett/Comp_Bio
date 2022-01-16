##Shayna Mallett
##CSE 598 Algorithms in CompBio
##ASU Fall 2021
import math
import re

def decode(emission, transition, observed, alphabet):
    last_column = [math.log(1) for i in range(len(states))]
    backtracking = [['.' for x in range(len(transition))] for y in range(len(observed)+1)]
    #Loop not recursive because python is dumb
    #Only need the most recent column 
    for i in range(len(observed)):
        cur_column = []
        for j in range(len(states)):#should be 0,1 for test dataset
            toCurrent = []
            for x in range(len(states)):#same
                toCurrent.append(last_column[x] + math.log(float(transition[x][j])) + math.log(float(emission[j][alphabet.index(observed[i])])))
            print(toCurrent)
            cur_column.append(max(toCurrent))
            print(cur_column)
            backtracking[i][j] = toCurrent.index(max(toCurrent))
            print(backtracking[i][j])
        last_column = cur_column
    backtracking[len(backtracking)-1][0] = last_column.index(max(last_column))
    print(backtracking)
    return backtracking


def backtrack(backtracking, states):
    hiddenPath = ''
    x = len(backtracking) - 1
    last = backtracking[x][0]
    hiddenPath = states[last]
    x -= 1
    while x > 0:
        last = backtracking[x][last]
        hiddenPath = states[last] + hiddenPath
        x -= 1
                        
    return hiddenPath

def normal_round(n, decimals=0):
    expoN = n * 10 ** decimals
    if abs(expoN) - abs(math.floor(expoN)) < 0.5:
        return math.floor(expoN) / 10 ** decimals
    return math.ceil(expoN) / 10 ** decimals

def occurrences(text, sub):
        return len(re.findall('(?={0})'.format(re.escape(sub)), text))

def getTransitionMatrix(hiddenPath, states):
    transition = []
    for x in range(len(states)):
        transition.append([])
        total = hiddenPath.count(states[x])
        if hiddenPath[len(hiddenPath)-1] == states[x]:
            total -= 1
            print("end of hidden path is " , states[x])
        print(total)
        for y in range(len(states)):
            curTransition = [states[x], states[y]]
            print(''.join(curTransition))
            print(hiddenPath.count(''.join(curTransition)))
            if total == 0:
                transition[x].append(normal_round(1/len(states) , 3))
            else:
                transition[x].append( normal_round(((occurrences(hiddenPath, ''.join(curTransition) ) )/ (total)) ,3))
    print(transition)
    return transition

def getEmissionMatrix(observed, alphabet, hiddenPath, states):
    emission = []
    zipped = list(zip(observed, hiddenPath))
    for x in range(len(states)):
        emission.append([])
        total = hiddenPath.count(states[x])
        for y in range(len(alphabet)):
            if total == 0:
                emission[x].append(normal_round(1/len(alphabet) , 3))
            else:
                emission[x].append(normal_round( ((zipped.count((alphabet[y],states[x]))) /(total)), 3)) 
    print(emission)      
    return emission

def printMatrixWithColumnsAndRows(matrix, rows, columns):
        print('\t' , '\t'.join(columns))
        for x in range(len(matrix)):
            print(rows[x],'\t', '\t'.join(map(str,matrix[x])) )
        
        
with open('../../Downloads/rosalind_ba10h.txt') as data:
#with open('./viterbi.txt') as data:
    observed = data.readline().strip('\n')
    data.readline()#----line
    print(observed)
    alphabet = data.readline().strip('\n').split("\t")
    print(alphabet)
    data.readline() #----line
    hiddenPath = data.readline().strip('\n')
    data.readline()#---line
    states = data.readline().strip('\n').split("\t")
    for x in states:
        print(x)
    transition = getTransitionMatrix( hiddenPath, states)
    emission = getEmissionMatrix(observed, alphabet, hiddenPath, states)
    print(transition)
    print(emission)
    print(states)
    print(alphabet)
    printMatrixWithColumnsAndRows(transition, states, states)
    print('--------')
    printMatrixWithColumnsAndRows(emission, states, alphabet)