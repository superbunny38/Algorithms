class Solution:
    def activitySelection(self, start, end):
        merged = []
        for s,e in zip(start,end):
            merged.append((s,e))
        merged.sort(key=lambda x:x[1])
        
        n = 1
        prev = merged[0][1]
        # print(merged[0])
        for interval in merged[1:]:
            if interval[0]>prev:
                n+=1
                prev = interval[1]
                # print(interval)
            
        return n

start = [1, 3, 2, 5]
end = [2, 4, 3, 6]
ret = Solution().activitySelection(start=start,end=end)
print(ret)