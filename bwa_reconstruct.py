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
    #yes i know how inefficient this is
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
        for i in range(len(front)):
            row = front[i]
            if row[len(front)-1] == '$':
                return row
        
      
with open('../../Downloads/rosalind_ba9j.txt') as data:
    text = data.readline().strip('\n')
 
    transform = []
    for x in text:
        transform.append(x)        
    sortedLetters = insertionSort(transform.copy())
    original = reconstruct(sortedLetters, transform)
    print(original)