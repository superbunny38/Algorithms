#5582
import sys
input = sys.stdin.readline

def solution(S1,S2):
    length1, length2 = len(S1),len(S2)
    memoization = [[0]*length2 for _ in range(length1)]
    answer = 0
    for i in range(1,length1):
        for j in range(1,length2):
            if S1[i-1] == S2[j-1]:
                memoization[i][j] = memoization[i-1][j-1]+1
                answer = max(answer,memoization[i][j])
    return answer

s1 = input()
s2 = input()
print(solution(s1,s2))
