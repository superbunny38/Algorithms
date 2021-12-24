#10817

n, x = map(int,input().split())
array = list(map(int, input().split()))


for i in range(len(array)):
    if x > array[i]:
        print(array[i],end=" ")
        
    
