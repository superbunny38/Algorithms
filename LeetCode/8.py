class Solution:
    def myAtoi(self, s: str) -> int:
        read = []
        s = list(s)

        if len(s) == 0:
            return 0
        print("s:",s)
        print("s[0]:",s[0])
        while s:
            if s[0] == ' ':
                s.pop(0)
            else:
                break
            
        if len(s) == 0:
            return 0

        if s[0] == '-':
            sign = '-'
            s = s[1:]
        elif s[0] == '+':
            sign = ''
            s = s[1:]
        else:
            sign = ''
        read.append(sign)
        print("s:",s)
        print("1. read:",read)
        if len(s) == 0:
            return 0
        
        while s[0] == '0':
            if len(s)>2:
                if s[1].isnumeric():
                    s.pop(0)
                    read.append('0')
                else:
                    break
            else:
                break
                
        print("2. read:",read)
        if len(s) == 0:
            return 0
        for idx in range(len(s)):
            if s[idx].isnumeric() == False:
                break
            else:
                read.append(s[idx])
        if len(read) == 1:
            return 0
        s = int(read[0]+"".join(read[1:]))
        if s < -2**31:
            s = -2**31
        elif s > 2**31-1:
            s = 2**31-1
        return s
