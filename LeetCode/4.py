class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        merged = nums1+nums2

        if (n)%2 == 1:
            m_idx = int((n+1)/2)
            idx1,idx2 = 0,len(nums1)
            for _ in range(m_idx):
                if idx1 >= len(nums1):
                    get = merged[idx2]
                    idx2 +=1
                    continue
                elif idx2 >= len(merged):
                    get = merged[idx1]
                    idx1 +=1
                    continue
                if merged[idx1]<merged[idx2]:
                    get = merged[idx1]
                    idx1+=1
                else:
                    get = merged[idx2]
                    idx2+=1
            return get

        else:
            m_idx1, m_idx2 = n//2,n//2+1
            idx1,idx2 = 0,len(nums1)
            for _ in range(m_idx2):
                if idx1 >= len(nums1):
                    get = merged[idx2]
                    idx2 +=1
                    if _ == m_idx2-2:
                        prev_get = get
                    continue
                elif idx2 >= len(merged):
                    get = merged[idx1]
                    idx1 +=1
                    if _ == m_idx2-2:
                        prev_get = get
                    continue
                if merged[idx1]<merged[idx2]:
                    get = merged[idx1]
                    idx1+=1
                else:
                    get = merged[idx2]
                    idx2+=1
                if _ == m_idx2-2:
                        prev_get = get
            get = (get+prev_get)/2
            return get
