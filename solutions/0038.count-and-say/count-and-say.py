#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            s = self.countAndSay(n-1)
            m = len(s)
            tmp = ''
            j = 0
            i = 0
            while i < m:
                j = 1
                while (i+j) < m and s[i] == s[i+j]:
                    j += 1
                tmp += str(j)
                tmp += s[i]
                i += j
            return tmp

    tests = [
        (1, '1'),
        (4, '1211'),
        (5, '111221'),
    ]
# @lc code=end
