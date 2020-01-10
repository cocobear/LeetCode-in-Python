#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numToList(self, num):
        a = None
        cur = None
        for i in str(num)[::-1]:
            tmp = ListNode(int(i))
            tmp.next = None
            if not a:
                a = tmp
                cur = a
            else:
                cur.next = tmp
                cur = cur.next
        return a  

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        m = 0       
        for tmp in [l1,l2]:
            i = 0
            while True:
                #print(tmp.val)
                m = m + tmp.val*(10**i)
                if tmp.next:
                    i += 1
                    tmp = tmp.next
                else:
                    break
        #print(m)
        #print(self.numToList(m))
        return self.numToList(m)


        

# @lc code=end

