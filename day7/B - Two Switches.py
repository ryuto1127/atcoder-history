a, b, c, d = map(int, input().split())

start = max(a, c)
end = min(b, d)

print(max(0, end - start))
