#3273
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))
x = int(input())

#1, 12
#2, 11
#3, 10


numbers = sorted(numbers)
count = 0

start_idx, end_idx = 0,n-1

while start_idx < end_idx:
    #print(start_idx)
    #print(end_idx)
    if numbers[start_idx]+numbers[end_idx] == x:
        #print(f"start_Idx: {start_idx} end_idx:{end_idx}")
        #print(f"found! {numbers[start_idx]}+{numbers[end_idx]}={x}")
        start_idx += 1
        count +=1
    elif numbers[start_idx]+numbers[end_idx] > x:
        end_idx -=1
    else:#numbers[start_idx]+numbers[end_idx] < x
        start_idx +=1
        

        
print(count)
