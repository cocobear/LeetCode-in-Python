#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

from __future__ import annotations
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isValid(board, row, col):
            n = len(board[0])
            # 检查列上是否有冲突
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # 检查右上角是否有冲突
            for i, j in zip(range(row-1,-1,-1), range(col+1, n)):
                if board[i][j] == 'Q':
                    return False
            # 检查左上角是否有冲突
            for i, j in zip(range(row-1,-1,-1), range(col-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            return True
        def backtrack(board, row):

            n = len(board)
            if row == n:
                # 这里需要复制整个数组
                temp = []
                for i in board:
                    temp.append("".join(i))
                ret.append(temp[:])
                return
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(board, row+1)
                board[row][col] = '.'

        # 不能使用这种方式创建，里面的list是引用，赋值时会同时进行 出现下面的现象
        # >>> board[0][0] = 'b'
        # >>> board
        # [['b', '.', '.', '.'], ['b', '.', '.', '.'], ['b', '.', '.', '.'], ['b', '.', '.', '.']]
        # board = [['.']*n]*n
        board = [["." for i in range(n)] for j in range(n)]
        ret = []
        backtrack(board, 0)
        return ret
    tests = [
        (4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])
    ]

# @lc code=end

