# POJ3617 Best Cow Line
# S = input()
# T = []
# left = 0
# right = len(S)-1
# min_as_dict_order = ''
# for i in range(len(S)):
#    #print(S, left, right)
#    if S[left] < S[right]:
#        min_as_dict_order = S[left]
#        left += 1
#    elif S[left] < S[right]:
#        min_as_dict_order = S[right]
#        right -= 1
#    else:
#        # 前と後ろの文字が一致している
#        # POINT : 前と後ろのどちらを用いるべきかは，反転させた文字列S＿とSの辞書順比較でわかる
#        breakFlag = False
#        for s, s_ in zip(S[left: right + 1], reversed(S[left: right + 1])):
#            if s > s_:
#                # 反転させたほうがいい≒右側から取り除いたほうがいい
#                min_as_dict_order = S[right]
#                right -= 1
#                breakFlag = True
#                break
#            elif s < s_:
#                # 反転させたほうがいい≒左側から取り除いたほうがいい
#                min_as_dict_order = S[left]
#                left += 1
#                breakFlag = True
#                break
#        if not breakFlag:
#            # どちらでもよい
#            min_as_dict_order = S[right]
#            right -= 1
#
#    T.append(min_as_dict_order)
#
# print(''.join(T))

# POJ 3069(未完)
#N = int(input())
#R = int(input())
#X = list(map(int, input().split()))
#
#near = [set() for _ in X]
# for i in range(len(X)):
#    x = X[i]
#    for diff, x_ in enumerate(X[i:]):
#        if x_ - x <= R:
#            near[i].add(i+diff)
#            near[i+diff].add(i)
#        else:
#            break
#
#cnt = 0
# while True:  # len(near) > 0:
#    print(near)
#    maxlen = 0
#    maxlen_pos = 0
#    for i, n in enumerate(near):
#        if maxlen < len(n):
#            maxlen = len(n)
#            maxlen_pos = i
#    # 点をつける = 左端，右端と半径R以内の点をすべて削除
#    fattest = near[maxlen_pos]
#    if len(fattest) == 0:
#        break
#    cnt += 1
#
#    for pos in [min(fattest), max(fattest)]:
#        set_ = near[pos]-fattest
#        for s in set_:
#            near[s] -= fattest
#    for s in fattest:
#        near[s] = set()
#
# print(cnt)
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
    if continueFlag:
        continue
    if mincost == -1 or mincost > cost:
        # 制約を満たしているか
        mincost = cost
print(mincost)
