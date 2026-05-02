class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        bought_price = math.inf
        sold_price = 0
        max_profit = 0
        for price in prices:
            if price < bought_price:
                bought_price = price
            elif price > bought_price:
                sold_price = price
                max_profit = max(max_profit, sold_price - bought_price)

        return int(max_profit)
