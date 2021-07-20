# N, M = map(int, input().split())
# cnt = 0
# less_node_cnt = [0 for _ in range(N+1)]
# for _ in range(M):
#    a, b = map(int, input().split())
#    # a<bの保証
#    if a > b:
#        tmp = b
#        b = a
#        a = tmp
#    # print(a, b)
#    # 自分より頂点番号が小さい隣接頂点の数が０，１，２で処理を分ける
#    # 大きい方から小さい方だけ考えればいい
#    if less_node_cnt[b] == 0:
#        cnt += 1
#        less_node_cnt[b] += 1
#    elif less_node_cnt[b] == 1:
#        cnt -= 1
#        less_node_cnt[b] += 1
#    else:
#        # do nothing
#        pass
#
# print(cnt)

# def base8to9(base8):
#    base10_N = 0
#    # 8進法から10進法へ
#    for i, s in enumerate(reversed(str(base8))):
#        base10_N += 8**i*int(s)
#    base9_N = ""
#
#    if base10_N == 0:
#        return 0
#    while not base10_N == 0:
#        base9_N = str(base10_N % 9)+base9_N
#        base10_N //= 9
#    # print(base9_N)
#
#    return int(''.join(base9_N))
#
#
# N, K = map(int, input().split())
#
# base8_N = N
#
# for _ in range(K):
#    base9_N = base8to9(base8_N)
#    # print(base9_N)
#    base9_N = int(''.join(['5' if i == '8' else i for i in str(base9_N)]))
#    base8_N = base9_N
#
# print(base9_N)
#

from itertools import permutations

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
M = int(input())
XY = [set() for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    # x<yの制約をかける
    XY[x].add(y)
    XY[y].add(x)
# print(XY)

order = [i for i in range(N)]
mincost = -1
for order in permutations(order):
    continueFlag = False
    cost = 0
    prev = -1
    for j, i in enumerate(order):
        if j >= 1:
            # 制約チェック
            if i in XY[prev]:
                continueFlag = True
                break
        cost += A[i][j]
        prev = i
    #print(order, cost)
    if continueFlag:
        continue
    if mincost == -1 or mincost > cost:
        # 制約を満たしているか
        mincost = cost
print(mincost)
