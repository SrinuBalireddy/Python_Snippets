# class Solution(object):
#     def arrangeCoins(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         i = 2
        
        
#         while i <= n:
#             level = (i*(i+1))//2
#             if level == n:
#                 return i
#             elif level > n:
#                 return i-1
#             i += 1

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """        
        import math
        
        return int((-1 + math.sqrt(1+(8*n)) )//2)
        
"""

the number of coins in k step order 
1+2+3+....k

this is equal to (k(k+1))//2

so the equation we are solving is the largest possible value of k
such that (k*(k+1)//2) <= n

forming a quad equation - k2+k-2n=0

roots = (-1 (+/-) sqrt(1+8n))/2

as n is always a non negative number we can ignore the negative root

"""
            
        
        
        
            
        