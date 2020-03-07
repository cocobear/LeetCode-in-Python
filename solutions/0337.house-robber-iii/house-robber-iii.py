#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node: return 0, 0
            rub_left, not_rub_left = dfs(node.left)
            rub_right, not_rub_right = dfs(node.right)

            # 不抢本店
            not_rub = max(rub_left, not_rub_left) + max(rub_right, not_rub_right)

            rub = node.val + not_rub_left + not_rub_right
            return rub, not_rub

        return max(dfs(root))



# @lc code=end

