n = int(input())

nums = []

for a in range(1, n + 1):
  i = 0
  while a % 2 == 0:
    a = a // 2
    i += 1
  nums.append(i)
  
print(2 ** max(nums))