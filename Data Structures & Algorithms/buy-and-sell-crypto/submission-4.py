class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        best = 0
        prof = 0

        for p in prices:
            if p <= curMin:
                curMin = p
            
            prof = p - curMin
            
            best = max(best, prof)

        return best