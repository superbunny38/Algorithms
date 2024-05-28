class Solution:
    def longestPalindrome(self, s: str) -> str:
        def if_palindrome(substring):
            start_idx,end_idx = 0, len(substring)-1
            while start_idx <= end_idx:
                if substring[start_idx] == substring[end_idx]:
                    start_idx+=1
                    end_idx-=1
                else:
                    return False
            return True
        
        def if_palindrome_exists(substring):
            last_idx = len(substring)
            while last_idx >= 1:
                if if_palindrome(substring[:last_idx]):
                    print("palindrome!",substring[:last_idx])
                    return substring[:last_idx]
                last_idx -=1
            return substring[0]
            
        if len(s)==1:
            return s
        max_length = 0
        ret = None
        first_idx = 0
        while first_idx < len(s)-1:
            print(f"1 on {s[first_idx]}({first_idx})")
            tmp_ret = if_palindrome_exists(s[first_idx:])
            if max_length < len(tmp_ret):
                max_length = len(tmp_ret)
                ret = tmp_ret
            first_idx +=1
        if ret == None:
            return s[0]
        return ret
