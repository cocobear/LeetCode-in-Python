#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeaf(root):
            ret = []
            def dfs(node):
                if not node: return False
                if not node.left and not node.right:
                    ret.append(node.val)
                dfs(node.left)
                dfs(node.right)
            dfs(root)
            return ret
        a = getLeaf(root1)
        b = getLeaf(root2)
        return a == b
        
# @lc code=end

