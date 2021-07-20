def base8to9(base8):
    base10_N = 0
    # 8進法から10進法へ
    for i, s in enumerate(reversed(str(base8))):
        base10_N += 8**i*int(s)

    print(base10_N)
    base9_N = ""
    while not base10_N == 0:
        base9_N += str(base10_N % 9)
        base10_N //= 9
    base9_N_ = list(reversed(base9_N))
    return int(''.join(base9_N))


N, K = map(int, input().split())

base8_N = N

for _ in range(K):
    base9_N = base8to9(base8_N)
    # print(base9_N)
    for base9_N_ in reversed(str(base9_N)):
        base8_N *= 10
        if base9_N_ == 5:
            base8_N += 5
        else:
            base8_N += base9_N_

# print(base8_N)
