# Write your code here :-)
#numlist = [1,2,5,6,6,8,9]

def binary_nearest_num(list, target):

    min_diff = float('inf')
    low = 0
    high = len(list)-1
    closest_num = None

    # Edge cases for empty list ord
    # if the list has only one element
    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]

    while low <= high:
        mid = (low+high)//2

    # Ensure we are not moving out of range and
    # fetch the right and left elements from the mid
        if mid + 1 < len(list):
            min_diff_right = abs(list[mid+1] - target)
        if mid > 0:
            min_diff_left = abs(list[mid-1] - target)

        # check if the absolute values of left and right
        # elements are smaller than any seen prior
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = list[mid+1]

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = list[mid-1]

        # move the mid point as per the binary search alogirthm
        if target > list[mid]:
            low = mid + 1
        elif target < list[mid]:
            high = mid -1
        else:
            return list[mid]

    return closest_num

numlist = [2,5,6,7,8,8,9]
target = 4
res = binary_nearest_num(numlist, target)
print(res)











#linear search
"""
numlist = [1,2,4,6,5,4,3,6,8,9]
numlist = set(numlist)
print(numlist)
target = 10

def binary_nearest_num(list,target):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high)//2


def nearest_num(list, target):

    diff = {}
    newlist =[]

    for num in list:
        diff[num] = target-num

    for _,v in diff.items():
        newlist.append(v)

    least = min(newlist)
    print(least)

    print(list(my_dict.keys())[list(my_dict.values()).index(112)])


nearest_num(numlist,13)

"""

