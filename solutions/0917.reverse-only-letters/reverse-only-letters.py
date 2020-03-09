#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        i = 0
        j = len(S) - 1
        while i < j:
            if not S[i].isalpha():
                i += 1
            elif not S[j].isalpha():
                j -= 1
            else:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1

        return ''.join(S)
# @lc code=end

