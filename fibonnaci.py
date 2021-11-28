class Solution:
    def fib(self, n: int) -> int:
        # Recursive appraoch
        # This is a slow solution, wouldnt want to do it with larger Ns
        # with recursion, working backwards and building up the numbers from the base case
        # An iterative approach would start fr the base case directly and build up
        # Time complexity of Fibonacci recurisve is exponential, ie O(2^n)
        # Space complexity of recursive is linear, as the maximum depth is proportional
        # to the n
        if n == 0: return 0
        if n == 1: return 1
        return self.fib(n-2) + self.fib(n-1)
    
    def fib_iterative(self, n: int) -> int:
        # Iterative approach
        # Time complexity is linear, O(n)
        # Space complexity must be linear since more cache for higher input
        seen = {0: 0, 1: 1}
        for i in range(2, n+1):
            seen[i] = seen[i - 1] + seen[i - 2]

        return seen[n]

    def fib_iterative_no_cache(self, n: int) -> int:
        # Iterative approach
        # Time complexity is linear, O(n)
        # Space complexity is constant, O(1)
        a, b = 0, 1
        for i in range(0,n):
            a, b = b, a + b
        return a


    def fib_w_memo_obj(self, n: int, memo: dict = {}):        
        if n in memo: return memo[n] # Add the memo case
        if n == 0: return 0
        if n == 1: return 1
        memo[n] = self.fib_w_memo_obj(n-2, memo) + self.fib_w_memo_obj(n-1, memo)
        return memo[n]


if __name__ == '__main__':
    print(Solution().fib_w_memo_obj(150))
