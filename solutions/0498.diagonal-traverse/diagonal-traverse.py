#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
from __future__ import annotations
# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        ans = []
        m = len(matrix)
        n = len(matrix[0])
        x, y = 0, 0
        direction = 'UP'
        i = 0
        while x < m and y < n:
            # if i > 10: break
            # i += 1
            ans.append(matrix[x][y]) 
            # 先向右上
            print('DIR:%s, %s, x:%s, y:%s'%(matrix[x][y], str(direction), str(x), str(y)))
            if direction == 'UP':
                x -= 1
                y += 1
                if x < 0 and y < n:
                    x = 0
                    direction = 'DOWN'
                elif y == n:
                    x += 2
                    y -= 1
                    direction = 'DOWN'
            else:
                x += 1
                y -= 1
                if y < 0 and x < m:
                    y = 0
                    direction = 'UP'
                elif x == m:
                    y += 2
                    x -= 1
                    direction = 'UP'                 

        return ans
    tests = [
        ([
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ], [1,2,4,7,5,3,6,8,9])
    ]

# @lc code=end

