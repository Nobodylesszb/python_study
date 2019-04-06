"""
in Python, every value is a reference, you can say a pointer, 
to an object. Objects cannot be values. 
Assignment always copies the value; 
two such pointers point to the same object
if you operate with head directly, 
you will lost the pointer point at the head after running the while loop.
Therefore, we set another pointer cur = head 
and we can return the left linked list with pointer head, 
which hasn't been changed during the while loop. Hope that helps.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
     def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next # del the dup
            else:
                cur = cur.next
        return head

        
        