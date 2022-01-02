
def bubblesort(arr):
    n = len(arr)#number of values in list
    for i in range(n-1):
        for j in range(0,n-i-1):
            #swap
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



arr = [32,23,18,7,11,99,55]
print(bubblesort(arr))
