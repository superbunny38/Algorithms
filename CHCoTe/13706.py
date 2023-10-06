#13706
#제곱근

import sys
import math

input = sys.stdin.readline

def sol(number):
    start = 1
    end = number

    while True:
        mid_point = (start+end)//2
        double = mid_point**2 
        if double == number:
            print(mid_point)
            return
        elif double < number:
            start = mid_point+1
        else:
            end = mid_point-1
            

N = int(input())
sol(N)
