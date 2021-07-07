#2839
#설탕배달
bagData = [-1 for _ in range(50001)]
    
def n_bag(N):
    maxi = N//3
    for i in range(maxi+1):#5
        for j in range(maxi+1):#3
            if bagData[5*i+3*j] == -1:
               bagData[5*i+3*j] = i+j
            else:
                if bagData[5*i+3*j] > i+j:
                   bagData[5*i+3*j] = i+j
    return bagData[N]
N = int(input())
print(n_bag(N))
