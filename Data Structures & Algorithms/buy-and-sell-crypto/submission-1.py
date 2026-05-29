class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxprof = 0
        currprof = 0
        minstock = prices[0]

        for num in prices:
            if num < minstock:
                minstock = num

            currprof = num - minstock

            if currprof > maxprof:
                maxprof = currprof
        
        return maxprof
            