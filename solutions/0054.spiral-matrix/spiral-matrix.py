#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

from __future__ import annotations
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x = 0
        y = 0
        i = 0
        direction = 'R'
        visited = {}
        ans = []
        m = len(matrix)
        if m <= 0: return []
        n = len(matrix[0])
        while i <= m*n:
            ans.append(matrix[x][y])
            visited[(x,y)] = True
            print('x:%d, y:%d, visited:%s'%(x,y, str(visited)))
            i += 1
            if i == m*n:
                return ans
            if direction == 'R':
                y += 1
                # 超出边界
                # 已访问过
                if y >= n or (x,y) in visited:
                    y -= 1
                    x += 1
                    direction = 'D'
            elif direction == 'D':
                x += 1
                if x >= m or (x,y) in visited:
                    x -= 1
                    y -= 1
                    direction = 'L'
            elif direction == 'L':
                y -= 1
                if y < 0 or (x,y) in visited:
                    y += 1
                    x -= 1
                    direction = 'U'
            elif direction == 'U':
                x -= 1
                if x < 0 or (x,y) in visited:
                    x += 1
                    y += 1
                    direction = 'R'


    tests = [
        ([
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
            ], [1,2,3,6,9,8,7,4,5])
    ]
# @lc code=end

