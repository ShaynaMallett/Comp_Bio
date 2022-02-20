##Shayna Mallett
##CSE 598 Algorithms in CompBio
##ASU Fall 2021

def blosum(x, y):
    score =  {
        'A' : {'A': 4 , 'C':0, 'D':-2, 'E':-1, 'F':-2,'G':0,'H':-2,'I':-1,'K':-1,'L':-1,'M':-1,'N':-2,'P':-1,'Q':-1,'R':-1,'S':1,'T':0,'V':0,'W':-3,'Y':-2},
        'C' : {'A': 0 , 'C':9, 'D':-3, 'E':-4, 'F':-2,'G':-3,'H':-3,'I':-1,'K':-3,'L':-1,'M':-1,'N':-3,'P':-3,'Q':-3,'R':-3,'S':-1,'T':-1,'V':-1,'W':-2,'Y':-2},
        'D' : {'A': -2 , 'C':-3, 'D':6, 'E':2, 'F':-3,'G':-1,'H':-1,'I':-3,'K':-1,'L':-4,'M':-3,'N':1,'P':-1,'Q':0,'R':-2,'S':0,'T':-1,'V':-3,'W':-4,'Y':-3},
        'E' : {'A': -1 , 'C':-4, 'D':2, 'E':5, 'F':-3,'G':-2,'H':0,'I':-3,'K':1,'L':-3,'M':-2,'N':0,'P':-1,'Q':2,'R':0,'S':0,'T':-1,'V':-2,'W':-3,'Y':-2},
        'F' : {'A': -2 , 'C':-2, 'D':-3, 'E':-3, 'F':6,'G':-3,'H':-1,'I':0,'K':-3,'L':0,'M':0,'N':-3,'P':-4,'Q':-3,'R':-3,'S':-2,'T':-2,'V':-1,'W':1,'Y':3},
        'G' : {'A': 0 , 'C':-3, 'D':-1, 'E':-2, 'F':-3,'G':6,'H':-2,'I':-4,'K':-2,'L':-4,'M':-3,'N':0,'P':-2,'Q':-2,'R':-2,'S':0,'T':-2,'V':-3,'W':-2,'Y':-3},
        'H' : {'A': -2 , 'C':-3, 'D':-1, 'E':0, 'F':-1,'G':-2,'H':8,'I':-3,'K':-1,'L':-3,'M':-2,'N':1,'P':-2,'Q':0,'R':0,'S':-1,'T':-2,'V':-3,'W':-2,'Y':2},
        'I' : {'A': -1 , 'C':-1, 'D':-3, 'E':-3, 'F':0,'G':-4,'H':-3,'I':4,'K':-3,'L':2,'M':1,'N':-3,'P':-3,'Q':-3,'R':-3,'S':-2,'T':-1,'V':3,'W':-3,'Y':-1},
        'K' : {'A': -1 , 'C':-3, 'D':-1, 'E':1, 'F':-3,'G':-2,'H':-1,'I':-3,'K':5,'L':-2,'M':-1,'N':0,'P':-1,'Q':1,'R':2,'S':0,'T':-1,'V':-2,'W':-3,'Y':-2},
        'L' : {'A': -1 , 'C':-1, 'D':-4, 'E':-3, 'F':0,'G':-4,'H':-3,'I':2,'K':-2,'L':4,'M':2,'N':-3,'P':-3,'Q':-2,'R':-2,'S':-2,'T':-1,'V':1,'W':-2,'Y':-1},
        'M' : {'A': -1 , 'C':-1, 'D':-3, 'E':-2, 'F':0,'G':-3,'H':-2,'I':1,'K':-1,'L':2,'M':5,'N':-2,'P':-2,'Q':0,'R':-1,'S':-1,'T':-1,'V':1,'W':-1,'Y':-1},
        'N' : {'A': -2 , 'C':-3, 'D':1, 'E':0, 'F':-3,'G':0,'H':1,'I':-3,'K':0,'L':-3,'M':-2,'N':6,'P':-2,'Q':0,'R':0,'S':1,'T':0,'V':-3,'W':-4,'Y':-2},
        'P' : {'A': -1 , 'C':-3, 'D':-1, 'E':-1, 'F':-4,'G':-2,'H':-2,'I':-3,'K':-1,'L':-3,'M':-2,'N':-2,'P':7,'Q':-1,'R':-2,'S':-1,'T':-1,'V':-2,'W':-4,'Y':-3},
        'Q' : {'A': -1 , 'C':-3, 'D':0, 'E':2, 'F':-3,'G':-2,'H':0,'I':-3,'K':1,'L':-2,'M':0,'N':0,'P':-1,'Q':5,'R':1,'S':0,'T':-1,'V':-2,'W':-2,'Y':-1},
        'R' : {'A': -1 , 'C':-3, 'D':-2, 'E':0, 'F':-3,'G':-2,'H':0,'I':-3,'K':2,'L':-2,'M':-1,'N':0,'P':-2,'Q':1,'R':5,'S':-1,'T':-1,'V':-3,'W':-3,'Y':-2},
        'S' : {'A': 1 , 'C':-1, 'D':0, 'E':0, 'F':-2,'G':0,'H':-1,'I':-2,'K':0,'L':-2,'M':-1,'N':1,'P':-1,'Q':0,'R':-1,'S':4,'T':1,'V':-2,'W':-3,'Y':-2},
        'T' : {'A': 0 , 'C':-1, 'D':-1, 'E':-1, 'F':-2,'G':-2,'H':-2,'I':-1,'K':-1,'L':-1,'M':-1,'N':0,'P':-1,'Q':-1,'R':-1,'S':1,'T':5,'V':0,'W':-2,'Y':-2},
        'V' : {'A': 0 , 'C':-1, 'D':-3, 'E':-2, 'F':-1,'G':-3,'H':-3,'I':3,'K':-2,'L':1,'M':1,'N':-3,'P':-2,'Q':-2,'R':-3,'S':-2,'T':0,'V':4,'W':-3,'Y':-1},
        'W' : {'A': -3 , 'C':-2, 'D':-4, 'E':-3, 'F':1,'G':-2,'H':-2,'I':-3,'K':-3,'L':-2,'M':-1,'N':-4,'P':-4,'Q':-2,'R':-3,'S':-3,'T':-2,'V':-3,'W':11,'Y':2},
        'Y' : {'A': -2 , 'C':-2, 'D':-3, 'E':-2, 'F':3,'G':-3,'H':2,'I':-1,'K':-2,'L':-1,'M':-1,'N':-2,'P':-3,'Q':-1,'R':-2,'S':-2,'T':-2,'V':-1,'W':2,'Y':7}
    }
    return score.get(x).get(y)

