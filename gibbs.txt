##Shayna Mallett
##CSE 598 Algorithms in CompBio
##ASU Fall 2021

import random
from fractions import Fraction


##Helper functions
def printProfile(profile):
    for x in range(0, 4):
        print(profile[x])


def printMotif(motif):
    print("Score: ", getScore(motif))
    for row in motif:
        print(''.join(row))
    #printProfile(getProfile(motif))


###Scoring functions

# Returns the profile of a matrix of motifs
def getProfile(matrix):
    profile = []
    # For each position along the length of the sequences
    # Pre fill with la-place for pseudocounts
    k = len(matrix[0])
    t = len(matrix)
    for i in range(0, 4):
        profile.append([])
        for j in range(0, k):
            profile[i].append(1)
    # For each index in the length of the sequences
    for i in range(0, k):
        # For each sequence in the matrix
        for j in range(0, t):
            # update the count in profile
            if matrix[j][i] == 'A':
                profile[0][i] += 1
            elif matrix[j][i] == 'C':
                profile[1][i] += 1
            elif matrix[j][i] == 'G':
                profile[2][i] += 1
            elif matrix[j][i] == 'T':
                profile[3][i] += 1
    # Change to frequencies
    for i in range(0, 4):
        for j in range(0, k):
            profile[i][j] = profile[i][j] / (t + 4)
    return profile


# returns the most probable motif matrix given a profile and t sequences
def getMotif(profile, dna):
    # for each sequence in dna, find the most probable kmer (gete length from profile) given the profile

    k = len(profile[0])
    t = len(dna)
    motifs = []

    # initialize array with t arrays to fill with each sequence's best k-mer
    for x in range(0, t):
        motifs.append([])

    # for each sequence
    for i in range(0, t):
        prob = 0
        start = 0
        # for each starting index of a k-mer in the current sequence
        for x in range(0, len(dna[i]) - k + 1):
            temp_prob = 1
            # for each base in the current k-mer
            for y in range(0, k):
                base = dna[i][x + y]
                if base == 'A':
                    temp_prob = temp_prob * profile[0][y]
                elif base == 'C':
                    temp_prob = temp_prob * profile[1][y]
                elif base == 'G':
                    temp_prob = temp_prob * profile[2][y]
                elif base == 'T':
                    temp_prob = temp_prob * profile[3][y]
            if temp_prob > prob:
                prob = temp_prob
                start = x
        most_probable = dna[i][start:(start + k)]
        motifs[i] = most_probable
    return motifs


# Returns the score of a matrix.
def getScore(matrix):
    profile = getProfile(matrix)
    consensus = getConsensus(profile)
    score = 0
    k = len(matrix[0])
    t = len(matrix)
    # For each index in the length of the sequences
    for i in range(0, k):
        # For each sequence in the matrix
        for j in range(0, t):
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
            consensus += 'A'
        elif maxBase == 1:
            consensus += 'C'
        elif maxBase == 2:
            consensus += 'G'
        elif maxBase == 3:
            consensus += 'T'
    return consensus


##Gibbs specific functions

# Returns the profile of a matrix of motifs
def getProfileLessI(matrix, skip):
    profile = []
    # For each position along the length of the sequences
    # Pre fill with la-place for pseudocounts
    k = len(matrix[0])
    t = len(matrix)
    for i in range(0, 4):
        profile.append([])
        for j in range(0, k):
            profile[i].append(1)
    # For each index in the length of the sequences
    for i in range(0, k):
        # For each sequence in the matrix
        for j in range(0, t):
            if not j == skip - 1:  # 0-based index for j so subtract 1 from i
                # update the count in profile skipping the i'th sequence every time
                if matrix[j][i] == 'A':
                    profile[0][i] += 1
                elif matrix[j][i] == 'C':
                    profile[1][i] += 1
                elif matrix[j][i] == 'G':
                    profile[2][i] += 1
                elif matrix[j][i] == 'T':
                    profile[3][i] += 1
    # Change to frequencies
    for i in range(0, 4):
        for j in range(0, k):
            profile[i][j] = profile[i][j] / ((t - 1) + 4)  # One less sequence to make the profile off of
    return profile


