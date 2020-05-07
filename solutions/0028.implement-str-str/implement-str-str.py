#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr_1(self, haystack: str, needle: str) -> int:
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

    def strStr_2(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1

        i = 0
        j = 0
        m = len(haystack)
        n = len(needle)
        find = False
        last = 0
        x = 0
        while i < m and j < n:
            x = x + 1
            print('i:%d j:%d'%(i,j))
            if haystack[i] != needle[j]:
                if find:
                    i = max(0, i - j + 1)
                else:
                    i += 1
                j = 0
                find = False
            else:
                find = True
                i += 1
                j += 1

        if j == n and find:
            return i - n
        else:
            return -1

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1

        m = len(haystack)
        n = len(needle)
        i = 0
        while i < m:
            if haystack[i:i+n] == needle:
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

