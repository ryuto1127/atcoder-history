n, s = map(int, input().split())

times = list(map(int, input().split()))
times = [0] + [t * 2 for t in times]

count = 0

for a in range(n):
  difference = times[a + 1] - times[a]
  if difference > 2 * s + 1:
    count += 1
    
    
if count == 0:
  print("Yes")
else:
  print("No")