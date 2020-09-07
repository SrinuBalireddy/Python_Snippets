# Write your code here :-)

def seating(n, s):

    occupied = s.split(' ')
    available  = 0

    for i in range(1,n+1):

        row= str(i)

        if not (row+'A' in occupied or row+'B' in occupied or row+'C' in occupied):
            available+=1
        if (not (row+'D' in occupied and row+'G' in occupied) and (not (row+'E' in occupied or row+'F' in occupied))):
            available+=1
        if not (row+'H' in occupied or row+'J' in occupied or row+'K' in occupied):
            available+=1

    return available

print(seating(1,''))
print(seating(2,'1A 2J'))
print(seating(10,'1A 2J 8D 6G'))



'''
        elif (row+'D' not in occupied and (not (row+'E' in occupied or row+'F' in occupied or row+'G' in occupied))):
            available+=1
        elif (row+'G' not in occupied and (not (row+'E' in occupied or row+'F' in occupied or row+'D' in occupied))):
            available+=1


def solution(N: int, S: str, n: int) -> int:
    """
    return option count
    """
    taken = [[] for _ in range(N)]
    for s in S.split(" "):
        row = int(s[:-1]) - 1
        if row > N:
            raise Exception("illegal reservation")

        taken[row].append(ord(s[-1]) - ord('A'))

    total_cnt = 0
    for row in taken:
        row.sort()
        row.append(ord('K') - ord('A') + 1)
        last = -1

        cnt = 0
        for idx in range(len(row)):
            free_seats = row[idx] - last - 1
            cnt += max(0, free_seats - (n - 1))
            last = row[idx]

        total_cnt += cnt

    return total_cnt


taken = [[] for _ in range(20)]
print(taken)
print(ord('32'))
'''
