# H行W列の値を全て足す必要はなく，事前に各行，各列の和を計算しておいて，適切な値を出力すればいい

H, W = map(int, input().split())
A = []
row_sum = []
for _ in range(H):
    a = list(map(int, input().split()))
    row_sum.append(sum(a))
    A.append(a)

column_sum = [0 for _ in range(W)]

for row in A:
    for j, a in enumerate(row):
        column_sum[j] += a

for i in range(H):
    sumrow = []
    row = row_sum[i]
    for j in range(W):
        # print(row_sum[i]+column_sum[j]-A[i][j], end=' ')
        sumrow.append(str(row+column_sum[j]-A[i][j])+' ')
    sumrow.append('\n')

print(''.join(sumrow))
# 5 5 5
# 5 5 5
# 5 5 5
