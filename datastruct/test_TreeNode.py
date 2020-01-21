
import LeetCode_in_Python.datastruct
from LeetCode_in_Python.datastruct.ListNode import makeListNode
from LeetCode_in_Python.datastruct.TreeNode import TreeNode


def test_str():
    assert str(TreeNode.constructTree([2, 3, 4])) == \
"""
    4
2
    3"""

