from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
appear = defaultdict(int, {})
cnt = 0
for i, a in enumerate(reversed(A)):
    cnt += i-appear[a]
    appear[a] += 1

print(cnt)
: