# Write your code here :-)
S, N = input(), int(input())
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))


Hi nagacharan. I will try to explain it:

❶iter(s) returns an iterator for S.

❷[iter(s)]*n makes a list of n times the same iterator for s.

Example: [[iter(s)]*3] = ([iter(s), iter(s), iter(s)])

ADVICE: It's not three copies of the same iterator, it's three times the same iterator object. Really:

for part in zip(*[iter(S)] * N):
It is equivalent to:

it = iter(s)
for part in zip(it, it, it):
❹*[] unpack a list:

Example: print(*[1,2,3,4]) = print(1,2,3,4)

❺zip make an iterator that aggregates elements from each of the iterables.

Example:

>>>x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)]
we have:

zip(*[iter(s)]*3)
It is equivalent to:

itr = iter(s)
zip(itr, itr, itr)
it extracts an item from all the three iterators from the list in order. Since all the iterators are the same object, it just groups the list in chunks of 3.

Example:

for part in zip(*[iter('abcdefghi')]*3):
	print(part)
a,b,c,d,e,f,g,h,i  a,b,c,d,e,f,g,h,i  a,b,c,d,e,f,g,h,i
^                    ^                    ^
      ^                    ^                    ^
            ^                    ^                    ^
Output:

(a,b,c)

(d,e,f)

(g,h,i)
