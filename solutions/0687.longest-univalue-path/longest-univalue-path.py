#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def helper(node):
            if not node: return 0
            a = helper(node.left)
            b = helper(node.right)
            n = 0
            left = 0
            right = 0
            if node.left and node.val == node.left.val:
                left = a
            if node.right and node.val == node.right.val:
                right = b
            n = max(left, right)
            self.ret = max(self.ret, left+right)
            return n + 1
        self.ret = 0
        helper(root)

        return self.ret
# @lc code=end

