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
    def mergeTwoListsFirst(self, l1: ListNode, l2: ListNode) -> ListNode:
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

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        first = l1
        second = l2
        head = l3
        cur = head
        tmp_val = None
        while first and second:
            
            if first.val < second.val:
                tmp_val = first.val
                first = first.next
            else:
                tmp_val = second.val
                second = second.next
            tmp = ListNode(tmp_val)
            cur.next = tmp
            cur = cur.next

        # 两个链表如果长度不一样，则剩下一个
        if first:
            cur.next = first
        if second:
            cur.next = second
        return head.next
# @lc code=end

    tests = [
            (makeListNode([1, 2, 4]), makeListNode([1, 3, 4]), makeListNode([1, 1, 2, 3, 4, 4])),

            ]