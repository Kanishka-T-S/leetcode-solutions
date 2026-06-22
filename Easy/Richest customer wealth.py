class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max=0
        for i in accounts:
            wealth=sum(i)
            if wealth>max:
                max=wealth
        return max