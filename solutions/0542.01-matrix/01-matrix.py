#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

from __future__ import annotations
# @lc code=start
from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        row = len(matrix)
        col = len(matrix[0])
        ret = [[-1 for i in range(col)] for _ in range(row)]
        q = deque()
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    ret[i][j] = 0
                    q.appendleft((i,j))

        print(ret)
        while q:
            tmp_i, tmp_j = q.popleft()
            for next_i,next_j in ((tmp_i-1,tmp_j), (tmp_i+1, tmp_j), (tmp_i, tmp_j-1), (tmp_i, tmp_j+1)):
                if 0 <= next_i < row and 0 <= next_j < col and ret[next_i][next_j] < 0:
                    ret[next_i][next_j] = ret[tmp_i][tmp_j] + 1
                    q.append((next_i, next_j))


        return ret

    tests = [
        ([[0,0,0],[0,1,0],[0,0,0]], [[0,0,0],[0,1,0],[0,0,0]]),
    ]
# @lc code=end

