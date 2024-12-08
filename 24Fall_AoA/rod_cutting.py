
def bottomup(price,n):
    memoization = [0]*(n+1)
    for i in range(1,n+1):
        max_price = -float('inf')
        for j in range(0,i):
            max_price = max(max_price,memoization[i-j-1]+price[j])
        memoization[i] = max_price
    return memoization[-1]

def recursive(price,n,val):
    if n == 0:
        return 0
    
    if val[n] != -1:
        return val[n]
    
    max_price = -1
    for i in range(1,n+1):
        max_price = max(max_price,price[i-1]+recursive(price,n-i,val))    
    val[n] = max_price
    return max_price

def topdown(price,n):
    val = [-1]*(n+1)
    return recursive(price,n,val)

'''
price[] = {1, 5, 8, 9, 10, 17, 17, 20}
n = 8
'''

price = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8

print(bottomup(price,n))

print(topdown(price=price,n=n))