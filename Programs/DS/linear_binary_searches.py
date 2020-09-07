# Write your code here :-)


numlist = [n for n in range(21)]
target = 15

#linear_search
def linear_search(list,target):
    for i in list:
        if i == target:
            return 'Target element is available in the list at the index ' + str(list.index(i))
    return 'Target element is not available in the list.'

#print(linear_search(numlist,target))

#binary_search_iterative
def binary_search_iterative(list, target):

    low = 0
    high = len(list)-1
    i=0

    while low <= high:
        i+=1
        mid = (low+high)//2
        if target == list[mid]:
            return 'Target element found at the index '+ str(mid)+ ' in ' + str(i) + ' tries'
        elif target > list[mid]:
            low = mid+1
        else:
            high = mid-1
    return 'Target element not found'

#print(binary_search_iterative(numlist,target))

#binary_search_recursive
def binary_search_recursive(list, target, low, high, i=0):

    i+=1

    if low > high:
        return 'Target element not found'

    mid = (low+high)//2
    if target == list[mid]:
        return 'Target element found at the index '+ str(mid)+ ' in ' + str(i) + ' tries'
    elif target > list[mid]:
        return binary_search_recursive(list, target, mid+1, high, i)
    else:
        return binary_search_recursive(list, target, low, mid-1, i)

#print(binary_search_recursive(numlist,target,0,len(numlist)-1))
"""
1 - L0, H19, mid9
2 - L10, H19, M14
3 - L10, H13, M11
4 - L12, H13, M12
5 - L13, H13, M12


1 - L0, H19, M9
2 - L10, H19, M14

"""