# Change the i-th motif in a matrix with the profile created from all the other t-i sequences
def updateMotifs(profile, motifs, dna, i):
    #print( i, " is i  in updateMotifs is : " , motifs[i-1] , " from : "  )
    #printMotif(motifs)
    k = len(profile[0])
    t = len(dna)
    #Same loop as randomized but only run on sequence i
    prob = 0
    start = 0
    kmerProbs = []
    totalProbs = 0
    #print("Using profile for biased die")
    #printProfile(profile)
    # for each starting index of a k-mer in the current sequence
    for x in range(0, len(dna[i - 1]) - k + 1-1):
        # Calculate  probability of each possible k-mer in the sequence
        temp_prob = 1
        # for each base in the current k-mer
        for y in range(0, k):
            base = dna[i - 1][x + y]
            if base == 'A':
                temp_prob = temp_prob * profile[0][y]
            elif base == 'C':
                temp_prob = temp_prob * profile[1][y]
            elif base == 'G':
                temp_prob = temp_prob * profile[2][y]
            elif base == 'T':
                temp_prob = temp_prob * profile[3][y]
        # Sum all probs to get normalized ranges for die simulation
        #print("At position " , x , " the prob is " , temp_prob)
        kmerProbs.append(temp_prob)#([temp_prob, totalProbs])
        #totalProbs += temp_prob#
    random.seed()
    thirdTimesTheCharm = random.choices( range(0,len(dna[i-1])-k+1-1), kmerProbs)
    #print("start from die : " , thirdTimesTheCharm)
    # Get normalized probability ranges for each k-mer
    '''for x in range(0, len(dna[i - 1]) - k + 1):
        kmerProbs[x][0] = kmerProbs[x][0] / totalProbs
        kmerProbs[x][1] = kmerProbs[x][1] / totalProbs
    
    #randI = random.random()
    #newStart = 0
    #print("Randi : " , randI)
    #print("Thresholds")
    #for x in range(0, len(dna[i-1])-k+1):
        #print(x , " : " , kmerProbs[x][1])
    #print("Adds to : " , totalProbs)
    # Thresholding the random variable within the normalized distribution of all possible k-mers in the i-th sequence
    for x in range(0, len(dna[i - 1]) - k + 1):
        if randI > kmerProbs[x][1]:
            newStart = x
    '''
    #print("New start is ", newStart)
    new_kmer = dna[i - 1][thirdTimesTheCharm[0]:(thirdTimesTheCharm[0] + k)]
    #print("New kmer is " , new_kmer , " from " , dna[i-1])
    #print("New motif is : " )
    #printMotif(motifs)
    motifs[i - 1] = new_kmer  # updates the i-th kmer in the motif matrix correctly
    #printMotif(motifs)
    x=1
    return motifs


# main
def gibbsSampler(dna, k, t, N):
    # Set initial matrix with random k-mers from each sequence t
    motifs = []
    for x in range(0, t):
        random.seed()
        r = random.randint(0, len(dna[0]) - k)
        motifs.append(dna[x][r:(r + k)])
    bestMotifs = motifs
    bestScore= 100000000000
    profile = []
    iterator = 0
    o = 0
    m = 8
    # number of times to revise the motif matrix
    for j in range(0, N):
        i = random.randint(1, t)  # inclusive on both ends
        # Create profile without the i-th sequence
        profile = getProfileLessI(bestMotifs, i)#I checked this and it works as expected
        motifs = updateMotifs(profile, bestMotifs, dna, i)#The normalization is fine, the rand generator is fine, all the indexing for selecting and changing the string is fine
        
        #print("Motifs is : ")
        #printMotif(motifs)
        #print("Best is : ")
        #printMotif(bestMotifs)
        # For scoring we get the full profile
        newScore = getScore(motifs)
        if newScore < bestScore:
            bestMotifs = motifs
            bestScore = newScore
    return getScore(bestMotifs), bestMotifs


# main
with open("../../Desktop/598/rosalind_ba2g.txt", 'r') as data:
    parameters = data.readline()
    # k is length of k-mer we are searching for
    # t is number of strings (dna matrix will have 0-based indexing
    k = int(parameters.split()[0])
    t = int(parameters.split()[1])
    N = int(parameters.split()[2])
    dna = []
    for x in range(0, t):
        dna.append(data.readline().strip('\n'))
    print("T is : " , t , " and the number and length of dna is: " , len(dna), " ",  len(dna[0]) , " or  " , len(dna[1]))
    allBestMotifs = []
    bestOfTheBest = []
    # Running randomized algorithm 20 times
    for iteration in range(0, 20):
        score, motif = gibbsSampler(dna, k, t, N)
        if iteration == 0:
            bestOfTheBest = (score, motif)
        elif score < bestOfTheBest[0]:
            bestOfTheBest = (score, motif)
        allBestMotifs.append((score, motif))
    #print("All best")
    #for pair in allBestMotifs:
        #printMotif(pair[1])
    print("Returns")
    printMotif(bestOfTheBest[1])
    #realMotif = ['TCTCGGGG', 'CCAAGGTG', 'TACAGGCG', 'TTCAGGTG', 'TCCACGTG']
    realMotif = ['ACGTCCACCGGCGTC','AAGCGCACCGGGGTG','ACCCTTACCGGGGTG','AAGTTCCTCGGGGTG','AAGTTTTATGGGGTG',
                    'AAGTTTACCGGGTGC','AAGTTTCGAGGGGTG','CTGTTTACCGGGGTA','AAGTTGCTCGGGGTG','AAACATACCGGGGTG',
                    'AAGTTTAGGAGGGTG','AAGGAAACCGGGGTG','AAGTTTACACAGGTG','TAGTTTACCGGGGAT','CCTTTTACCGGGGTG','AAGTGAGCCGGGGTG',
                    'AAGTCGTCCGGGGTG','AAGTTTACCGGACAG','AAGTTTACCAATGTG','AAGTTTACCGTCATG']
    ''''''
    print("\nReal: ")
    printMotif(realMotif)