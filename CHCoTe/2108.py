#2108
#통계학
import sys
input = sys.stdin.readline
N = int(input())
numbers = []
count = {}

for i in range(N):
    number = int(input())
    numbers.append(number)
numbers = sorted(numbers)

for number in numbers:
    if number not in count:
        count[number] = 1
    else:
        count[number] += 1
    
    
#print(count)
def sol(numbers,N):
    global count
    
    print(round(sum(numbers)/N))
    if N%2 == 0:
        print((numbers[N//2]+numbers[N//2-1])/2)
    else:
        print(numbers[(N-1)//2])
    sorted_v = sorted(count.items(), key = lambda x: x[1],reverse = True)
    #print(sorted_v)
    if N>1 and sorted_v[0][1] == sorted_v[1][1]:
        print(sorted_v[1][0])
    else:
        print(sorted_v[0][0])
    print(max(numbers)-min(numbers))

sol(numbers,N)
    
    
