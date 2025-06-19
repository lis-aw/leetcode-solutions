class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = float('inf')
        for num in prices:
            if num < minprice:
                minprice=num
            if num-minprice>maxprofit:
                maxprofit = num-minprice
        return maxprofit



        