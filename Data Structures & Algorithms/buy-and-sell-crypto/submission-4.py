class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxprof = 0
        prof = 0 

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                maxprof = prices[j] - prices[i]
                prof = max(maxprof, prof)
        return prof



        

            