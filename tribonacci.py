class Solution:
    def tribonnaci(self, n: int) -> int:
        # Time complexity linear
        # Space complexity constant
        a, b, c = 0, 1, 1
        for i in range(n):
            a, b, c = b, c, a + b + c
        return a

print(Solution().tribonnaci(8))