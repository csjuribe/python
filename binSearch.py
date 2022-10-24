class Solution(object):    
    def mySqrt(self, num):
        """
        :type x: int
        :rtype: int
        """       
        lower = 0
        upper = num
        
        while lower <= upper:
            mid = (lower + upper) //2
            sqr = mid * mid
            if sqr == num or ( sqr < num and (mid + 1) * (mid + 1) > num):
                return mid
            elif sqr > num :
                upper = mid - 1
            else:
                lower = mid + 1
