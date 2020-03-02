#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root: return None
        ret = []
        def dfs(node, path):
            nonlocal target
            if not node.left and not node.right and ((node.val + sum(path)) == target):
                path.append(node.val)
                ret.append(path[:])
                return
            if node.left:
                dfs(node.left, path+[node.val])
            if node.right:
                dfs(node.right, path+[node.val])
            
        dfs(root, [])
        return ret
        
# @lc code=end

