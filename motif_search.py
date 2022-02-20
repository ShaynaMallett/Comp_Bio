##Shayna Mallett
##CSE 598 Algorithms in CompBio
##ASU Fall 2021

import random
from fractions import Fraction
def printProfile(profile):
    for x in range(0, 4):
        print(profile[x])
        
def printMotif(motif):
    print("Score: " , getScore(motif )) 
    for row in motif:
        print(''.join(row))
    printProfile(getProfile(motif))

        
#Returns the profile of a matrix of motifs
def getProfile(matrix):
    profile = []
    #For each position along the length of the sequences
    #Pre fill with la-place for pseudocounts
    k = len(matrix[0])
    t = len(matrix)
    for i in range (0, 4):
        profile.append([])
        for j in range(0, k):
            profile[i].append(1)
    #For each index in the length of the sequences
    for i in range (0, k):
        #For each sequence in the matrix
        for j in range (0, t):
            #update the count in profile
            if matrix[j][i] == 'A':
                profile[0][i] += 1
            elif matrix[j][i] == 'C':
                profile[1][i] += 1
            elif matrix[j][i] == 'G':
                profile[2][i] += 1
            elif matrix [j][i] == 'T':
                profile[3][i] += 1
    #Change to frequencies
    for i in range (0, 4):
        for j in range(0, k):
            profile[i][j] = profile[i][j]/(t+4) 
    return profile

#returns the most probable motif matrix given a profile and t sequences 
def getMotif(profile, dna):
    #for each sequence in dna, find the most probable kmer (gete length from profile) given the profile 

    k = len(profile[0])
    t = len(dna)
    motifs = []
    
    #initialize array with t arrays to fill with each sequence's best k-mer
    for x in range (0, t) :
        motifs.append([])
        
    #for each sequence 
    for i in range(0, t):
        prob = 0
        start = 0
        #for each starting index of a k-mer in the current sequence
        for x in range(0, len(dna[i])-k+1):
            temp_prob = 1
            #for each base in the current k-mer
            for y in range(0, k):
                base = dna[i][x+y]
                if base == 'A':
                    temp_prob = temp_prob*profile[0][y]
                elif base == 'C':
                    temp_prob = temp_prob*profile[1][y]
                elif base == 'G':
                    temp_prob = temp_prob*profile[2][y]
                elif base == 'T':
                    temp_prob = temp_prob*profile[3][y]
            if temp_prob > prob:
                prob = temp_prob
                start = x
        most_probable = dna[i][start:(start+k)]
        #print("The " , i , "'s most probable k-mer: " , most_probable, " with P= " ,prob)
        motifs[i]= most_probable
    #print("Using profile: " )
    #printProfile(profile)
    #getConsensus(profile)
    return motifs

#Returns the score of a matrix. 
def getScore(matrix):
    profile = getProfile(matrix)
    consensus = getConsensus(profile)
    score = 0
    k = len(matrix[0])
    t = len(matrix)
    #For each index in the length of the sequences
    for i in range (0, k):
        #For each sequence in the matrix
        for j in range (0, t):
            if matrix[j][i] != consensus[i]:
                score += 1 
    return score

def getConsensus(profile):
    score = 0
    k = len(profile[0])
    consensus = ''
    for i in range(0, k):
        maxF = 0
        maxBase = 'N'
        for j in range(0, 4):
            if profile[j][i] > maxF:
                maxF = profile[j][i]
                maxBase = j               
        if maxBase == 0:
            consensus +='A'
        elif maxBase == 1:
            consensus +='C'
        elif maxBase == 2:
            consensus += 'G'
        elif maxBase == 3:
            consensus += 'T'
    #print("Consensus: " ,consensus) 
    return consensus

#main
def randomizedMotifSearch(dna, k, t):    
    #Set initial matrix with random k-mers from each sequence t
    motifs = []
    for x in range(0, t):
        r = random.randint(0,len(dna[0])-k)
        motifs.append( dna[x][r:(r+k)])

    bestMotifs = motifs.copy()
    profile = []
    iterator = 0
    while True :#and iterator <1000:
        iterator += 1
        profile = getProfile(bestMotifs)
        motifs = getMotif(profile, dna)
        
        #Lower score is a better matrix
        if getScore(motifs) < getScore(bestMotifs):
            bestMotifs = motifs.copy()
            #print("<")
            #print("\nBest = ", getScore(bestMotifs))
            #printProfile(bestMotifs)
            ##print("\nReal = ", getScore(realMotifs))
            #printProfile(realMotifs) 
        else:
            return getScore(bestMotifs),bestMotifs
            break
            s =1
            #printMotif(bestMotifs) 
            #break
    '''print(iterator)
    printMotif(bestMotifs)
    printMotif(realMotifs)'''


#main
with open("rosalind_ba2f.txt", 'r') as data:
    parameters = data.readline()
    #k is length of k-mer we are searching for
    #t is number of strings (dna matrix will have 0-based indexing
    k = int(parameters.split()[0])
    t = int(parameters.split()[1])
    realMotifs = ['TCTCGGGG','CCAAGGTG','TACAGGCG', 'TTCAGGTG' , 'TCCACGTG']
    dna = []
    for x in range(0,t) :
        dna.append(data.readline().strip('\n'))
    allBestMotifs = []
    bestOfTheBest = []
    for iteration in range(0, 1000):
        score,motif = randomizedMotifSearch(dna,k,t)
        if iteration == 0:
            bestOfTheBest = (score,motif)
        elif score < bestOfTheBest[0]:
            bestOfTheBest = (score,motif)
        allBestMotifs.append((score, motif))
    printMotif(bestOfTheBest[1])