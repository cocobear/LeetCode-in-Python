#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from __future__ import annotations
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def dfs(i, j, k, visited):
            if k == len(word):
                return True
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and \
                    (tmp_i, tmp_j) not in visited and \
                        board[tmp_i][tmp_j] == word[k]:
                    visited.add((tmp_i, tmp_j))
                    if dfs(tmp_i, tmp_j, k+1, visited):
                        return True
                    visited.remove((tmp_i, tmp_j))
            return False
                    
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and dfs(i, j, 1, {(i, j)}):
                    return True
        return False

    tests = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED', True)
    ]
# @lc code=end

