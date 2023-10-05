#1193
#분수찾기

import sys
import copy

input = sys.stdin.readline

def sol(th):
    start_r = 1
    elems = 0
    if th == 1:
        return '1/1'
    #print(elems,end = "")
    while True:
        #print(f"+{start_r}",end = " ")
        elems += start_r
        start_r +=1
        if elems + start_r >= th:
            break
        
    n_move = th-elems
    #print("= elems:",elems)
    #print("n_move:",n_move)
    #print("start_r:",start_r)
    
    if start_r%2==0:#짝수
        numer = 1
        for i in range(n_move-1):
            numer +=1
        #print("짝")
        frac = f'{numer}/{start_r+1-numer}'
    else:
        #print("짝")
        numer = copy.deepcopy(start_r)
        for i in range(n_move-1):
            numer -=1
        frac = f'{numer}/{start_r+1-numer}'
    return frac


X = int(input())
print(sol(X))
