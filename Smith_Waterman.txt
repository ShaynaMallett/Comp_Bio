##Shayna Mallett
##CSE 598 Algorithms in CompBio
##ASU Fall 2021

blosum=  {
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


def align(alignment, backtracking):
    '''
    alignment[1][0][0] = 0
    alignment[0][0][0] = sigma
    alignment[2][0][0] = sigma
    #Initialize costs 
    maxScore = neg_inf
    maxScoreIndexes = 0,0
    #Lower level
    for x in range(1, i+1):
        alignment[0][x][0] = sigma
    for x in range(1, j+1):
        alignment[0][0][x] = sigma
           
    #Middle level
    for x in range(1, i+1):
        alignment[1][x][0] = 0
    for x in range(1, j+1):
        alignment[1][0][x] = 0
    
    #Upper level
    for x in range(1, j+1):
     alignment[2][0][x] = sigma 
    for x in range(1, i+1):
        alignment[2][x][0] = sigma
    '''
    #Only need the previous scores, should make this faster
    #all already initialized to neg inf in main
    #Initialize costs 
    maxScore = neg_inf
    maxScoreIndexes = 0,0
    for x in range(1, i+1):
        temp_alignment = [[0 for x in range(j+1)] for l in range(3)]

        for y in range(1, j+1):
            ##Start here, need to calculate backtracking on the first row and column 
            #Score based on choice
            #score = blosum.get(s[x-1]).get(t[y-1])
            #match = alignment[1][x-1][y-1] + score
            #match = algignment[1][y-1]+score
            #start_In = (alignment[1][x][y-1]+sigma)
            #start_In = temp_alignment[1][y-1]+sigma
            #extend_In = (alignment[0][x][y-1]+epsilon)
            #extend_in = temp_alignment[0][y-1]+epsilon

            #start_Del = (alignment[1][x-1][y]+sigma)
            #start_Del = alignment[1][y]+sigma
            #extend_Del = (alignment[2][x-1][y]+epsilon)
            #extend_Del = alignment[1][y]+epsilon
            #Find maximum choice score
            
            #Lower level
            temp_alignment[0][y] = max(temp_alignment[1][y-1]+sigma, temp_alignment[0][y-1]+epsilon)
            temp_alignment[2][y] = max(alignment[1][y]+sigma, alignment[2][y]+epsilon)
            ''' if alignment[0][x][y] ==  extend_In :
                #extend
                backtracking[0][x][y] = '|'#insertion
            else:
                #start
                backtracking[0][x][y] = '^'#jump up
                            
            #Upper level
            alignment[2][x][y] = max(extend_Del, start_Del)
            if alignment[2][x][y] == extend_Del:
                #extend
                backtracking[2][x][y] = '-'#deletion
            else:
                #start
                backtracking[2][x][y] = 'v'#jump down

            close_In = (alignment[0][x][y])
            close_Del = (alignment[2][x][y])
            '''
            #Middle level
            newScores = [temp_alignment[0][y], temp_alignment[2][y], alignment[1][y-1] + blosum.get(s[x-1]).get(t[y-1]), 0]
            temp_alignment[1][y] = max(newScores)
            backtracking[x][y] = newScores.index(temp_alignment[1][y])
            '''   alignment[1][x][y] = max(0, close_In, close_Del, match)
            if alignment[1][x][y] == match :#> 0:
                #match
                backtracking[1][x][y] = '\\'
            elif alignment[1][x][y] == close_Del:# > match and close_Del > 0:
                #delete
                backtracking[1][x][y] = '^'#jump up for level 2 - deletion
            elif alignment[1][x][y] == close_In:# > close_Del and close_In > match and close_In > 0:
                #insert
                backtracking[1][x][y] = 'v'#jump down for level 0 - insertion
            else:
                backtracking[1][x][y] = 's'
            '''
            #Save end of local alignment
            if temp_alignment[1][y] > maxScore:
                maxScore = temp_alignment[1][y]
                maxScoreIndexes = x,y
        alignment = temp_alignment.copy()

    #print(maxScoreIndexes)
    return maxScore, maxScoreIndexes

#Needs to have modification to both v and w in alignment, see sample data set 
def backtrack( backtracking, s, t, i, j, endIndexX, endIndexY):
    #backtrackSequence = []
    '''for x in range(i+1):
        print(backtracking[x])'''
    #backtrackSequence.append([])
    #r = s[:endIndexX]
    #u = t[:endIndexY]
    
    #not doing this anymore level = 1
    i = endIndexX
    j = endIndexY
    
    while(not ( i==0 or j==0) or not backtracking[i][j]==3):
        
        if backtracking[i][j] == 0:#inserting increment j only
            j -= 1
        elif backtracking[i][j] == 1:#deleting increment i only
            i -= 1
        elif backtracking[i][j] == 2:#match add symbol and increase i and j
            #r = s[i-1] + r
            #u = t[j-1] + u
            i -= 1
            j -= 1
        elif backtracking[i][j] == 3:
            break
            #ready to exit, this shouldn't happen
            
    return s[i:endIndexX], t[j:endIndexY]
                            



#Alignment penalty variables 
sigma = -11 #start gap
epsilon = -1 #extend gap 


with open("./rosalind_laff.txt", 'r') as data:
#with open("../../Downloads/rosalind_fa.txt", 'r') as data:
#with open("../../Downloads/rosalind_laff_840_1_dataset.txt", 'r') as data:
    #Get data
    
    data.readline()#Fasta seq name don't need
    s = ''
    string = data.readline()
    while not string[0] == '>':
        s = s + string.strip("\n")
        string = data.readline()
    string = data.readline()
    t = ''
    while string:
        t = t + string.strip("\n")
        string = data.readline()

    #print("got s and t")
    #Get lengths of sequences
    i = len(s)
    j = len(t)
    neg_inf = float('-inf')
    print(i)
    print(j)
    #Initialize backtracking and three alignment matrices
    backtracking = [[3  for x in range(j+1)] for y in range(i+1)] 
    alignment = [[0 for x in range(j+1)] for l in range(3)]

    #Align data
    result = align(alignment, backtracking)
    #Get optimal local alignment score and ending indexes of that alignment
    score = result[0]
    endIndexX = result[1][0]
    endIndexY = result[1][1]
    print(score)
    
    backtrackSequence = backtrack(backtracking, s, t, i, j, endIndexX, endIndexY)
    #print(backtrackSequence)
    with open("./rosalind_laff_answer.txt",'w') as answer:
        answer.write(str(score))
        answer.write('\n')
        answer.write(backtrackSequence[0])
        answer.write('\n')
        answer.write(backtrackSequence[1])