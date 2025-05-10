n = int(input())

cards = list(map(int, input().split()))

alice = 0
bob = 0

cards.sort(reverse=True)

for i in range(n):
    if i % 2 == 0:
        alice += cards[i]
    else:
        bob += cards[i]
    
print(alice - bob)

"""
mao is used only once while list can be accessed anytime

sort(reverse=True) means sort the things in the order from big to small

using i % 2 == 0 and 1, we can make the code function one by one
"""