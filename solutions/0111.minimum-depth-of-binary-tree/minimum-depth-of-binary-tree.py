#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        mindep = float('inf')
        def dfs(node, dep):
            if not node:
                return
            nonlocal mindep
            if node.left:
                dfs(node.left, dep +1)
            if node.right:
                dfs(node.right, dep +1)
            if not node.left and not node.right:
                mindep = min(mindep, dep)
        dfs(root, 1)

        return mindep
        
# @lc code=end

