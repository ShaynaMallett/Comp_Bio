##Shayna Mallett
##CSE 598 Algorithms in CompBio
##ASU Fall 2021

with open('rosalind_dna.txt', 'r') as data:
    dna = data.readline()
    a = 0
    c = 0
    g = 0
    t = 0
    for n in dna:
        if n=='A':
            a+=1
        elif n=='C':
            c+=1
        elif n=='G':
            g+=1
        elif n=='T':
            t+=1                        
    print(a , " " , c , " " , g , " " , t)        
    data.close