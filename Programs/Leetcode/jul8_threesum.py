# Write your code here :-)
nums = [-1, 0, 1, 2, -1, -4]

def threesum(nums):

    result = []

    for i in range(1,len(nums)):
        first_index = nums[i-1]
        for j in range(0,len(nums)):
            if nums.index(nums[j]) != i-1 and i !=j:
                twosum = nums[i]+nums[j]
                if first_index+twosum == 0:
                    if len(result) ==0 or (first_index,nums[i],nums[j]) not in result:
                        result.append((first_index,nums[i],nums[j]))

    #for i in range(len(result)-1):
    #    check = all(val in result[i+1] for val in result[i])

    return result

print(threesum(nums))


# leetcode code
def threeSum1(nums):
        nums.sort()
        n, result = len(nums), []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue

            target = -nums[i]
            beg, end = i + 1, n - 1

            while beg < end:
                if nums[beg] + nums[end] < target:
                    beg += 1
                elif nums[beg] + nums[end] > target:
                    end -= 1
                else:
                    if len(result) == 0 or result[-1] != (nums[i], nums[beg], nums[end]):
                        result.append((nums[i], nums[beg], nums[end]))
                    beg += 1
                    end -= 1

        return result

#print(threeSum1(nums))


### final solution from leetcode -

class solution:
    def threeSum(self, nums):
        nums.sort()
        n, result = len(nums), []

        for i in range(n):
            if i>0 and nums[i] == nums[i-1]: continue

            target = -nums[i]
            beg, end = i+1, n-1

            while  beg < end:
                if nums[beg]+nums[end] < target:
                    beg += 1
                elif nums[beg]+nums[end] > target:
                    end -= 1
                else:
                    result.append((nums[i], nums[beg], nums[end]))
                    beg += 1
                    end -= 1
        return set(result)

#s = solution()
#print(s.threeSum(nums))


