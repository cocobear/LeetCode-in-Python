#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = ''
        m = len(num1)
        n = len(num2)
        if num1 == '0' or num2 == '0':
            return '0'
        # 1位乘2位结果最大可能是3位
        res_list = [0]*(m*n + 1)
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(m):
            for j in range(n):
                x = int(num1[i]) * int(num2[j])
                if x >= 10:
                    res_list[i+j+1] += x//10
                    res_list[i+j] += x%10

                else:
                    res_list[i+j] += x
                # 处理再一次进位
                v = res_list[i+j]
                if v >= 10:
                    res_list[i+j+1] += v//10
                    res_list[i+j] = v%10
                # print(res_list)
        # print(res_list)
        ans = ''.join([str(i) for i in res_list[::-1]]).lstrip('0')
        return ans




    tests = [
        ('9', '9', '81'),
        ('0', '21', '0'),
        ('33', '55', '1815'),
        ('123', '456', '56088'),
    ]

# @lc code=end

