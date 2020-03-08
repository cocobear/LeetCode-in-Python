#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     if not lists: return
    #     n = len(lists)
    #     if n == 1:
    #         return lists[0]

    #     def merge(a, b):
    #         c = ListNode(0)
    #         node = c
    #         while a or b:
    #             if not a:
    #                 node.next = b
    #                 b = b.next
    #             elif not b:
    #                 node.next = a
    #                 a = a.next
    #             elif a.val > b.val:
    #                 node.next = b
    #                 b = b.next
    #             elif a.val <= b.val:
    #                 node.next = a
    #                 a = a.next
    #             node = node.next
    #         return c.next
    #     mid = n // 2
    #     left = lists[0:mid]
    #     right = lists[mid:]
    #     l = self.mergeKLists(left)
    #     r = self.mergeKLists(right)
    #     return merge(l, r)
    def mergeKLists(self, lists):
        if not lists:
            return 
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = cur = ListNode(0)
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next

        
# @lc code=end

