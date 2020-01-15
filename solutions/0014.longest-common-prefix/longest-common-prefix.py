#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from __future__ import annotations

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        i = 0
        j = 0
        x = 0
        running = True
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        while i < len(strs[0]) and running:
            finish = False
            x = 0
            try:
                tmp = ''.join([x[i] for x in strs ])
            except IndexError:
                break
                
            if tmp.replace(tmp[0],'') == '':
                i +=1
            else:
                break
        prefix = strs[0][:i]

        return prefix

    tests = [
        (["flower","flow","flight"], 'fl'),
        (["dog","racecar","car"], ''),
        ([], ''),
        ([''], ''),
        (['a'], 'a'),
        (['c','c'], 'c'),
        (['aa','ab'], 'a'),
        (['aa', 'a'], 'a')
    ]
# @lc code=end