def printBlosum():
    print('   A C D E F G H I K L M N P Q R S T V W Y')
    for x in 'ACDEFGHIKLMNPQRSTVWY':
        row = ' ' + str(x) + ' '
        for y in 'ACDEFGHIKLMNPQRSTVWY':
            row += str(blosum(x, y))+ ' '
        print(row)
          
def printMatrix(matrix):
    for y in range(len(matrix[0])):
        row = ""
        for x  in range(len(matrix)):
            row += str(matrix[x][y])
            row += " " 
        print(row)

def align(alignment, backtracking):
    alignment[0][0] = 0
    for x in range(1, i+1):
        alignment[x][0] = alignment[x-1][0]+sigma
    for y in range(1, j+1):
        alignment[0][y] = alignment[0][y-1]+sigma
    for x in range(1, i+1):
        for y in range(1, j+1):
            match = 0
            match = blosum(v[x-1], w[y-1])
            #print("For :" , x , " and " , y , " the letters are " , v[x-1] , " and " , w[y-1], " score is " , match)
            alignment[x][y] = max(alignment[x-1][y]+sigma, alignment[x][y-1]+sigma, alignment[x-1][y-1]+ match)
            if alignment[x][y] == alignment[x-1][y]+sigma:
                    backtracking[x][y]= '-'
            elif alignment[x][y] == alignment[x][y-1]+sigma:
                    backtracking[x][y]='|'
            elif alignment[x][y] == alignment[x-1][y-1]+match:
                    backtracking[x][y]="\\"
    return alignment[i][j]

#Needs to have modification to both v and w in alignment, see sample data set 
def backtrack( backtracking, v, w, i, j):
    #is recursive
    #python can suck it
    backtrackSequence = ''
    while(not ( i==0 or j==0)):

        if backtracking[i][j]== '|':#If we have insertion in w
            backtrackSequence = '|' + backtrackSequence #Building the string from the backwards out
            j = j-1 #change current position
            #return backtrack( backtracking, v, w, i, j-1)+'|'
        elif backtracking[i][j]=='-':
            backtrackSequence = '-' + backtrackSequence
            i = i-1
            #return backtrack( backtracking, v, w, i-1, j)+ '-'
        elif backtracking[i][j]=="\\":
            backtrackSequence = "\\" + backtrackSequence
            i = i-1
            j = j-1
            #return backtrack( backtracking, v, w, i-1, j-1)+"\\"
    return backtrackSequence


def constructSequences(backtrackSequence, v, w):
    new_v = ''
    new_w = ''
    i = 0
    j = 0
    for y in range(len(backtrackSequence)):
        x = backtrackSequence[y]
        if x == '|':
            new_v += '-'
            new_w += w[j]
            j+=1
        if x == '-':
            new_v += v[i]
            new_w += '-'
            i+=1
        if x == "\\":
            new_v += v[i]
            new_w += w[j]
            i+=1
            j+=1
    return new_v, new_w
sigma = -5
# main function
with open("../../Downloads/rosalind_ba5e.txt", 'r') as data:
    v = data.readline().strip("\n")
    w = data.readline().strip("\n")
    i = len(v)
    j = len(w)
    neg_inf = float('-inf')
    backtracking = [['.' for x in range(j+1)] for y in range(i+1)]

     
    alignment = [[neg_inf for x in range(j+1)] for y in range(i+1)]
    score = align(alignment, backtracking)
    print(score)
    backtrackSequence = backtrack(backtracking, v, w, i, j)
    new = constructSequences(backtrackSequence, v, w)
    new_v = new[0]
    new_w = new[1]
 
    print(new_v)
    print(new_w)