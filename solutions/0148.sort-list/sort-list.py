#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        fast , slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = ListNode(0)
        node = dummy
        while l and r:
            if l.val > r.val:
                node.next = r
                r = r.next
            else:
                node.next = l
                l = l.next
            node = node.next
        node.next = l or r
        return dummy.next

        
        
# @lc code=end

