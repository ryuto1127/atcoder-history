n, a, b = map(int, input().split())

total = 0

for i in range(1, n + 1):
    if b >= sum(map(int, str(i))) >= a:  # ← コロン追加！
        total += i

print(total)

"""

"""