#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur1 = head
        newlist = ListNode(2**31)

        cur2 = newlist
        tmp = head.val
        while cur1 != None:
            if cur2.val == cur1.val:
                cur1 = cur1.next
            else:
                cur2.next = ListNode(cur1.val)
                cur2 = cur2.next
                cur1 = cur1.next
        # print(newlist)
        return newlist.next


# @lc code=end

    tests = [
        (makeListNode([1,1,2]), makeListNode([1,2])),
        (makeListNode([1,1,2,3,3]), makeListNode([1,2,3])),
        (makeListNode([]), makeListNode([]))
    ]