#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from __future__ import annotations
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1],[1,1]]
        pre = [1, 1]
        if numRows <= 2:
            return ans[:numRows]
        for _ in range(2, numRows):
            i = 0
            j = 1
            new_row = [pre[0]]
            while j < len(pre):
                new_row.append(pre[i]+pre[j])
                i += 1
                j += 1
            new_row += [pre[-1]]
            # print(new_row)
            ans.append(new_row)
            pre = new_row
        return ans

    
    tests = [
        (5, [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]),
        (1, [[1]]),
        (2, [[1],[1,1]])
    ]
        
# @lc code=end

