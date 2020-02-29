#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return None
        ret = []
        i = 0
        def dfs(i, path):
            ret.append(path)
            while i < len(nums):
                dfs(i+1, path + [nums[i]])
                i += 1
        dfs(i, [])
        return ret
# @lc code=end

