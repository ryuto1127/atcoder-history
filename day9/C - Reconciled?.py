import math

n, m = map(int, input().split())

if abs(n - m) > 1:
  print(0)
elif n > m:
  print(math.factorial(m) * math.factorial(m) * n % (10 ** 9 + 7))
elif n == m:
  print(math.factorial(m) * math.factorial(m) * 2 % (10 ** 9 + 7))
else:
  print(math.factorial(n) * math.factorial(n) * m % (10 ** 9 + 7))

"""
すぬけ君は、犬を 
N 匹と猿を 
M 匹飼っています。すぬけ君は、この 
N+M 匹を一列に並べようと思っています。

文字通り犬猿の仲の犬たちと猿たちを仲直りさせたいすぬけ君は、犬同士、または猿同士が隣り合うところができないように並べようと思っています。

このような並べ方は何通りあるでしょうか。犬と猿は 
10 
9
 +7 以上の数を理解できないので、並べ方の個数を 
10 
9
 +7 で割ったあまりを求めてください。 ただし、犬同士、また猿同士は互いに区別します。また、左右が反転しただけの列も異なる列とみなします。
"""