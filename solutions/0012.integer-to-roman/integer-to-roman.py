#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        roman_ano = [
                    ('I','V'),
                    ('X','L'),
                    ('C','D'),
                    ('M','Z')
        ]
        i = len(str(num)) - 1
        if num > 1000:
            x = num // 1000
            roman += 'M'*x
            num %= 1000

        # print('now: {} {} i = {}'.format(num, roman, i))

        while i >= 0:
            if num >= 9*10**i:
                roman += roman_ano[i][0]
                roman += roman_ano[i+1][0]
            elif num >= 5*10**i:
                x = num // 10**i
                roman += roman_ano[i][1]
                roman += roman_ano[i][0]*(x-5)
            elif num >= 4*10**i:
                roman += roman_ano[i][0]
                roman += roman_ano[i][1]
            elif num >= 1*10**i:
                x = num // 10**i
                roman += roman_ano[i][0]*x
            num %= 10**i
            i -= 1

            # print('now: {} {}'.format(num, roman))
        return roman

    tests = [
        (3, 'III'),
        (4, 'IV'),
        (9, 'IX'),
        (58, 'LVIII'),
        (1994, 'MCMXCIV'),
    ]
# @lc code=end

