"""
给一个数字，搜索树中以数字为根的子树
"""

#遍历
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        trav = root
        while trav:
            if trav.val == val:
                return trav
            elif trav.val < val:
                trav = trav.right
            else:
                trav = trav.left

#迭代
class Solution2:
    def searchBST(self, root, val):
        if root and val < root.val: return self.searchBST(root.left, val)
        elif root and val > root.val: return self.searchBST(root.right, val)
        return root