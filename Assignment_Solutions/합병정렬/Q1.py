# Type or paste your code in this area
#2018312824
#류채은

#입력
N = int(input())
num_list = list(map(int,input().strip().split()))[:N]

def print_yohans(L):
    for idx, value in enumerate(L):
        if idx == len(L)-1:
            print(f" {value}")
        else:
            print(f" {value}", end = "")
            
def isEmpty(L):
    if len(L) == 0:
        return True
    else:
        return False

def merge(L1,L2):
    L = []#empty list
    while isEmpty(L1) != True and isEmpty(L2) != True:
        if L1[0] <= L2[0]:
            L.append(L1.pop(0))
        else:
            L.append(L2.pop(0))
            
    while isEmpty(L1) != True:
        L.append(L1.pop(0))

    while isEmpty(L2) != True:
        L.append(L2.pop(0))

    return L

def partition(L,half_idx):
    return L[:half_idx], L[half_idx:]
    
def mergeSort(L):
    n = len(L)
    
    if len(L)>1:
        L1,L2 = partition(L, int(n//2))
        #print(f"L1:{L1} L2:{L2}")
        L1 = mergeSort(L1)
        L2 = mergeSort(L2)
        L = merge(L1,L2)
        #print(f"merged:{L}")
    return L

num_list = mergeSort(num_list)
print_yohans(num_list)
