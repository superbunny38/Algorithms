A = [5,3,2,7,8,1,0,5,1]
j =1
n = len(A)
while j<n:
    key = A[j]
    i = j-1
    while i >= 0 and A[i]>key:
        A[i+1] = A[i]
        i = i-1
    j = j+1
    A[i+1] = key
print(A)
