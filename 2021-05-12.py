from functools import lru_cache
import sys
from copy import copy
from collections import deque
sys.setrecursionlimit(2000)
## N, L = map(int, input().split())
## K = int(input())
## A = list(map(int, input().split()))
##
## distances = []
## distances = [A[i+1]-A[i] for i in range(N-1)]
## distances.insert(0, A[0])
## distances.append(L - A[N - 1])
##
# 「最大となる最小値」Mを探す
# Mは0以上L以下であることがわかっているので，Mを2分探索する
# leftのほうが条件が満たされる方
## left = 1
## right = L
##
##
# """max_separate_point
# 最大何個の「長さmin_piece以上のピース」に分割できるか？
# """
##
##
# def max_separate_point(D, min_piece):
##
# 分割可能な最大数は貪欲法で解ける
# ↑なぜ？
##    cnt = 0
##    tmp_piece = 0
# for d in D:
##        tmp_piece += d
# if tmp_piece >= min_piece:
##            cnt += 1
##            tmp_piece = 0
# return cnt
##
##
# while True:
# if right - left <= 1:
# print(left)
# exit()
##    mid = (left+right)//2
# 最大ピース長 = midの分割数がK以上なら，条件が満たされる
##
# if K < max_separate_point(distances, mid):
##        left = mid
# else:
##        right = mid
##
#
#
# def make_all_pattern(n: int) -> set:
#    if n == 1:
#        return set([tuple([1])])
#    new_pattern = set()
#    for pattern in make_all_pattern(n - 1):
#        # 今までのパターンに1足す
#        # print(len(pattern))
#        for i in range(len(pattern)):
#            new_pattern.add(
#                pattern[:i]+tuple([pattern[i] + 1])+pattern[i+1:])
#        # 新しい要素の追加
#        for i in range(len(pattern)+1):
#            new_pattern.add(pattern[:i]+tuple([1])+pattern[i:])
#    return new_pattern
#
#
#N = int(input())
#
# if N % 2 == 1:
#    exit()
# ビット全探索ではなく，並び替えパターンを全列挙する
# 2**20 <10^8なので素直にやってもTLEにはならないはず
# ...と思っていたが，カッコの制約をどうやって表現する？となった時に困る
# 「n//2の長さのようかんを長さ1以上の任意のピースにカットする」みたいな話になりそう
# 下から作っていけばいい感じか？
# と思ったけどそれもめんどい
# 条件1:( == )
# 条件2:(で+1，)で-1したときに負数にならない
# for i in range(2 ** N):
#    counter = 0
#    for n in range(N):
#        # n桁目が1かどうかをチェックする
#        if ((i >> n) & 1):
#            counter -= 1
#        else:
#            counter += 1
#            if counter > 0:
#                break
#    if not counter == 0:
#        continue
#    tmpqueue = deque()
#    for n in range(N):
#        if ((i >> n) & 1):
#            tmpqueue.appendleft(')')
#        else:
#            tmpqueue.appendleft('(')
#    print(''.join(tmpqueue))
#
#    print(make_all_pattern(N))
#    for p in :
#        for item in p:
#           print('('*item + ')'*item, end='')
#       print()
