import heapq
import bisect
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

distances = []
distances = [A[i+1]-A[i] for i in range(N-1)]
distances.insert(0, A[0])
distances.append(L - A[N - 1])

#
# 作成には線形時間が必要
#sorted_distances = heapq.heapify(distances)
sorted_distances = sorted(distances, reverse=True)

##print(distances, sorted_distances)

# N回分割するということは，N-K回結合するということ
# 戦略としては，最小のピースとその隣を結合して，最小スコアをもつピースを除外し続けることを考える
# 作業中のデータの保持にはヒープ木(heapq)を使おう...と思っていたが，結局のところ削除にO(N)必要なので，bisectを使ってみることにする


for _ in range(N - K):
    # 最小のピースの位置を見つける
    # ソート済みリストから最小ピースのpop
    min_elem = sorted_distances.pop()
    # 元リスト内の位置を特定
    min_elem_index = distances.index(min_elem)

    # 最小のピースを結合する
    # 両隣，小さい方を探す
    # 左側がない
    smaller_neighbor_index: int
    if min_elem_index == 0:
        smaller_neighbor_index = 1
    # 右側がない
    elif min_elem_index == (len_distances := len(distances) - 1):
        smaller_neighbor_index = len_distances-1
    else:
        r_neighbor = min_elem_index+1
        l_neighbor = min_elem_index-1
        smaller_neighbor_index = l_neighbor if distances[
            l_neighbor] < distances[r_neighbor] else r_neighbor
    smaller_neighbor = distances[smaller_neighbor_index]

    # ピースの結合・各データ構造の更新
    ###print(distances, min_elem, smaller_neighbor, smaller_neighbor_index)
    new_elem = min_elem + smaller_neighbor
    #print(distances, min_elem, smaller_neighbor)
    distances[min_elem_index] = new_elem
    distances.remove(smaller_neighbor)

    sorted_distances.remove(smaller_neighbor)
    # 挿入箇所を2分探索
    left = 0
    right = len(distances)-1
    while True:
        if right - left <= 1:
            sorted_distances.insert(left, new_elem)
            break
        pos = (right+left)//2
        # 左が大きい，右が小さい
        if sorted_distances[pos - 1] > new_elem:
            # 今いるところが大きすぎるので小さいエリア=右に移動:
            left = pos
        else:
            # 今いるところが小さすぎるので大きいエリア=左に移動:
            right = pos
    # print()


print(sorted_distances[-1])
