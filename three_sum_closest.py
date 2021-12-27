from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        sum_nums = None
        nums_len = len(nums)
        for idx, a in enumerate(nums):            
            l = idx + 1
            r = nums_len - 1            
            while l < r:                
                cur_sum = a + nums[l] + nums[r]
                if sum_nums is None or abs(target - cur_sum) < abs(target - sum_nums):
                    sum_nums = cur_sum                
                if cur_sum > target:
                    r -= 1
                else:
                    l += 1
        return sum_nums

print(Solution().threeSumClosest([-1,2,1,-4], 1))