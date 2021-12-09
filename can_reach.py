from typing import List


class Solution:
    def canReach(self, A: List[int], i: int, memo = {}) -> bool:
        if 0 <= i < len(A) and A[i] >= 0:
            A[i] = -A[i]
            return A[i] == 0 or self.canReach(A, i + A[i]) or self.canReach(A, i - A[i])
        return False
    

print(Solution().canReach([4, 2, 3, 0, 3, 1, 2], 5))
