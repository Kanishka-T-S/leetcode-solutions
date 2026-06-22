class Solution:
    def isPalindrome(self, x: int) -> bool:
        t=x
        r=0
        while t>0:
            d=t%10
            r=r*10+d
            t=t//10
        return x==r
        