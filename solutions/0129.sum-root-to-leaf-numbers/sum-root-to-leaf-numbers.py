#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        nums = []
        def dfs(node, path):
            if node:
                if not node.left and not node.right:
                    path = path + [node.val]
                    nums.append(path[:])
                else:
                    dfs(node.left, path+[node.val])
                    dfs(node.right, path+[node.val])

            
        dfs(root, [])
        
        ret = 0
        for n in nums:
            for idx, x in enumerate(n[::-1]):
                # print(idx,x)
                ret = ret + x*10**idx
                                      
        return ret
        
# @lc code=end

