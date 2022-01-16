##Shayna Mallett
##CSE 598 Algorithms in CompBio
##ASU Fall 2021

with open("rosalind_subs.txt", 'r') as input:
    s = input.readline().strip('\n')
    t = input.readline().strip('\n')

##Variables
    t_len = len(t)
    s_len = len(s) 
    z_string = t + '#' + s
    #First position of string matches the entire string, don't calculate
    z = [0] 
    l = -1
    r = -1
    beta = -1
    k = 1
    kp = -1
    ktmp = -1
    matches = []
    print(z_string)
##Construct z array 
    for k in range(1,len(z_string)-1):
        
        if k > r:
            #Character comparisons
            if z_string[k] == z_string[0]:
                #start new z box
                l = k
                ktmp = k
                #print(ktmp)
                while z_string[ktmp] == z_string[ktmp-k] and ktmp < len(z_string)-1:
                    #print(ktmp)
                    ktmp = ktmp + 1
                    
                    
                r = ktmp - 1
                
                z.append(r-l+1)
                if r-l+1 == t_len:
                    matches.append(l-t_len)
                
            else:
                z.append(0)
        else:
            kp = k - l 
            beta = r - k + 1
            if z[kp] < beta:
                z.append(z[kp])
            elif z[kp] > beta:
                z.append(beta)
                print("hello")
            else:
                #Character comparisons
                #Need to update z box    
                l = k
                ktmp = k + beta
                while z_string[ktmp] == z_string[ktmp-k]and ktmp < len(z_string)-1:
                    ktmp = ktmp + 1
                r = ktmp - 1
                z.append(r-l+1)
                if r-l+1 == t_len:
                        matches.append(l-t_len)
    print(*matches, sep=' ')
    print(z)


    #Convert the resulting z-array and the text into an lps' algorithm
    lpsP = [0]#first index
    #For each z value, we move to the index of the end of the indicated prefix(because we are dealing with suffixes)
    #And assign the same value to that new position of the lps' array
    i = 1
    #but what if they overlap ? 
    while i < len(z):
        if z[i] > 1:
            y = i+z[i] - 1
            #print("y is " , y)
            val = z[i]
            #print("val is " , val)
            while i < y:
                #print("replacing " , z[i], " with 0" )
                lpsP.append(0)
                i = i+1
            lpsP.append(val)
            #print("replacing 0 with " , val)
            i = i+1
        else:
            #Case 0 and 1 should be the same between the arrays
            lpsP.append(z[i])
            i = i+1
        
    print("z = " , z)
    print("lpsP = " , lpsP)