#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

from __future__ import annotations
# @lc code=start
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S: return None

        ret = []

        def dfs(char, path):
            if len(path) == len(S):
                ret.append(path)
                return
            for i in range(len(char)):
                if char[i].isalpha():
                    dfs(char[i+1:], path+char[i].lower())
                    dfs(char[i+1:], path+char[i].upper())
                else:
                    dfs(char[i+1:], path+char[i])
        dfs(S, '')
        ret.sort()
        ret.reverse()
        return ret

    tests = [
        ('a1b2', ["a1b2", "a1B2", "A1b2", "A1B2"]),
    ]
# @lc code=end

