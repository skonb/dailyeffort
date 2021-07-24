import math
N = int(input())
N *= 1.08
if math.floor(N) == 206:
    print('so-so')
elif math.floor(N) < 206:
    print('Yay!')
else:
    print(':(')
