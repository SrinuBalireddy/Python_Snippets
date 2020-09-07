# Write your code here :-)

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        import math

        for i in range(1024):
            if n == math.pow(2,i):
                return True
        return False

obj= Solution()
print(obj.isPowerOfTwo(1025))


##########################
# other solution

def isPowerOfTwo(n):

    while n>1:
        n/=2
        print(n)

    return True if n == 1.0 else False

isPowerOfTwo(1025)

