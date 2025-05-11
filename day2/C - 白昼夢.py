s = input()

while s:
  if s.endswith("dream"):
    s = s[:-5]
  elif s.endswith("dreamer"):
    s = s[:-7]
  elif s.endswith("erase"):
    s = s[:-5]
  elif s.endswith("eraser"):
    s = s[:-6]
  else:
    print("NO")
    break
else:
  print("YES")

  """
  else if could be elif

  python is sensitive to spaces

  these codes are different

  s = "dream"

while s:
    if s.endswith("dream"):
        s = s[:-5]
    else:
        break
else:
    print("YES")  # this is included to while


while s:
    if s.endswith("dream"):
        s = s[:-5]
    else:
        break
    else:
    print("YES")  # this is not part of while and causes an error

  """