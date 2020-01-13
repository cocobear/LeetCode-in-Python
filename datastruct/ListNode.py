class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        if isinstance(other, ListNode):
            m = self
            n = other
            while m and n:
                if m.val != n.val:
                    return False
                m = m.next
                n = n.next
        if m or n:
            return False
        return True

    def __str__(self):
        n = self
        s = ''
        while n:
            s += '->'
            s += str(n.val)
            n = n.next
        return s



def makeListNode(list_int):
    a = None
    cur = None
    for i in list_int:
        tmp = ListNode(int(i))
        tmp.next = None
        if not a:
            a = tmp
            cur = a
        else:
            cur.next = tmp
            cur = cur.next

    return a

