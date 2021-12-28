from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        :type digits: str
        :rtype: List[str]
        """
        d2l_map = {'2':['a','b','c'],
                   '3':['d','e','f'],
                   '4':['g','h','i'],
                   '5':['j','k','l'],
                   '6':['m','n','o'],
                   '7':['p','q','r','s'],
                   '8':['t','u','v'],
                   '9':['w','x','y','z']
                   }
        q = []
        res = []
        for s in reversed(digits):
            q.append(s)

        while q:
            num = q.pop()
            append_letters = d2l_map[num]
            tmp_res = []
            if not res:
                res = append_letters
            else:
                for substr in res:
                    substr_extended = [substr + cur_letter for cur_letter in append_letters]
                    tmp_res.extend(substr_extended)
                res = tmp_res

        return res


print(list(Solution().letterCombinations("23")))
