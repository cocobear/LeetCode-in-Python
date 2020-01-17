#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t = 0
        n = len(s)

        for i in range(n-1, -1, -1):
            if s[i] != ' ':
                t += 1
            elif t == 0:
                continue
            else:
                break
        return t

    tests = [
        ('hello world', 5),
        ('hi', 2),
        (' a', 1),
        ('', 0),
        (' ', 0),
        ('a ', 1),
    ]
# @lc code=end

