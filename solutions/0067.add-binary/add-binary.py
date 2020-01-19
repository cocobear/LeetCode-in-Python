#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a)
        n = len(b)
        i = m - 1
        j = n - 1
        extra = 0
        res = ''
        while i >=0 or j >= 0:
            if i < 0:
                x = int(b[j]) + extra
            elif j < 0:
                x = int(a[i]) + extra
            else:
                x = int(a[i]) + int(b[j]) + extra
            extra = x // 2
            res = str(x%2) + res
            i -= 1
            j -= 1
        if extra:
            return str(extra) + res
        else:
            return res

    tests = [
        ('11', '1', '100'),
        ('1010', '1011', '10101')
    ]
# @lc code=end

