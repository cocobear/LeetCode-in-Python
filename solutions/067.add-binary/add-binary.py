#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        ans = ''
        exp = 0
        while i >=0 or j >= 0:
            if i < 0:
                x = int(b[j]) + exp
            elif j < 0:
                x = int(a[i])  + exp
            else:
                x = int(a[i]) + int(b[j]) + exp


            rem = x % 2
            exp = x // 2
            ans += str(rem)
            i -= 1
            j -= 1
        if exp:
            ans += str(exp)
        return ans[::-1]

    tests = [
        ("1010", "1011", '10101'),
        ('11', '1', '100')
    ]





        
# @lc code=end

