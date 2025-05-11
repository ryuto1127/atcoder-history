n = int(input())

values = []
for _ in range(n):
    values.append(int(input()))

unique = set(values)
print(len(unique))


"""
when getting maltiple values by vertical lines like
1
2
2
3
we can use this way
values = []
for _ in range(n):
    values.append(int(input))

append means adding new values

set(a) deletes same values in a

len(a) shows the length of a
"""