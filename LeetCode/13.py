class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_to_num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        indices = ['I','V','X','L','C','D','M']
        summ = 0
        idx = 0
        s = list(s)
        while s:
            if len(s) == 1:
                print("+",s[0])
                summ += symbol_to_num[s.pop(0)]
                return summ
            prev,after = s[idx],s[idx+1]
            print(f"prev:{prev} ({symbol_to_num[prev]}) after:{after} ({symbol_to_num[after]})")
            if symbol_to_num[prev] < symbol_to_num[after]:
                summ += symbol_to_num[after]-symbol_to_num[prev]
                print("+",symbol_to_num[after]-symbol_to_num[prev])
                s.pop(0)
                s.pop(0)
            else:
                summ += symbol_to_num[prev]
                print("+",symbol_to_num[prev])
                s.pop(0)
            
        return summ
                
            
s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
