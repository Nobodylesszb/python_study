"""
创建第三个链表，依次比较L1,l2的值
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self,l1,l2):
        """
        :type l1:listnode
        :type l2:listnode
        :rtype:listnode
        """
        dummy = cur = ListNode(0)
        while l1 and l2 :
            if l1.val <l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
