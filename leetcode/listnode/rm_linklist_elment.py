"""
Before writing any code, 
it's good to make a list of edge cases that we need to consider. 
This is so that we can be certain that 
we're not overlooking anything while coming up with our algorithm, 
and that we're testing all special cases when we're ready to test.
 These are the edge cases that I came up with.

1.The linked list is empty, i.e. the head node is None.
2.Multiple nodes with the target value in a row.
3.The head node has the target value.
4.The head node, and any number of nodes immediately after it have the target value.
5.All of the nodes have the target value.
6.The last node has the target value.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy_head = ListNode(-1)
        dummy_head.next = head
        cur_node = dummy_head
        while cur_node.next != None:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return dummy_head.next
            
            