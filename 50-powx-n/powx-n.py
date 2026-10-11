class Solution:
    def power(self, x:float, n: int) ->float:
        if n==1:
            return x
        if n==0:
            return 1
        return self.power(x*x, n//2) if n%2==0 else x*self.power(x*x, n//2)

    def myPow(self, x: float, n: int) -> float:
        if n<0:
            return 1/self.power(x,-n)
        return self.power(x,n)