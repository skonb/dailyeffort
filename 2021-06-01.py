# 012 - Red Painting（★4）
# 赤マス追加時→互いに到達可能なマス目の組を作成する
# 2マス間探索時→互いに到達可能なマス目の組を一個ずつ見ていく
H, W = map(int, input().split())
Q = int(input())
accessables = []
# log = []
for _ in range(Q):
    order = list(map(int, input().split()))
    # log.append(str(order))
    if order[0] == 1:
        r, c = order[1:3]
        # 0オリジン合わせ
        r -= 1
        c -= 1
        # 上下左右を探索範囲に加える
        kouho = []
        if not r == 0:
            kouho.append(tuple([r-1, c]))
        if not r == H-1:
            kouho.append(tuple([r+1, c]))
        if not c == 0:
            kouho.append(tuple([r, c-1]))
        if not c == W-1:
            kouho.append(tuple([r, c+1]))

        connected = []
        for a in accessables:
            for k in kouho:
                if k in a:
                    a.add(tuple([r, c]))
                    connected.append(a)
        # log.append(f'connected={connected},len={len(connected)}')
        # 候補なしなら新しい島を作る(setを加える)
        if len(connected) == 0:
            accessables.append(set([tuple([r, c])]))
        # 候補が1つだけ
        elif len(connected) == 1:
            pass
        # 候補が2つ以上ならset同士を結合する
        elif len(connected) >= 2:
            sumset = connected.pop(0)
            accessables.remove(sumset)
            for c in connected:
                sumset = sumset | c
                if c in accessables:
                    accessables.remove(c)
            accessables.append(sumset)
        # log.append(str(accessables))

    else:
        ra, ca, rb, cb = order[1:5]
        # 0オリジン合わせ
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
        a = tuple([ra, ca])
        b = tuple([rb, cb])
        printedFlag = False
        for acc in accessables:
            if a in acc:
                if b in acc:
                    print('Yes')
                    # log.append('Yes')
                else:
                    print('No')
                    # log.append('No')
                printedFlag = True
        if not printedFlag:
            print('No')
            # log.append('No')
# debug
# print('\n'.join(log))
