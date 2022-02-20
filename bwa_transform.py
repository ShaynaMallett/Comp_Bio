##Shayna Mallett
##CSE 598 Algorithms in CompBio
##ASU Fall 2021
def printMatrix(matrix):
    for row in matrix:
        print(row)
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
      
with open('../../Downloads/rosalind_ba9i.txt') as data:
    text = data.readline().strip('\n')
    matrix = []
    
    #Construct matrix
    for x in range(len(text)):
        matrix.append(text)
        text = text[1:(len(text))] + text[0]
        
    #Sort and print
    matrix = insertionSort(matrix) 
    print(getTransform(matrix))