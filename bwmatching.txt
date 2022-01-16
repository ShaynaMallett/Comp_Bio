##Shayna Mallett
##CSE 598 Algorithms in CompBio
##ASU Fall 2021
def printMatrix(matrix):
    string = ''
    for x in matrix:
        string += str(x) + " " 
    print(string)
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

                     
def BWMatching(first, last, patt):
    top = 0
    bottom = len(last)-1
    topIndex = 0
    bottomIndex = 0
    while(top <= bottom):
        if patt:#For each symbol in the pattern
            
            symbol = patt[len(patt)-1]
            patt = patt[0:len(patt)-1]
            
            found = False
            for i in range(top, bottom+1):#For all the indexes in the matrix that match
                if last[i] == symbol and not found:
                    topIndex = i
                    bottomIndex = i
                    found = True
                elif last[i] == symbol and found:
                    bottomIndex = i
                    
            if not found:
                return 0
            else:
                top = L_2_F(first, last, topIndex)
                bottom = L_2_F(first,last, bottomIndex)
            
        else:
            return bottom - top + 1

                

            
                        
                    
      
with open('../../Downloads/rosalind_ba9l.txt') as data:
    text = data.readline().strip('\n')
    patterns = data.readline().strip('\n').split(' ')
    print(text)
    print(patterns)
    patternOccurances = []
    transform = []
    for x in text:
        transform.append(x)        
    sortedLetters = insertionSort(transform.copy())
    for pattern in patterns:
        patternOccurances.append(BWMatching(sortedLetters, transform, pattern))
    #print(' '.join(str(patternOccurances))) #I do not know how to spell that word
    printMatrix(patternOccurances)