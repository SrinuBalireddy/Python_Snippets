# Write your code here :-)
"""
Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the
unsigned integer 43261596,
so return 964176192 which its binary representation is 00111001011110000010100101000000.
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        new_val = format(n,'032b')[::-1]  # format will change the number to binary
                                          # '032b' is to get a 32bit binary value (other values are '016b')
        return int(new_val,2)         # this is convert binary to int

#s = Solution()
#print(s.reverseBits('00000010100101000001111010011100'))



# leetcode solution


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

