##Shayna Mallett
##CSE 598 Algorithms in CompBio
##ASU Fall 2021
import math

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


with open('../../Downloads/rosalind_ba10c.txt') as data:
#with open('./viterbi.txt') as data:
    observed = data.readline().strip('\n')
    data.readline()#----line
    print(observed)
    alphabet = data.readline().strip('\n').split("\t")
    print(alphabet)
    data.readline()#---line
    states = data.readline().strip('\n').split("\t")
    print(states)
    data.readline()
    transition = []
    emission = []
    data.readline()#column names
    for i in range(len(states)):
        transition_row = data.readline().strip('\n').split('\t')#[1].split("	")
        transition.append([])
        print(transition_row)
        for x in range(len(states)):
            transition[i].append(transition_row[x+1])

        
    data.readline()#---line
    data.readline()#column names
    for i in range(len(states)):
        emission_row = data.readline().strip('\n').split('\t')#[1].split("	")
        emission.append([])
        for x in range(len(alphabet)):
            emission[i].append(emission_row[x+1])

    print(transition)
    print(emission)

    #Convert input characters to their indexes in the order of the emission matrix
    # nevermind I can just do this as I go with .index() observed_index = inputToAlphabet(observed)
    #Create the graph
    backtracking = decode(emission, transition, observed, alphabet)
    #Backtrack
    hiddenPath = backtrack(backtracking, states)
    print(hiddenPath)