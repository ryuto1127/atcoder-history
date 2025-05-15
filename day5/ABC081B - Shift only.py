n = input()

numbers = list(map(int, input().split()))

count_list = []

for num in numbers:
  count = 0
  while num % 2 == 0:
    count += 1
    num //= 2
  count_list.append(count)
  
print(min(count_list))