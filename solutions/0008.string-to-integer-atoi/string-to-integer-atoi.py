#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.lstrip()
        n = []
        if len(s) == 0:
            return 0

        if not s.startswith(('+','-')) and not s[0].isdigit():
            return 0
        for i in range(len(s)):
            if s[i].isdigit() or (s[i] == '-' and i == 0) or (s[i] == '+' and i == 0):
                n.append(s[i])
            else:
                break
        # print(n)
        try:
            x = int(''.join(n))
        except ValueError:
            return 0
        # if s[0] == '-':
        #     x = -x
        if x <= -(2**31):
            return -2**31
        elif x > (2**31 -1):
            return 2**31 -1
        else:
            return x

    tests = [
        ('42', 42),
        ('-42', -42),
        ('4193 with words', 4193),
        ('words and 987', 0),
        ('-91283472332', -2147483648),
        ('3.14159', 3),
        ('', 0),
        ('-', 0),
        ('+1', 1)

    ]    
# @lc code=end

