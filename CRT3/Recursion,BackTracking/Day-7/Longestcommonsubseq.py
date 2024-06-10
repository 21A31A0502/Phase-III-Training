def longestCommonSubsequence(text1,text2):
        n1=len(text1)
        n2=len(text2)
        def recursiveapproach(index1,index2):
            if index1 == n1 or  index2 == n2:
                return 0
               
            elif text1[index1] == text2[index2]:
                return 1+recursiveapproach(index1+1,index2+1) 
            ch1=recursiveapproach(index1+1,index2)
            ch2=recursiveapproach(index1,index2+1)
            return max(ch1,ch2)
           
        cache=[[-1]*n2 for i in range(n1)]    
        def memonizationapproach(index1,index2):
            if index1 == n1 or  index2 == n2:
                return 0
            elif cache[index1][index2] != -1:
                return cache[index1][index2]    
            elif text1[index1] == text2[index2]:
                cache[index1][index2]= 1+memonizationapproach(index1+1,index2+1)
                return cache[index1][index2] 
            ch1=memonizationapproach(index1+1,index2)
            ch2=memonizationapproach(index1,index2+1)
            cache[index1][index2]=max(ch1,ch2)
            return cache[index1][index2]
                
        def tabulation():
            cache=[[0]*(n2+1) for i in range(n1+1)]
            for index1 in range(n1-1,-1,-1):
                for index2 in range(n2-1,-1,-1):
                    if text1[index1]==text2[index2]:
                        cache[index1][index2] = 1 + cache[index1 + 1][index2 + 1]
                    else:
                        ch1 = cache[index1 + 1][index2]
                        ch2 = cache[index1][index2 + 1]
                        cache[index1][index2] = max(ch1, ch2)
 
            return cache[0][0]
 
        return tabulation()    
text1="abc"
text2="def"
print(longestCommonSubsequence(text1,text2))    