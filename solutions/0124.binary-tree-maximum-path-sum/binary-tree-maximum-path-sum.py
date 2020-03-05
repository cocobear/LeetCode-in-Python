#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ret = float('-inf')
        def findmax(node):
            if not node: return 0
            left = findmax(node.left)
            right = findmax(node.right)
            cur = max(node.val, node.val + max(left, right))

            self.ret = max(self.ret , cur, node.val + left + right)
            return cur
        findmax(root)
        return self.ret


# @lc code=end

