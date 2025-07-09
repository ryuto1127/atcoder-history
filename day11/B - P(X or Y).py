import math
x, y = map(int, input().split())

SUM = []
DIF = []

for a in range(1, 7):
  for b in range(1, 7):
    if a + b >= x:
      SUM.append((a, b))
    if abs(a - b) >= y:
      DIF.append((a, b))
      
final = set(SUM + DIF)

print(len(final) / 36)