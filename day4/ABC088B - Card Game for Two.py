n = int(input())
numbers = list(map(int, input().split()))
  
numbers.sort(reverse=True)
alice = 0
bob = 0

for i in range(1, n + 1):
  if i % 2 == 1:
    alice += numbers[i -1]
  else:
    bob += numbers[i - 1]
    
print(abs(alice - bob))

"""
i have already done this question before but i did again for reviewing.
i cound make it without stoping and help this time!
"""