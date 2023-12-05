this should be easy since eventually all the teams should play with all the teams and since the number of teams is decreasing by 2 each time is even but also incleasing by one each time odd then  the total number of maches should be equal to n-1

# Another Method
an easier method would be this function :
class Solution(object):
  def numberOfMatches(self, n):
    out =0
    while n>1:
      if n%2==0:
        out+=n/2
        n=n/2
      else:
        out +=(n+1)/2
        n=(n-1)/2
    return out


    now this another way to approach this test which is simpler to think of and execute but ofcorse it takes O(n) time and O(1) space
