# Write your code here :-)
class employee:

    def __init__(self, first, last, salary):
        self.first = first
        self.last  = last
        self.salary= salary

    def fullname(self):
        self.fullname = self.first+' '+self.last
        return self.fullname


emp1 = employee('srinu','b','5000')
emp2 = employee('sow','y','6000')


print(emp1.first)
print(emp1.fullname())


matrix = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]

def riverSizes(matrix):
    # Write your code here.

    rows = len(matrix)
    columns = len(matrix[0])
    size = 0
    res =[]

    for i in range(rows):
        for j in range(columns):
            while matrix[i][j]:
                size += 1
                matrix[i][j] = 0
                if i != rows-1:
                    i += 1
            res.append(size)
    return res

print(riverSizes(matrix))


