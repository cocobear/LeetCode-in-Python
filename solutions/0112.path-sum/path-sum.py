#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        ret = False
        def dfs(node, cursum):
            nonlocal ret
            if not node.left and not node.right and ((cursum+node.val) == sum):
                ret = True
            if node.left:
                dfs(node.left, cursum + node.val)
            if node.right:
                dfs(node.right, cursum + node.val)

        dfs(root, 0)
        return ret
        
# @lc code=end

