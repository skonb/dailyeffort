import bisect


N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

# Aのソート済みリストの作成(nlogn)
sortedA = sorted(A)

# K個選ぶということはN-K個結合するってこと
#
for _ in range(N-K):
    # 現在もっとも小さいピースに対して結合を行う
    # 結合後のピースは適切な位置に挿入する

    # 一番小さいピースの検索(logN)
    # ソート済みデータ構造から一番小さいピースを取得(1)
    minv = sortedA.pop(0)
    # 元の配列から一番小さいピースのインデックスを取得(logN)
    minv_index = A.index(minv)

    # 隣のピースとの結合(N)
    # 両隣のうち小さい方を結合(1)
    min_neighbor_index = -1
    if minv_index == 0:
        min_neighbor_index = 1
    elif minv_index == len(A)-1:
        min_neighbor_index = len(A)-2
    else:
        neighbor1 = A[minv_index-1]
        neighbor2 = A[minv_index+1]
        min_neighbor_index = minv_index - 1 if neighbor1 < neighbor2 \
            else minv_index + 1
    minv_neighbor = A[min_neighbor_index]

    newv = minv + minv_neighbor
    # 元リストから片方を削除，片方の値を更新(N,1)
    A.pop(minv_index)
    A[min_neighbor_index] = newv

    # ソート済みリストの更新
    # ソート済みリストから結合前の2要素を削除(logN)
    print(sortedA, minv_neighbor, newv)
    sortedA.remove(minv_neighbor)
    # ソート済みリストに結合後の1要素を挿入(logN)
    sort_pos = bisect.insort(sortedA, newv)
