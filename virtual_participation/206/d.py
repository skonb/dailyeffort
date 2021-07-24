import math
N = int(input())
A = list(map(int, input().split()))
lenA = len(A)
A1 = A[:lenA//2]
A2 = list(reversed(A[math.ceil(lenA/2):]))
print(A, A1, A2)
