n, k = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort(reverse=True)

b = 0

for a in range(k):
  b += nums[a]
  
print(b)