import time

bList = [3,2,0,1,6,39,498,118,5,398,106,39,29,48,78,31,85,649,210]
N = len(bList)
def bubblesort(arr):
    n = len(arr)#number of values in list
    for i in range(n-1):
        for j in range(0,n-i-1):
            #swap
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

start1 = time.time()


print(bubblesort(bList))
print("time :", time.time() - start1)
 


def bubblesort2(arr):
    n = len(arr)#number of values in list
    for i in range(n-1):
        swap = 0
        for j in range(0,n-i-1):
            #swap
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap +=1
        if swap == 0:
            break
    return arr



start2 = time.time()
print(bubblesort2(bList))
print("time :", time.time() - start2)
 
def bubblesort3(A,n,s):
    swap = s
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            swap += 1
            A[j], A[j + 1] = A[j + 1], A[j]
    if swap == 0:
        return
    if n - 1 > 1:
        bubblesort3(A,n-1,swap)
 
 


start3 = time.time()
bubblesort3(bList,len(bList),1)
print(bList)
print("time :", time.time() - start3)
