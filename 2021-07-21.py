# 復習 : BestCowLine(POJ 3617)
# 辞書順で小さくなるようにTを作る
# N = int(input())
# S = input()
#
# 貪欲法で求める．同じ場合，次の物を比較したい -> 逆順・辞書順で比較する
# T = []
# l = 0
# r = N-1
# for _ in range(N):
#    #  辞書順比較をする
#    if S[l:r] < ''.join(reversed(S[l:r+1])):
#        # 正順が小さい -> 左の方が小さい
#        T.append(S[l])
#        l += 1
#    else:
#        # 正順が大きいか同じ -> 右の方が小さい
#        T.append(S[r])
#        r -= 1
#    print(''.join(T), S[l:r+1])
# print(''.join(T))
#
# 類題 :C - Dubious Document 2
#import re
#total_str = input()
#S = input()
#
#T = []
#l = 0
#r = len(S)
#match = False
#
# 逆から正規表現マッチングする
# for i in reversed(range(len(total_str) - len(S)+1)):
#    #print(i, i + len(S), total_str[i: i + len(S)].replace('?', '.'), S)
#    if match := re.match(total_str[i: i + len(S)].replace('?', '.'), S):
#        total_str = total_str[:i] + S + total_str[i + len(S):]
#        match = True
#        break
#
# if not match:
#    print('UNRESTORABLE')
#    exit()
#
#
# for t in total_str:
#    if t == '?':
#        print('a', end='')
#    else:
#        print(t, end='')
# print()

# 類題 :C - 辞書式順序ふたたび
N, K = map(int, input().split())
S = input()
