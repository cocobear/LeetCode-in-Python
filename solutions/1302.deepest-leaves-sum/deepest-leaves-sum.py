#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [(root, 0)]
        total = 0
        maxdep = -1
        while queue:
            node, dep = queue.pop(0)
            if dep > maxdep:
                total = node.val
                maxdep = dep
            elif dep == maxdep:
                total += node.val

            if node.left:
                queue.append((node.left, dep+1))
            if node.right:
                queue.append((node.right, dep +1))

        return total
        
# @lc code=end

