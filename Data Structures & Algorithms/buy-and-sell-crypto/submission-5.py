class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minStock = prices[0]
        maxProf = 0

        for p in prices:
            prof = p - minStock
            if p < minStock:
                minStock = p
            
            maxProf = max(prof, maxProf)
        
        return maxProf