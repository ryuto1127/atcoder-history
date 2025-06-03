# N: 壁の枚数, M: 操作の数
N, M = map(int, input().split())

# (1) 差分配列を 0 で初期化 (インデックス 1 ～ N を使い、R+1 のために N+2) まで確保
diff = [0] * (N + 2)

# (2) M 回の操作を読み込んで差分配列に反映
for _ in range(M):
    L, R = map(int, input().split())
    diff[L] += 1       # インデックス L 以降に +1 の影響を与える
    diff[R + 1] -= 1   # インデックス R+1 以降でその影響を打ち消す

# (3) 累積和を取って各壁のペイント回数を求める
count = [0] * (N + 1)
curr = 0
for i in range(1, N + 1):
    curr += diff[i]
    count[i] = curr
    
print(min(count[1:]))