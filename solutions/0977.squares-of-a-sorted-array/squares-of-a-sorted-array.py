#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ret = []
        i = 0
        j = len(A) - 1

        while i <= j:
            if A[i]**2 > A[j]**2:
                ret.append(A[i]**2)
                i += 1
            else:
                ret.append(A[j]**2)
                j -= 1
        return ret[::-1]
# @lc code=end

