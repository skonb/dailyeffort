# 008 - AtCounter（★4）
from typing import Dict, Set
count_dict = dict()

flag = list('atcoder')
for f in flag:
    count_dict[f] = set()
N = int(input())
S = input()
strippedS = list()
for i, s in enumerate(S):
    if s in flag:
        strippedS.append(s)

# 「それ以降に部分文字列を何個作れるか」のテーブルを作っておく
flag.reverse()
strippedS.reverse()

table = [[0 for _ in range(len(strippedS))] for _ in flag]
for i, flag_ in enumerate(flag):
    for j, s in enumerate(strippedS):
        # 末端
        if not j == 0:
            table[i][j] = table[i][j-1]

        if s == flag_:
            if i == 0:
                table[i][j] += 1
            else:
                table[i][j] += table[i-1][j]
print(table[-1][-1] % (10**9+7))

# print(table)
