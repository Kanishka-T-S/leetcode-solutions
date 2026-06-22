class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        k=(n*(n+1))//2
        c=sum(nums)
        return k-c