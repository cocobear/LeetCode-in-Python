#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = n2 = 0
        while l1:
            n1 *= 10
            n1 += l1.val
            l1 = l1.next
        while l2:
            n2 *= 10
            n2 += l2.val
            l2 = l2.next
        n3 = n1 + n2

        head = ListNode(0)
        if n3 == 0: return head

        while n3:
            x = n3 % 10
            n3 = n3 // 10
            head.next, head.next.next = ListNode(x), head.next

            

        return head.next


# @lc code=end

