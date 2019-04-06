"""
找到链表的中间的元素
利用两个指针，一个走一步。另一个走两步，当两步走到尾，另一个就到达中间
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head


node1 = ListNode(3)
node2 = ListNode(4)
node3 = ListNode(5)
node1.next = node2
node2.next = node3


S = Solution()
print(S.middleNode(node1))


        