import sys

n = int(input())
places = [(0, 0, 0)]

for _ in range(n):
    t, x, y = map(int, input().split())
    places.append((t, x, y))

for i in range(1, len(places)):
    t1, x1, y1 = places[i - 1]
    t2, x2, y2 = places[i]

    dt = t2 - t1
    dist = abs(x2 - x1) + abs(y2 - y1)

    if dist > dt or (dt - dist) % 2 != 0:
        print("No")
        sys.exit()

print("Yes")
