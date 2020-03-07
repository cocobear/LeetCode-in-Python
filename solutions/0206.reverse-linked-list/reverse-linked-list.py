#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        if not head: return head
        q = []
        while head:
            q.insert(0, head.val)
            head = head.next

        newNode = ListNode(q[0])
        n = newNode
        for i in q[1:]:
            newNode.next = ListNode(i)
            newNode = newNode.next

        return n
    
    def reverseListIter(self, head: ListNode) -> ListNode:
        # 
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur

        return pre

    def reverseList(self, head: ListNode) -> ListNode:
        def helper(node, pre=None):
            if not node: return pre
            n = node.next
            node.next = pre
            return helper(n, node)

        return helper(head)





        
# @lc code=end

