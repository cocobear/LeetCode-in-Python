#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from __future__ import annotations
from collections import deque

# @lc code=start
class Solution:
    # def exist_1(self, board: List[List[str]], word: str) -> bool:
    #     if not board:
    #         return False
    #     if not word:
    #         return False

    #     cur_word_pos = deque()

    #     moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #     m = len(board)
    #     n = len(board[0])

    #     # 向四个方向分别查找指定的字符
    #     # 返回四个方向所有符合的坐标
    #     def find_char(pos, char):
    #         rets = []
    #         for move in moves:
    #             new_pos = (pos[0] + move[0], pos[1]+move[1])
    #             # print('try find char:[%s] at pos: %s'%(char, str(new_pos)))
    #             if 0 <= new_pos[0] <m and 0<= new_pos[1] <n:
    #                 if board[new_pos[0]][new_pos[1]] == char:
    #                     rets.append(new_pos)
    #             else:
    #                 continue
    #         return rets

    #     def find_word(pos, word):
    #         if not word:
    #             return True
    #         # print('find [%s] at %s'%(word, str(pos)))
    #         # 不能回退查找
    #         rets = find_char(pos, word[0])
    #         # print('find [%s] at %s cur_word_pos is:%s'%(word, str(rets), str(cur_word_pos)))
    #         for new_pos in rets:
    #             if new_pos in cur_word_pos:
    #                 continue
    #             cur_word_pos.append(new_pos)
    #             if len(word) == 1:
    #                 return True
    #             else:
    #                 if find_word(new_pos, word[1:]):
    #                     return True
    #                 else:
    #                     cur_word_pos.pop()
    #                     continue
    #         else:
    #             return False

    #     for i in range(m):
    #         for j in range(n):
    #             cur_word_pos.clear()
    #             cur_word_pos.append((i,j))
    #             if board[i][j] == word[0]  and find_word((i,j), word[1:]):
    #                 return True
    #     return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        if not word:
            return False

        m = len(board)
        n = len(board[0])


        def dfs(i, j, x):
            if x == len(word):
                return True
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[x]:
                v = board[i][j]
                board[i][j] = '#'
                if dfs(i-1,j, x+1) or dfs(i+1,j,x+1) or dfs(i,j-1,x+1) or dfs(i,j+1,x+1):
                    return True
                board[i][j] = v
            else:
                return False



        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


    tests = [
        ([["a","a"]], 'aaa', False),
        ([['a']], 'a', True),
            ([
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ], "ABCCED", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False),
    ]

if __name__ == "__main__":
    s = Solution()
    print(s.exist([
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ], 'ABCCED'))
# @lc code=end

