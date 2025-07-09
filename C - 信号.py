b1, r1, b2, r2, t = map(int, input().split())

period1 = b1 + r1
period2 = b2 + r2
count = 0

for a in range(t):
  if (a % period1 < b1) and (a % period2 < b2):
    count += 1
    
print(count)