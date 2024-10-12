class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
            
        mem = [0]*(n+1)
        mem[1] = 1
       
        for i in range(2,n+1):
            mem[i] = mem[i-1]+mem[i-2]
        return mem[n]
        
