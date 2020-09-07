# Write your code here :-)
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        newlist = [[] for _ in range(numCourses)]
        main_res = []
        for i in prerequisites:
            if i[0] <= numCourses-1:
                newlist[i[0]].append(i[1])
        print(newlist)

        for i in range(len(newlist)):
            counter = 0
            if len(newlist[i]) == 0:
                if i not in main_res:
                    main_res.append(i)
            else:
                for val in newlist[i]:
                    if val in main_res:
                        counter += 1
                    elif len(newlist[val]) == 0:
                        main_res.append(val)
                        counter += 1
                if counter == len(newlist[i]):
                    if i not in main_res:
                        main_res.append(i)

        return main_res


#s = Solution()
#print(s.findOrder(2, [[0,1]]))
#print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
#print(s.findOrder(3, [[0,1],[0,2],[1,2]]))


# new solution

class Solution1(object):
    def findOrder1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def stackfunc(mylist, index, stacklist):
            if len(mylist[index]) == 0:
                if index not in stacklist:
                    stacklist.append(index)
            else:
                for i in mylist[index]:
                    stackfunc(mylist,i, stacklist)
                    if i not in stacklist:
                        stacklist.append(i)

            if index not in stacklist:
                stacklist.append(index)

        newlist = [[] for _ in range(numCourses)]
        main_res = []
        for i in prerequisites:
            if i[1] <= numCourses-1:
                newlist[i[1]].append(i[0])
        print(newlist)

        counter = 0
        for i in range(len(newlist)-1):
            if newlist[i][1] == newlist[i+1][0]:
                counter += 1
            if counter == len(newlist):
                return []

        stacklist = []
        for i in range(len(newlist)):
            stackfunc(newlist, i, stacklist)

        return stacklist[::-1]


s = Solution1()
#print(s.findOrder(2, [[0,1]]))
print(s.findOrder1(4, [[1,0],[2,0],[3,1],[3,2]]))
#print(s.findOrder1(3, [[0,1],[0,2],[1,2]]))


