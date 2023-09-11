#9251
#LCS

import sys
input = sys.stdin.readline
str1 = input()[:-1]
str2 = input()[:-1]

def dp(string1, string2):
    memoization = []
    length1,length2 = len(string1), len(string2)
    #print("length1:",length1)
    #print("length2:",length2)
    for row_idx in range(length1+1):
        tmp = [0]*(length2+1)
        memoization.append(tmp)
    #print("memoization:")
    #for m in memoization:
    #    print(m)
    #print()
    #점화식
    #문자가 같을 때: m[i][j] = m[i-1][j-1]+1
    #문자가 다를 때: m[i][j] = max(m[i-1][j],m[i][j-1])
   
    for i in range(1,length1+1,1):
        for j in range(1,length2+1,1):
            if string1[i-1] == string2[j-1]:
                memoization[i][j] = memoization[i-1][j-1]+1
            else:
                memoization[i][j] = max(memoization[i-1][j],memoization[i][j-1])
    #print("memoization:")
    #for m in memoization:
    #    print(m)
    #print()
    return memoization[length1][length2]

print(dp(str1,str2))
