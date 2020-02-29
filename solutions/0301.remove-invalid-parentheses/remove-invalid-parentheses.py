#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 暴力解法 
        # 找出删除各种字符的所有组合，并一一判断是否有效
        # 容易超时
        def isValid(s):
            count = 0
            for i in s:
                if i == '(':
                    count += 1
                elif i == ')':
                    count -= 1
                    if count < 0: return False
            return count == 0
        level = {s}
        while True:
            valid = list(filter(isValid, level))
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}
# @lc code=end

