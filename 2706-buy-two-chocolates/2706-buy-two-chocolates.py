class Solution(object):
    def buyChoco(self, prices, money):
        prices = sorted(prices)
        if prices[0]+prices[1]>money:
            return money
        return money -(prices[0]+prices[1])