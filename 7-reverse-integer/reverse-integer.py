class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x = abs(x)
        result = 0
        while x!=0:
            result = (x%10) + (result*10)
            x //= 10

        result *= sign
        
        return result if result > -2**31 and result < 2**31 else 0
        