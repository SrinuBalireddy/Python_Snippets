# Write your code here :-)
def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits)==0:
            return digits
        else:
            number = int(''.join([str(k) for k in digits]))+1
            #digits[-1] += 1
            return [int(k) for k in str(number)]

print(plusOne([9]))

