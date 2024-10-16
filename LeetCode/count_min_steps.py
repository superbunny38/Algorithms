# Minimum steps to minimize n as per given condition
'''
Given a number n, count minimum steps to minimize it to 1 according to the following criteria: 

If n is divisible by 2 then we may reduce n to n/2.
If n is divisible by 3 then you may reduce n to n/3.
Decrement n by 1.
'''

def count_steps(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    memoization = [-1]*(n+1)
    memoization[0] = 0
    memoization[1] = 9
    memoization[2] = 1
    memoization[3] = 1
    
    for i in range(4,n+1):
        opt1, opt2 = float('inf'),float('inf')
        if i%2 == 0 and i/2>0:
            opt1 = min(opt1, memoization[int(i/2)])
        if i%3 == 0 and i/3>0:
            opt2 = min(opt2, memoization[int(i/3)])
        if i-1>0:
            opt3 = memoization[i-1]
        ans = min(opt1,opt2,opt3)+1
        memoization[i] = ans
        
    return memoization[n]
    

print(count_steps(10))
print(count_steps(6))
print(count_steps(2))
