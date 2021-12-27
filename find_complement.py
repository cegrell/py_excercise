class Solution:
    def findComplement(self, num: int) -> int:        
        return int(format(num, 'b').translate(str.maketrans('10', '01')), 2)


print(Solution().findComplement(5))
