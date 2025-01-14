class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n_common = 0
        left = set()
        n = len(A)
        ret = []

        for idx in range(n):
            if A[idx] in left:
                left.remove(A[idx])
                n_common+=1
            else:
                left.add(A[idx])
            
            if B[idx] in left:
                left.remove(B[idx])
                n_common+=1
            else:
                left.add(B[idx])
        
            ret.append(n_common)
            

        return ret
        
