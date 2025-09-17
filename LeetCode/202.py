class Solution:
    def isHappy(self, n: int) -> bool:
        
        hashmap = dict()
        
        def rec(number):
            if number == 1:
                return True
        
            ret = 0
            for digit in str(number):
                ret += int(digit)**2
            
            if ret in hashmap:
                return False
            hashmap[ret] = ret
            return rec(ret)
        return rec(n)
 
        
    
s = Solution().isHappy(2)
print(s)
s = Solution().isHappy(71)
print(s)