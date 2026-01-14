class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        # 'path' is the current permutation we are building (e.g., [1, 2])
        # 'remaining' is the list of numbers we haven't used yet
        def backtrack(path, remaining):
            
            # 1. BASE CASE: No numbers left to pick?
            # We found a complete permutation!
            if not remaining:
                result.append(path)
                return

            # 2. RECURSIVE STEP
            # Try picking every available number one by one
            for i in range(len(remaining)):
                
                # The number we pick now
                current_num = remaining[i]
                
                # The numbers left after picking this one
                # (All numbers before index i + All numbers after index i)
                next_remaining = remaining[:i] + remaining[i+1:]
                
                # Recurse: Add current_num to path, pass the new remaining list
                backtrack(path + [current_num], next_remaining)

        # Start with empty path, and all numbers available
        backtrack([], nums)
        return result
