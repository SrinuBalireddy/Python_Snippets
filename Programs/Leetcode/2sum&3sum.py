# Write your code here :-)

# 2sum


def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0: return nums

        for i in nums:
            secondval = target - i
            if secondval in nums[nums.index(i)+1:]:
                return [nums.index(i), nums.index(secondval)]

        return 'No indexes match the target'

print(twoSum([3,2,4], 6))

# 3sum
class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0 and (nums[i-1] == nums[i]): continue

            target = -nums[i]
            beg, end = i+1, n-1

            while beg < end:
                if nums[beg]+nums[end] < target:
                    beg += 1
                elif nums[beg]+nums[end] > target:
                    end -= 1
                else:
                    result.append((nums[i], nums[beg], nums[end]))
                    beg += 1
                    end -= 1

        return result
