#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) - 1
        if b == -1: return True

        while a < b:
            if not s[a].isalpha() and not s[a].isnumeric():
                a += 1
                continue
            if not s[b].isalpha() and not s[b].isnumeric():
                b -= 1
                continue
            if s[a].upper() == s[b].upper():
                a += 1
                b -= 1
                continue
            else:
                return False

        return True

# @lc code=end

