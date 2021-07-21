# 2-3動的計画法

# の前にDPの復習
# 2-2-4例題
# C - Multiple Gift
# アイデア : A{i+1}がAiの倍数でA{i+1}>Aiならば最小のものは2倍
# import math
# X, Y = map(int, input().split())
# cnt = 1
# while True:
# if (X := X * 2) <= Y:
# cnt += 1
# else:
# break
# print(cnt)
# if Y % X == 0:
# print(math.floor(math.log2(Y//X))+1)
# else:
# print(math.floor(math.log2(Y/X))+1)
# 動的計画法
# 0-1 Knapsack Problem
# 縦をアイテムナンバー，横を重さとする
N, W = map(int, input().split())
dp_item_weight = [[0 for _ in range(W+1)] for _ in range(N)]

for i in range(N):
    v, w = map(int, input().split())
    for w_ in range(1, W+1):
        if i == 0:
            if w_ >= w:
                dp_item_weight[i][w_] = v
        else:
            if w_-w >= 0:
                dp_item_weight[i][w_] = max(
                    [dp_item_weight[i-1][w_], dp_item_weight[i-1][w_-w]+v])
            else:
                dp_item_weight[i][w_] = dp_item_weight[i-1][w_]

# print(dp_item_weight)
print(max(dp_item_weight[-1]))
