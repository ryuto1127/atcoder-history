n = int(input())

nums = [2, 1]

for a in range(n + 1):
  if a > 1:
    b = nums[a - 2] + nums[a -1]
    nums.append(b)
    
print(nums[n])

"""
n = int(input())

l0, l1 = 2, 1
for _ in range(n):
    l0, l1 = l1, l0 + l1

print(l0)

this is a simpler version
"""