#
# @lc app=leetcode id=831 lang=python3
#
# [831] Masking Personal Information
#

# @lc code=start
class Solution:

    def maskPII(self, S: str) -> str:
        def maskEmail(name):
            res = ''
            name = name.lower()
            res = name[0] + '*'*5 + name[-1]
            return res
        def maskPhone(s):
            s = ''.join([x for x in s if x.isalnum()])
            n = len(s)
            pre_n = n - 10
            res = ''
            if pre_n:
                res = '+' + '*'*pre_n + '-'
            res += '***-***-'
            res += s[-4:]
            return res


        try:
            name, company = S.split('@')
        except ValueError:
            return maskPhone(S)
        name = maskEmail(name)
        return name + '@' + company.lower()
    
    tests = [
        ("LeetCode@LeetCode.com", "l*****e@leetcode.com"),
        ("AB@qq.com", "a*****b@qq.com"),
        ("JackAndJill@Gmail.Com", "j*****l@gmail.com"),
        ("1(234)567-890", "***-***-7890"),
        ("86-(10)12345678", "+**-***-***-5678"),
        ("+(501321)-50-23431", "+***-***-***-3431")
    ]
# @lc code=end

