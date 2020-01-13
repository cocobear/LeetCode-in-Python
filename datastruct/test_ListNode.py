
import LeetCode_in_Python.datastruct
from LeetCode_in_Python.datastruct.ListNode import makeListNode

def test_make_eq():
    assert makeListNode([2]) != makeListNode([3])

    assert makeListNode([2, 4, 3]) == makeListNode([2,4,3])
    assert makeListNode([2, 4, 3]) != makeListNode([2,4,3, 4 ])
    assert makeListNode([1, 4, 3]) != makeListNode([2,4,3, 4 ])

def test_str():
    assert str(makeListNode([2, 4, 3])) == '->2->4->3'

