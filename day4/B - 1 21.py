a, b = map(int, input().split())

num = int(str(a) + str(b))

root = int(num ** 0.5)

if root * root == num:
  print("Yes")
else:
  print("No")