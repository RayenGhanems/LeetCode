class Solution(object):
    def buyChoco(self, prices, money):
        one = prices[0] 
        two = prices[1]

        for i in prices[2:]:
            if i < max(one,two):
                if one>two:
                    one=i
                else:
                    two =i

        result = money if (one + two) > money else money - (one + two)
        return result

