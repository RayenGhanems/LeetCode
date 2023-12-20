class Solution(object):
    def buyChoco(self, prices, money):
        one = prices[0] 
        two = prices[1]

        for i in prices[2:]:
            if i < one or i < two:
                if one>two:
                    one=i
                else:
                    two =i

        return money if (one + two) > money else money - (one + two)

