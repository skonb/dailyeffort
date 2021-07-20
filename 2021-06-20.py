# 典型90問33
# H, W = map(int, input().split())
# if H == 1 or W == 1:
#    print(H * W)
# else:
#    print((H//2+H % 2)*(W//2+W % 2))
# 典型90問55
# from itertools import combinations
# N, P, Q = map(int, input().split())
# A = list(map(int, input().split()))
# A = [a % P for a in A]
# 戦略 : ナイーブに全探索->TLE
# cnt = 0
# for p in combinations(A, 5):
#    # print(p)
#    product = 1
#    for p_ in p:
#        product *= p_
#    cnt += product % P == Q
# print(cnt)

# 戦略 : 再帰で書く
# def select5(target_list, rest_cnt=5, prev_prod=1):
#    cnt = 0
#    if rest_cnt >= 2:
#        for i, l in enumerate(target_list):
#            cnt += select5(target_list[i+1:], rest_cnt-1, prev_prod*l)
#    else:
#        for l in target_list:
#            cnt += (((prev_prod*l) % P) == Q)
#    return cnt
#
#
# print(select5(A))

# 061 - Deck（★2）
from collections import deque
Q = int(input())
queue = deque()
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        queue.appendleft(x)
    elif t == 2:
        queue.append(x)
    else:
        print(queue[x-1])
