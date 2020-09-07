# Write your code here :-)
numlist = [2,5,6,7,8,8,9]
target = 11

def binary_search_closest(numlist, target):

    low = 0
    high = len(numlist)-1
    min_diff = float('inf')
    closest_num = None

    while low <= high:
        mid = (low+high)//2

        # To validate right element of mid is not
        # out of index
        if mid+1 < len(numlist):
            right_diff = abs(numlist[mid+1] - target)
        if mid > 0:
            left_diff = abs(numlist[mid-1] - target)

        # check if the left and right difference are
        # less than the min_diff and assign min_diff value
        if right_diff < min_diff:
            min_diff = right_diff
            closest_num = numlist[mid+1]
        if left_diff < min_diff:
            min_diff = left_diff
            closest_num = numlist[mid-1]

        if target > numlist[mid]:
            low = mid+1
        elif target < numlist[mid]:
            high = mid-1
        else:
            return numlist[mid]

    return closest_num

print(binary_search_closest(numlist,target))
