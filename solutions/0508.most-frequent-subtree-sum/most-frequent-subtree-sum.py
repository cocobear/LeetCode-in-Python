#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root: return

        ret = {}
        def dfs(node):
            if not node: return 0
            s = node.val + dfs(node.left) + dfs(node.right)

            ret[s] = ret.get(s, 0) + 1
            return s

        dfs(root)
        max_n = max(ret.values())
        return [x for x in ret.keys() if ret[x] == max_n]

# @lc code=end

