# 復習 : 貪欲法
# C - 積み重ね
#N = int(input())
#mountain_top = []
# for _ in range(N):
#    w = int(input())
#    i = 0
#    for e in mountain_top:
#        if e >= w:
#            mountain_top[i] = w
#            break
#        i += 1
#    if i == len(mountain_top):
#        mountain_top.append(w)
#    # print(mountain_top)
# print(len(mountain_top))
#
#T = int(input())
#N = int(input())
#A = list(map(int, input().split()))
#M = int(input())
#B = list(map(int, input().split()))
#
# if N < M:
#    print('no')
#    exit()
#
# A.sort()
# B.sort()
#
# for b in B:
#    breakFlag = False
#    for ia in range(len(A)):
#        if A[ia] <= b and b <= A[ia] + T:
#            A = A[ia + 1:]
#            breakFlag = True
#            break
#    if not breakFlag:
#        print('no')
#        exit()
# print('yes')
#
#N = int(input())
#A = list(map(int, input().split()))
#target = set([0])
# for a in A:
#    target_ =  target.copy()
#    for e in target:
#        target_.add(a + e)
#    target = target_
#
# print(len(target))
#
