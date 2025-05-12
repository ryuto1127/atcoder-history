n, a, b = map(int, input().split())

total = 0

for num in range(1, n + 1):
  if b >= sum(map(int, str(num))) >= a:
    total += num
    
print(total)