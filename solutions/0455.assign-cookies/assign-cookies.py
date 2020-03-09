#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        ret = 0
        j = 0
        i = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                ret += 1
            else:
                j += 1
        return ret

# @lc code=end

