import math

a, b = map(int, input().split())

if (a / b) - math.floor(a / b) > 0.5:
  print(math.ceil(a / b))
else:
  print(math.floor(a / b))