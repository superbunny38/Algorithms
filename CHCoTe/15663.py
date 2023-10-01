#15663
import sys
input = sys.stdin.readline
from itertools import permutations

N,M = map(int,input().split())
numbers = list(map(int,input().split()))

def print_(string):
    print(" ".join([str(s_) for s_ in string]))

def sol():
    global N,M,numbers
    
    for s in sorted(set(list(permutations(numbers,M)))):
        print_(s)

sol()
