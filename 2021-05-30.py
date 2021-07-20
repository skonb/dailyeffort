#from collections import defaultdict
#from math import gcd
#A, B, C = map(int, input().split())
#
#gcd_of_abc = gcd(gcd(A, B), C)
# print(A//gcd_of_abc+B//gcd_of_abc+C//gcd_of_abc-3)


#edge_dict = defaultdict(int, [])
#edge_dict[A] += 1
#edge_dict[B] += 1
#edge_dict[C] += 1
#
#min_size = min(edge_dict.keys())
#after_min_size = -1
#
#cnt = 0
#
#updated = True
# while updated:
#    updated = False
#    new_edge_dict = defaultdict(int, [])
#    for k, v in edge_dict.items():
#        cnt += (k//min_size)*v
#        new_edge_dict[min_size] += (k//min_size)*v
#        new_edge_dict
#        if k % min_size:
#            cnt += 1
#            updated = True
#            new_edge_dict[k % min_size] += 1
#    min_size = min(new_edge_dict.keys())
#    edge_dict = new_edge_dict
#    print(new_edge_dict)
#
# print(cnt)
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dist = 0
for a, b in zip(A, B):
    dist += abs(a-b)

if dist > K:
    print("No")
elif dist == K:
    print("Yes")
elif (K - dist) % 2 == 0:
    print("Yes")
else:
    print("No")


