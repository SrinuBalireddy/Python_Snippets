# Write your code here :-)
""" Question ----
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

# iterative solution
import copy

nums = [1, 2, 3]
result = [[]]
"""
for num in nums:
    new_result = copy.deepcopy(result)

    for index in range(len(result)):
        new_result[index].append(num)

    result += new_result
"""

for num in nums:
    for i in range(len(result)):
        r = result[i] + [num]
        result.append(r)

print(result)


a = 3

for i in range(a):
    print(i)
    a += 1
    if a == 10:
        break

