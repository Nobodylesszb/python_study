"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# class Solution(object):
#     def levelOrder(self, root):
#         q, ret = [root], []
#         while any(q):
#             ret.append([node.val for node in q])
#             q = [child for node in q for child in node.children if child]
#         return ret


#迭代
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:return []
        res = []
        stack = [root]
        while stack:
            temp = []
            next_stack = []
            for node in stack:
                temp.append(node.val)
                for child in node.children:
                    next_stack.append(child)
            stack = next_stack
            res.append(temp)
        return res