#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        ret = [0]
        def helper(node):
            if not node: return 0

            l = helper(node.left)
            r = helper(node.right)
            ret[0] += abs(node.val + l + r - 1)
            return node.val + l + r - 1

        helper(root)
        return ret[0]
        
# @lc code=end

