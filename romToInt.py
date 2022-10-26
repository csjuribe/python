class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        count = 0
        prev = 0
        
        for i in s:
            num = 0
            if i == 'I':
                num = 1
            elif i == 'V':
                num =  5
            elif i == 'X':
                num = 10
            elif i == 'L':
                num = 50
            elif i == 'C':
                num = 100
            elif i == 'D':
                num = 500
            elif i == 'M':
                num = 1000
            else:
                num = 0
                
            if ( num > prev):
                total = total + num - (2 * prev)
            else:
                total = total + num
            prev = num
            
        return total
