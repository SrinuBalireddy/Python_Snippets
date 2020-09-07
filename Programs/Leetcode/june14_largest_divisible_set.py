def largestDivisibleSubset(nums):
    if len(nums) == 0:
        return []
    nums.sort()
    sol = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
                sol[i] = sol[j] + [nums[i]]
    return max(sol, key=len)


print(largestDivisibleSubset([1,2,3]))

sol = [[num] for num in [1,2,3]]
print(sol)



# Write your code here :-)
"""
def largestDivisibleSubset(nums):

        subset= set()
        res = set()


        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a,b = nums[i], nums[j]
                if a%b == 0 or b%a == 0:
                    subset.add(nums[i])
                    subset.add(nums[j])
                else:
                    res.add(nums[j])


        val = list(subset-res)
        val.sort()
        return val

"""
