
"""
for a N-ary Tree, instead of comparing depth between only left and right child nodes, 
we simply iterate all child nodes by (self.maxDepth(node) 
for node in root.children) 
and return the max_depth on the current node by the fucntion max(child1, child2, ...).
 Eventually we will get the maximum depth for the root.
"""
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        if not root.children: return 1
        return max(self.maxDepth(node) for node in root.children) + 1