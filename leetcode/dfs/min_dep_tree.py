"""
关于dfs,bfs的解释
https://zhuanlan.zhihu.com/p/50187643
"""
class Solution:
    def minDepth(self,root):
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        return 1 + r + 1 if l == 0 or r == 0 else min(l,r)+1