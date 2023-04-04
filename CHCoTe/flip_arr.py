def exoj_print(arr):
    for idx, num in enumerate(arr):
        if idx == len(arr)-1:
            print(num)
        else:
            print(num, end = " ")

def flip_ret(num_arr,flip_ranges):
    for i in range(0,len(flip_ranges),2):
        start,end = flip_ranges[i],flip_ranges[i+1]
        num_arr[start:end+1] = num_arr[start:end+1][::-1]
    num_arr = [int(x) for x in num_arr]
    return num_arr    
        
n = int(input())
li = input().split()
li = [x.replace('\U00002013', '-') for x in li]
num_arr = list(map(float, li))
n_flip = int(input())
flip_ranges = list(input().split())
flip_ranges = [int(x) for x in flip_ranges]

assert len(flip_ranges) %2 == 0
assert len(flip_ranges)//2 == n_flip

exoj_print(flip_ret(num_arr,flip_ranges))
# Type or paste your code in this area
