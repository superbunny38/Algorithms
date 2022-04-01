def bubblesort(arr):
    n = len(arr)#number of values in list
    for i in range(n-1):
        for j in range(0,n-i-1):
            #swap
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def bin_search(ss,key):
    low = 0
    high = len(ss)-1
    while low<=high:
        mid = (high+low)//2
        if key == ss[mid]:
            return mid
        elif key<ss[mid]:
            high = mid-1
        else:
            low = mid+1
    return None

def binary_search(arr, score):
    # 코드를 작성하세요
    arr = bubblesort(arr)
    print(arr)
    rank = len(arr)-bin_search(arr,score)
    return rank
# 파일 불러오기 코드 작성 
scores = []
with open("scores.txt","r") as f:   
    for line in f:
        scores.append(line)

real_scores = []
for s in scores:
    real_scores.append(s[:-1])
scores = []
for s in real_scores:
    scores.append(float(s))
#print(scores)
#### do not edit this ####
my_score = 81
rank = binary_search(scores, my_score)
print(f'{my_score}은 {rank}등 입니다')
