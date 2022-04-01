from itertools import combinations

def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]   
 
    for j in range(low, high):
 
        if arr[j] <= pivot:
 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def howmany(arr,m):
    #print("arr:",arr)
    count = 0
    combi = combinations(arr,2)
    combi = list(combi)
    for c in combi:
        c0 = int(c[0])
        c1 = int(c[1])
        if c0+c1 == m:
            count+=1
    return count

N = int(input())
M = int(input())

arr = input().split()#[10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)

print(howmany(arr,M))
 
