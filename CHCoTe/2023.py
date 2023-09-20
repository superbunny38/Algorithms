#2023
#신기한 소수

import sys
input = sys.stdin.readline
prime = [2,3,5,7]
N = int(input())

def is_prime(number):
    global memoization
    for i in range(2,number):
        if number%i == 0:
            return False
    #memoization[number] = 1
    return True

def sol(n):
    #print(f"solution for N({n})")
    candidates = ['2','3','5','7']
    cur_digit = 1
    while cur_digit != n:
        new_candidates = []
        while candidates:
            num = candidates.pop(0)
            for i in range(1,10):
                if is_prime(int(num+str(i))) == True:
                    new_candidates.append(num+str(i))  
        candidates = new_candidates
        cur_digit +=1
        #print(f"digit: {cur_digit}")
        #print(new_candidates)
        
            
            
    return candidates

s = sol(N)
for candi in s:
    print(candi)




