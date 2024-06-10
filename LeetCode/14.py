class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = 201
        for str_ in strs:
            min_length = min(min_length, len(str_))
        
        end_idx = 1
        ret = ""
        common_str = strs[0][:end_idx]
        while True:
            print("end_idx:",end_idx)
            if end_idx > min_length:
                break
            for str_ in strs:
                if common_str == str_[0:end_idx]:
                    continue
                else:
                    print(f"returning... {common_str} != { str_[0:end_idx]}")
                    return ret
            ret = common_str
            end_idx +=1
            common_str = str_[0:end_idx]
            print("common_str:",common_str)
            
        return ret
