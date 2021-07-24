N = int(input())
A = list(map(int, input().split()))
ans = [i + 1 for i in range(N)]
A.sort()
if A == ans:
    print('Yes')
else:
    print('No')
