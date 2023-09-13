#1759
#암호 만들기

from itertools import combinations
import sys
input = sys.stdin.readline

def check(string):
    n_moum = 0
    n_jaum = 0
    for s in string:
        assert s.isalpha() == True
        if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s== 'u':
            n_moum +=1
        else:
            n_jaum +=1
    if n_moum >= 1 and n_jaum >= 2:
        return True
    else:
        return False

L, C = map(int, input().split())
letters = sorted(list(input().split()))

#print("sorted:",letters)

for c in list(combinations(letters,L)):
    pw = "".join(c)
    if check(pw) == True:
        print(pw[:L])
    else:
        continue
