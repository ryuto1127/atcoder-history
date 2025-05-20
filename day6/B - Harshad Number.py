n = int(input())

numbers = list(map(int, str(n)))

if n % sum(numbers) == 0:
  print("Yes")
else:
  print("No")  

"""
this is my first time that i could get 'correct' at the first try without any hints!
"""