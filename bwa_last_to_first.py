##Shayna Mallett
##CSE 598 Algorithms in CompBio
##ASU Fall 2021
def printMatrix(matrix):
    for row in matrix:
        print(row)
def printMatrices(A, B):
    for x in range(len(A)):
        print(A[x] , "\t" , B[x])
        
def insertionSort(matrix):
    for x in range(1, len(matrix)):
        curString = matrix[x]
        j = x -1
        while j>= 0 and matrix[j] > curString:
            matrix[j+1] = matrix[j]
            j -=1
        matrix[j+1] = curString
    return matrix

def getTransform(matrix):
    transform = ''
    for row in matrix:
        transform += row[len(row)-1]
    return transform

def reconstruct(front, end):   
    for i in range(len(front)):
        front[i] = end[i]+ front[i]
    insertionSort(front)
    if len(front[0]) < len(end):
        return reconstruct(front, end)
    else:
        return front
    
def L_2_FOld(matrix, i):
    counts = [0 for y in range(0, len(matrix))]
    A = 0
    C = 0
    G = 0
    T = 0
    End = 0
    for x in range(0,len(matrix)):
        row = matrix[x]
        if row[len(matrix)-1] == 'A':
            counts[x][0] += 1
        if row[len(matrix)-1] == 'C':
            counts[x][1] +=1
        if row[len(matrix)-1] == 'T':
            counts[x][0] += 1
        if row[len(matrix)-1] == 'G':
            counts[x][0] += 1
        if row[len(matrix)-1] == '$':
            counts[x][0] += 1


def L_2_F(sortedLetters, transform, i):
    counts = [0 for y in range(0, len(transform))]
    A = 0
    C = 0
    G = 0
    T = 0
    End = 0
    for x in range(0,len(transform)):
        row = transform[x]
        if row == 'A':
            A += 1
            counts[x] = A
        if row == 'C':
            C += 1
            counts[x] = C
        if row == 'G':
            G += 1
            counts[x] = G
        if row == 'T':
            T += 1
            counts[x] = T
        if row == '$':
            End += 1
            counts[x] = End
    symbol = transform[i]
    occurence = counts[i]
    if symbol == 'A':
        return occurence
    if symbol == 'C':
        return A + occurence
    if symbol == 'G':
        return A+C+ occurence
    if symbol == 'T':
        return A+C+G+occurence
    if symbol == '$':
        return 0

          
with open('../../Downloads/rosalind_ba9k.txt') as data:
    text = data.readline().strip('\n')
    i = int(data.readline().strip('\n'))

    transform = []
    for x in text:
        transform.append(x)        
    sortedLetters = insertionSort(transform.copy())
    #matrix = reconstruct(sortedLetters, transform)
    print(i)
    #printMatrices(sortedLetters,transform)
    j = L_2_F(sortedLetters,transform, i)
    print(j)