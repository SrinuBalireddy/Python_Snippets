# Write your code here :-)


# leetcode solution

"""
Let us solve this problem by definition: we do iteration by iteration.
However if N is very big, then we spend O(N) time and it can take too much time.
Note, that there can be only 2^8 possible options for cells (in fact only 2^6 even,
because after first step the first and the last symbols will always be zeros).
It means, that afrer some number of iterations, cells start to repeat, and we found a loop.

How can we find a loop? We need to keep our positions in hash-table,
so we can find loop_len. We do iteration by iteration and if we found a loop,
we need to do (N - i) % loop_len more steps.

Complexity: time and memory is O(64), because the loop size will be not more than 64.
"""

class Solution:
    def next_step(self, cells):
        res = [0]*8
        for i in range(1,7):
            res[i] = int(cells[i-1] == cells[i+1])
        return res

    def prisonAfterNDays(self, cells, N):
        found_dict = {}
        for i in range(N):
            cells_str = str(cells)
            if cells_str in found_dict:
                loop_len = i - found_dict[cells_str]
                return self.prisonAfterNDays(cells, ((N-i) % loop_len))
            else:
                found_dict[cells_str] = i
                cells = self.next_steps(cells)

        return cells


# my solution

    def prisonAfterNDays( cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        [0,1,0,1,1,0,0,1]
        """
        import copy

        i =1

        #for i in range(N):
        while i <= N:
            newcells = copy.copy(cells)
            for j in range(1,len(cells)-1):
                if ((cells[j-1] and cells[j+1]) or (not cells[j-1] and not cells[j+1])):
                    newcells[j] = 1
                else:
                    newcells[j] = 0
            newcells[0], newcells[-1] = 0, 0
            cells = copy.copy(newcells)
            i += 1
            if cells == [0 for _ in range(len(cells))]:
                break

        return cells


class Solution(object):

        def next_step(self, cells):
            res = [0]*8
            for i in range(1,7):
                res[i] = int(cells[i-1] == cells[i+1])
            return res

        def prisonAfterNDays(self, cells, N):
            """
            :type cells: List[int]
            :type N: int
            :rtype: List[int]
            [0,1,0,1,1,0,0,1]
            """
            found_dict = {}
            for i in range(N):
                cells_str = str(cells)
                if cells_str in found_dict:
                    loop_len = i - found_dict[cells_str]
                    return self.prisonAfterNDays(cells, ((N-i) % loop_len))
                else:
                    found_dict[cells_str] = i
                    cells = self.next_step(cells)

            return cells
