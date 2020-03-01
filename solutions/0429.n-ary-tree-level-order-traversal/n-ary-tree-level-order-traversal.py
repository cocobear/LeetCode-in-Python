#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ret = []
        def bfs(node, level):
            if node:
                if len(ret) <= level:
                    ret.append([])
                ret[level].append(node.val)
                for child in node.children:
                    bfs(child, level+1)

        bfs(root, 0)

        return ret

        
# @lc code=end

