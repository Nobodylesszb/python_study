"""
其实不能真正意义上的删除指定的Node，因为没有给与Previous Node。
我们真正删除的是指定Node的下一个Node，然后把指定Node的Value更改成下一个Node的值罢了。
为什么这个node.next.next在这里是没问题的，因为题目告诉了说指定的Node不为Tail，所以我们不用担心这个Edge Case。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self,node):
        node.val = node.next.val
        node.next = node.next.next

node1 = ListNode(3)
node2 = ListNode(4)
node3 = ListNode(5)
node1.next = node2
node2.next = node3


S = Solution()
print(S.deleteNode(node2))
