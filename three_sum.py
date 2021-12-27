from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return [[]]
        nums = sorted(nums)
        ret = []        
        for idx_a, a in enumerate(nums[:-2]):
            if idx_a > 0 and a == nums[idx_a-1]:
                continue
            if a > 0:
                break
            for idx_b, b in enumerate(nums[idx_a+1:-1]):
                if idx_b > idx_a + 1 and b == nums[idx_b-1]:
                    continue
                for idx_c, c in enumerate(nums[idx_a+1 + idx_b+1:]):
                    if idx_c > idx_b + 1 and c == nums[idx_c-1]:
                        continue
                    if a + b + c == 0 and sorted([a, b, c]) not in ret:                        
                        ret.append(sorted([a, b, c]))
        return ret

    def threeSum_optimal(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums = sorted(nums)
        ret = []
        n_len = len(nums)        
        for idx_a, a in enumerate(nums[:-2]):
            if idx_a > 0 and a == nums[idx_a-1]:
                continue
            if a > 0:
                break
            
            l = idx_a + 1
            r = n_len - 1
            while l < r:

                if a + nums[l] + nums[r] == 0:
                    if sorted([a, nums[l], nums[r]]) not in ret:
                        ret.append(sorted([a, nums[l], nums[r]]))
                    l += 1
                elif a + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return ret

print(f'Final result is {Solution().threeSum_optimal([0,0,0,0])}')