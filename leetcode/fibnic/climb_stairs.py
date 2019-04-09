class Solution():
    def ClimbStairs(self,n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.ClimbStairs(n-1)+self.ClimbStairs(n-2)