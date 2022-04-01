N = int(input())
from itertools import combinations
from itertools import permutations

def find_degree(N):
    degree = 0
    while True:
        N = N/10
        degree += 1
        if N < 10:
            break
    return int(degree)

def find_answer(N):
    
    d = find_degree(N)
    if d < 2:
        print(0)
        return
    multiple = []
    print(d)
    k = d
    for _ in range(d+1):
        multiple.append(10**(k)+1)
        k -= 1
    multiple.sort()
    digits = [9,8,7,6,5,4,3,2,1,0]

    #print("multiple:",multiple)
    combination = permutations(digits, len(multiple))

    possible_answers = []
    for perm in list(combination):
        summation = 0
        for p,m in zip(perm, multiple):
            #print(p,m)
            summation += p*m
        #print("summation:",summation)
        if summation == N:
            possible_answers.append(perm)
            
    #print(possible_answers)

    result = possible_answers[0]
    result = result[::-1]
    result = [str(x) for x in result]
    print("".join(result))

find_answer(N)
