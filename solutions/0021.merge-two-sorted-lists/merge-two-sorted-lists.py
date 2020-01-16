#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
from LeetCode_in_Python.datastruct.ListNode import ListNode
from LeetCode_in_Python.datastruct.ListNode import makeListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = ListNode(0)
        cur = newList
        cur1 = l1
        cur2 = l2
        while cur1 or cur2:
            tmp = ListNode(0)
            tmp.next = None

            if not cur1:
                tmp.val = cur2.val
                cur2 = cur2.next
            elif not cur2:
                tmp.val = cur1.val
                cur1 = cur1.next

            elif cur1.val < cur2.val:
                tmp.val = cur1.val
                cur1 = cur1.next

            else:
                tmp.val = cur2.val
                cur2 = cur2.next
            
            cur.next = tmp
            cur = cur.next

        return newList.next
        
# @lc code=end

    tests = [
            (makeListNode([1, 2, 4]), makeListNode([1, 3, 4]), makeListNode([1, 1, 2, 3, 4, 4])),

            ]