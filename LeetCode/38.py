class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        else:
            rec = self.countAndSay(n-1)

            cur_idx = 0
            peek_idx = cur_idx +1
            ret = ""
            count = 1

            while cur_idx < len(rec):
                if peek_idx < len(rec):
                    if rec[cur_idx]!= rec[peek_idx]:
                        ret += str(count)+rec[cur_idx]
                        cur_idx = peek_idx
                        peek_idx = cur_idx +1
                        count = 1
                    else:
                        count +=1
                        peek_idx +=1
                else:
                    ret += str(count)+rec[cur_idx]
                    cur_idx = peek_idx

            print(f"n:{n} ret:{ret}")
            return ret
