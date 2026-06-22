class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        maxs=0
        for num in nums:
            if num == 1:
                c+=1
                maxs= max(maxs,c)
            else:
                c=0
        return maxs   