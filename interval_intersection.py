from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if (len(firstList) == 0) | (len(secondList) == 0): return [] 
        idx_f, idx_s = 0, 0
        ret = []
        m, n = len(firstList), len(secondList)
        print(m, n)
        while (idx_f < m) & (idx_s < n):
            
            start_f, start_s  = firstList[idx_f][0], secondList[idx_s][0]
            end_f, end_s = firstList[idx_f][1], secondList[idx_s][1]

            common_start = max(start_f, start_s)
            common_end = min(end_f, end_s)
            
            print(common_start, common_end)
            if common_start <= common_end: 
                ret.append([common_start, common_end])

                if end_f >= end_s:
                    idx_s += 1
                elif end_f < end_s:
                    idx_f += 1
            else:
                if end_f >= end_s:
                    idx_s += 1
                elif end_f < end_s:
                    idx_f += 1
        return ret

    def intervalIntersection_optmized(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Time complexity: probably O(n + m) given that we're iterating through both lists
        # Space complexity: Probably linear given that the size of return list can be at least the size of one of the other lists
        if (len(firstList) == 0) | (len(secondList) == 0): return [] 
        idx_f, idx_s = 0, 0
        ret = []
        m, n = len(firstList), len(secondList)
        tmp = [0,0]
        print(m, n)
        while (idx_f < m) & (idx_s < n):
            if (secondList[idx_s][0] <= firstList[idx_f][1])  & (firstList[idx_f][0] <= secondList[idx_s][1]):
                ret.append([max(firstList[idx_f][0], secondList[idx_s][0]), min(firstList[idx_f][1], secondList[idx_s][1])])
            
            if firstList[idx_f][1] > secondList[idx_s][1]:
                idx_s += 1
            else:
                idx_f += 1
        
        return ret

print(Solution().intervalIntersection_optmized([[3,10]], [[5,10]]))
