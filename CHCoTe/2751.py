#2751
import sys
input = sys.stdin.readline
N = int(input())
numbers = []
for _ in range(N):
    n = int(input())
    numbers.append(n)

for number in sorted(numbers):
    print(number)
