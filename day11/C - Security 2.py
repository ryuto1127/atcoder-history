s = str(input())

count = 0

for a in range(1, len(s) + 1):
  count += (10 + int(s[-a]) - (count % 10)) % 10
  
print(count + len(s))