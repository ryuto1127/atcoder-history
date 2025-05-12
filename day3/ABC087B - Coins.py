a = int(input())
b = int(input())
c = int(input())
x = int(input())

total = 0

for A in range(a + 1):
  for B in range(b + 1):
    for C in range(c + 1):
      if 500 * A + 100 * B + 50 * C == x:
        total += 1
  
print(total)