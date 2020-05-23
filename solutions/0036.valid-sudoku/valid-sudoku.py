#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_repeat(row):
            row = [x for x in row if x != '.']
            return len(set(row)) != len(row)

        for row in board:
            if is_repeat(row):
                return False
        
        for col in zip(*board):
            if is_repeat(col):
                return False
        
        for i in range(3):
            for j in range(3):
                row = [board[x][y] for x in range(3*i, 3*(i+1)) for y in range(3*j, 3*(j+1))]
                if is_repeat(row):
                    return False
        return True

        
# @lc code=end

