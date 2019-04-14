"""
判断一个tree节点数据是否都一样
"""
class Solution:
 def isUnivalTree(self, root):
        def dfs(node):
            return not node or node.val == root.val and dfs(node.left) and dfs(node.right)
        return dfs(root)


class Solution2:
    def isUnivalTree(self, root):
        if not root:
            return True
        
        if root.right:
            if root.val != root.right.val: #Equavalent
                return False
            
        if root.left:
            if root.val != root.left.val: #Equavalent
                return False
        
        return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)