#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start
class ListNode:
    def __init__(self, val, next_ = None):
        self.val = val
        self.next = next_

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.num = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.num: return -1
        node = self.head
        i = 0
        for _ in range(index):
            node = node.next
        return node.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head == None:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            newNode = ListNode(val)
            newNode.next = self.head
            self.head = newNode
        self.num += 1



    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.tail == None:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            node = ListNode(val)
            self.tail.next = node
            self.tail = node
        self.num += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == self.num:
            self.addAtTail(val)
        elif index > self.num:
            return
        else:
            node_insert = ListNode(val)
            node = self.head
            pre = None
            for i in range(index):
                pre = node
                node = node.next
            node_insert.next = node

            if pre != None:
                pre.next = node_insert
            else:
                self.head = node_insert
            self.num += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.num:
            return
        node = self.head
        pre = None
        for _ in range(index):
            pre = node
            node = node.next

        node = node.next

        if pre != None:
            pre.next = node
            if node == None:
                self.tail = pre
        elif node == None:
            self.head = None
            self.tail = None
        else:
            self.head = node

        self.num -= 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

