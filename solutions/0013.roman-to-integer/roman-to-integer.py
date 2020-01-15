#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_ano = [
                    ('I','V'),
                    ('X','L'),
                    ('C','D'),
                    ('M','Z')
        ]
        n = len(s)
        num = 0
        x = 0
        i = 0
        while i < n:
            for j in range(3, -1, -1):
                x = 0
                # print('------------------i, j',i,j,num)
                if i == n:
                    break
                if roman_ano[j][0] == s[i] and ((j+1) <4) and  ((i+1) <n) and roman_ano[j+1][0] == s[i+1]:
                    num += 9*10**j
                    i += 2
                elif roman_ano[j][0] == s[i] and  ((i+1) <n) and roman_ano[j][1] == s[i+1]:
                    num+= 4*10**j
                    i += 2
                elif roman_ano[j][1] == s[i]:
                    # print('50',roman_ano[j][1])
                    i += 1
                    while i < n and  s[i] == roman_ano[j][0]:
                        i += 1
                        x += 1 
                    num += (5+x)*10**j
                elif roman_ano[j][0] == s[i]:
                    # print('个位',i)
                    while i < n and s[i] == roman_ano[j][0]:
                        i += 1
                        x += 1
                    # print('x=',x)
                    num += x*10**j
        return num
    tests = [
        ('III', 3),
        ('IV', 4),
        ('IX', 9),
        ('LVIII', 58),
        ('MCMXCIV', 1994),
        ('DCXXI', 621),
        ('MDLXX', 1570)

    ]
# @lc code=end

