class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        dp = [[0]*n for _ in range(n)]
        
        for dist in range(2,n):
            for i in range(n-dist):
                j = dist+i
                dp[i][j] = float('inf')
                for k in range(i+1,j):
                    cur_val = dp[i][k]+dp[k][j]+arr[i]*arr[k]*arr[j]
                    if cur_val<dp[i][j]:
                        dp[i][j] = cur_val
        return dp[0][-1]
