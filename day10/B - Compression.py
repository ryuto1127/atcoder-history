n = int(input())
As = list(map(int, input().split()))

Cs = sorted(set(As))

print(len(Cs))
print(*Cs)