#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        i = 0
        if m == 0:
            return 0
        while i < n:
            j = 0
            if i > (n-m):
                return -1
            while j < m:
                if haystack[i+j] != needle[j]:
                    break
                j += 1
            if j == m:
                return i
            else:
                i += 1
        return -1

    tests = [
        ('hello', 'll', 2),
        ('aaaaa', 'bba', -1),
        ('hell', '', 0),
        ('aaa', 'aaaa', -1),
    ]
# @lc code=end

