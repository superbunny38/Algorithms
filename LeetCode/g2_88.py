class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n == 0:
            return
        elif m == 0  and n!=0 :
            for idx in range(n):
                nums1[idx] = nums2[idx]
            return
        else:
            space_pointer,pointer1,pointer2 = n+m-1,m-1,n-1
            while pointer2>=0:
                num1,num2 = nums1[pointer1],nums2[pointer2]
                # print("current nums1:",nums1)
                # print(f"num1:{num1} num2:{num2} space_pointer at:{space_pointer}")
                # print()
                if num1<=num2:
                    nums1[space_pointer] = num2
                    space_pointer-=1
                    pointer2 -=1
                    
                elif num1>num2:
                    nums1[space_pointer] = num1
                    nums1[pointer1] = -float('inf')
                    pointer1 -= 1
                    space_pointer -=1
                    
                    if pointer1 <0:
                        while space_pointer >=0:
                            nums1[space_pointer] = num2
                            space_pointer -=1
                            pointer2 -= 1
                            num2 = nums2[pointer2]
                        break
