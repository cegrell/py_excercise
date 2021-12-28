from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []        
        nums = sorted(nums)
        len_nums = len(nums) - 1
        ret = []
        for idx_a, a in enumerate(nums[:-3]):
            if idx_a > 0 and a == nums[idx_a-1]:
                continue
            
            for idx_b_, b in enumerate(nums[idx_a+1:-2]):
                idx_b = idx_b_ + idx_a + 1
                
                l = idx_b + 1
                r = len_nums
                while l < r:                    
                    if a + b + nums[l] + nums[r] == target:                        
                        if sorted([a, b, nums[l], nums[r]]) not in ret:
                            ret.append(sorted([a, b, nums[l], nums[r]]))                        
                        l += 1
                    elif a + b + nums[l] + nums[r] < target:
                        l += 1
                    elif a + b + nums[l] + nums[r] > target:
                        r -= 1
        return ret


print(Solution().fourSum([-2,-1,-1,1,1,2,2], 0))