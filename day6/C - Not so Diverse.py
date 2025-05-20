from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

count = Counter(a)
freq = sorted(count.values())

# 種類数が K 以下なら書き換え不要
if len(freq) <= k:
    print(0)
else:
    # 種類数が K を超える場合、出現回数が少ないものから書き換え
    print(sum(freq[:len(freq) - k]))
"""
this is an example that is not used 'collections'

n, k = map(int, input().split())
a = list(map(int, input().split()))

# 出現回数を数える（Counterなしで）
count_dict = {}
for num in a:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# 出現回数だけのリストを作る
freq = list(count_dict.values())

# 種類数がk以下なら何も変える必要なし
if len(freq) <= k:
    print(0)
else:
    freq.sort()  # 出現回数が少ない順にソート
    # 少ないものから (種類数 - k) 個分を消す
    print(sum(freq[:len(freq) - k]))


"""