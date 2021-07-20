from typing import List
#N = int(input())
#class1 = []
#class2 = []
#tmp_class1_sum = 0
#tmp_class2_sum = 0
# for _ in range(N):
#    c, p = map(int, input().split())
#    if c == 1:
#        tmp_class1_sum += p
#        tmp_class2_sum += 0
#    else:
#        tmp_class1_sum += 0
#        tmp_class2_sum += p
#    class1.append(tmp_class1_sum)
#    class2.append(tmp_class2_sum)
#Q = int(input())
# for _ in range(Q):
#    L, R = map(int, input().split())
#    # 0オリジンに調整
#    L -= 1
#    R -= 1
#    class1_score = class1[R]-(0 if L == 0 else class1[L-1])
#    class2_score = class2[R]-(0 if L == 0 else class2[L-1])
#    print(f'{class1_score} {class2_score}')

# 007 - CP Classes（★3）
# 戦略 : B_jに対し不満度が最も小さくなるQをナイーブに探すとO(NQ)時間かかる
# そこで，Qを2分探索で見つけ出すことにする
import bisect


def bin_search(b: int, sortedA: List[int]) -> int:
    #left = 0
    #right = len(sortedA)-1
    # while right - left > 1:
    i = bisect.bisect_left(sortedA, b)
    if i == 0:
        return abs(sortedA[i]-b)
    elif i == len(sortedA):
        return abs(sortedA[i-1]-b)
    return min(abs(sortedA[i]-b), abs(sortedA[i-1]-b))


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A.sort()
min_sum = 0
for _ in range(Q):
    b = int(input())
    print(bin_search(b, A))
