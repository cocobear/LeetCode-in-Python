#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return None
        ret = []
        def dfs(node, level):
            if len(ret) <= level:
                ret.append([node.val])
            else:
                ret[level].append(node.val)
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
        dfs(root, 0)
        return ret

# @lc code=end

