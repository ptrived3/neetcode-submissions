class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currmin = prices[0]
        maxprofit = 0
        currprofit = 0

        for i in range(1, len(prices)):
            currprofit = prices[i] - currmin
            if prices[i] < currmin:
                currmin = prices[i]
                # currmax = prices[i]
                
            if currprofit > maxprofit:
                maxprofit = currprofit

            
        return maxprofit