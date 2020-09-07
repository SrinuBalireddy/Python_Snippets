# Write your code here :-)
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # easy one liner

        return s in (s*2)[1:-1]

s = Solution()
print(s.repeatedSubstringPattern('ababa'))

# other solution

class Solution1(object):
    def repeatedSubstringPattern1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 1:
            return False

        i=1
        while i <= (n//2):
            if n % i == 0:
                if s[0:i]* (n//i) == s:
                    return True
                else:
                    i += 1
            else:
                i += 1
        return False

s = Solution1()
print(s.repeatedSubstringPattern1('abab'))





