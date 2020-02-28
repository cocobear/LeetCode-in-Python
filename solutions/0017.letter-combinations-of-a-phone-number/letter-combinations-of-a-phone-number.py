#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from __future__ import annotations

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # BFS
        if len(digits) == 0: return []

        phoneMap = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8": "tuv", "9" : "wxyz"}

        ans = [x for x in phoneMap[digits[0]]]

        for digit in digits[1:]:
            ans = [ans[x]+y for y in phoneMap[digit] for x in range(len(ans))]
        return ans

    tests = [
        ('23', ["ad","bd","cd","ae","be","ce","af","bf","cf"]),
    ]
# @lc code=end

