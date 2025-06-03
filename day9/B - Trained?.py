n = int(input())

button = [int(input()) for _ in range(n)]

record = set()
current = 1
count = 0

while current != 2:
  if current in record:
    print(-1)
    break
  record.add(current)
  current = button[current - 1]
  count += 1
else:
  print(count)
