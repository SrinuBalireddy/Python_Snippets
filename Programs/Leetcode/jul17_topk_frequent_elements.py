# Write your code here :-)
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        res = []
        for i in count.most_common(k):
            res.append(i[0])

        # other optimal solution
        """
        # O(1) time
        if k == len(nums):
            return nums

        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)
        """

        return res

s= Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))
