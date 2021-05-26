# 内包表記・イテレータ・ジェネレータ・yieldの練習
# ジェネレータは関数により値のストリームを返す
# ジェネレータは性能を向上し， メモリ使用を減らし，可読性を高める ... とのこと

# リスト内の平方を計算する時，簡単なforループで出来る

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = []
# for x in a:
#    squares.append(x ** 2)
# print(squares)

# リスト内包表記を用いれば，ループする入力シーケンスに計算式を指定すれば，同じ結果が得られる
# mapよりうるさくなくてよいとされている
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = [x ** 2 for x in a]
# print(squares)

# 条件式で，入力要素からの要素をフィルタリング出来る
# 組み込み関数filterを使えば同じ結果が得られるがみづらい
# alt = map(lambda x:x**2 , filter(lambda x:x%2==0,a))
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_squares = [x ** 2 for x in a if x % 2 == 0]
# print(even_squares)

# (知らなかった！)リスト内包表記では多重ループができる
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 順序に注意
# 普通に2重forループを書いた時の順序になるs
# flat = [x for row in matrix for x in row]
# print(flat)

# 2次元配列を2次元のまま扱うこともできる
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# squared_matrix = [[x**2 for x in row]for row in matrix]
# print(squared_matrix)

# if条件は複数指定できる
# その場合条件はandとして扱う
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = [x for x in a if x > 4 if x % 2 == 0]
# c = [x for x in a if x > 4 and x % 2 == 0]
# print(a)
# print(b)
# print(c)

# ループ・条件が重なると大変見づらいのでif・forで代替し，ヘルパー関数を書いて後述のジェネレーターを導入することを考える

# 代入式を使い内包表記での繰り返し作業をなくす

stock = {'nails': 125,
         'screws': 35,
         'wingnuts': 8,
         'washers': 24
         }
order = ['screws', 'wingnuts', 'clips']


def get_batches(count, size):
    return count // size

# 内包表記を使わない
# result = dict()
# for name in order:
#    count = stock.get(name, 0)
#    batches = get_batches(count, 8)
#    if batches:
#        result[name] = batches
# print(result)


# 内包表記を使う
# result = {name: get_batches(stock.get(name, 0), 8)
#          for name in order if get_batches(stock.get(name, 0), 8) > 0}
# print(result)

# get_batches以下がかぶってるのが気に食わないのでウォルラス演算子(代入式)を用いる
# 冗長な呼び出しがなくなり，見やすくなるし性能が向上するし，いいことづくめ
# result = {name: batches
#          for name in order if (batches := get_batches(stock.get(name, 0), 8) > 0)}
# print(result)

# 内包表記の値の式で代入式を定義するのは間違いではないが，評価順序によってはエラーになるため注意が必要である
# result = {name: (batches := get_batches(stock.get(name, 0), 8))
#          for name in order if batches > 0}
# print(result)
# Traceback (most recent call last):
#  File "/Users/Irene/programs/daily/2021-05-25.py", line 83, in <module>
#    result = {name: (batches := get_batches(stock.get(name, 0), 8))
#  File "/Users/Irene/programs/daily/2021-05-25.py", line 84, in <dictcomp>
#    for name in order if batches > 0}
# NameError: name 'batches' is not defined

# 内包表記の中で代入式を使うと，変数名が内包表記を含むスコープにリークする
# half = [(squared := last**2)
#        for count in stock.values() if (last := count // 2) > 10]
# print(f'last item of {half} is {last} ** 2 = {squared}')

# これは通常のループでも起こる
# for count in stock.values():
#    last = count//2
#    squared = last**2
# print(last, count)

# しかし，代入式を伴わない内包表記のループではリークが起こらない
# half = [count//2 for count in stock.values()]
# print(half)
# print(count)  # 実行時例外
# half = [(count := count_)//2 for count_ in stock.values()]
# print(half)
# print(count)  # 実行時例外

# 代わりにジェネレータを作ってみる
# found = ((name, batches) for name in order if (
#    batches := get_batches(stock.get(name, 0), 8)))
# print(next(found))
# print(next(found))

# リストを返さずにジェネレータを返すことを考える
# 文字列中の単語の位置のインデックスをすべて求める
# def index_words(text):
#    result = []
#    if text:
#        result.append(0)
#    for index, letter in enumerate(text):
#        if letter == ' ':
#            result.append(index+1)
#    return result
#
#
# address = "Four score and seven years ago..."
# result = index_words(address)
# print(result[:10])

# このindex_words関数には2つ問題がある
#  1. コードが複雑で読みづらい
#  2. 結果を返す前に，すべての結果をリストに格納する必要がある(≒入力が大量にあるときには，プログラムがメモリを食いつぶしクラッシュを引き起こしかねない)
# ジェネレータを使うとこの関数はもっと上手く書ける
# ジェネレータとは，yield式をつかう関数のこと
# def index_words_iter(text):
    # if text:
    # yield 0
    # for index, letter in enumerate(text):
    # if letter == ' ':
    # yield index+1
#
#
# index_words_iter関数は，結果リストに関する処理のすべてが省かれていて，遥かに読みやすい
# 結果はyield式に渡される
# ジェネレータ呼び出しで返されるイテレータは，list()関数に渡して簡単にリストに変更できる
# ジェネレータはメモリをそれほど必要としないためどんな長さの入力にも容易に対応できる
# このようなジェネレータは「ステートフル」で「再利用できない」ことに注意する
# address = "Four score and seven years ago..."
# result = list(index_words_iter(address))
# print(result)

# 引数に対してイテレータを使うときは確実さを優先する
# 米国テキサス州の旅行者の人数について分析するため，人数を全体の比率に正規化する
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result


#visits = [15, 35, 80]
#percentages = normalize(visits)
# print(percentages)
#assert sum(percentages) == 100


# ジェネレータを使ってファイルを読み出す
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


# 結果が得られない
# これは，イテレータが結果を一度しか結果を一度しか返さないため
#it = read_visits('my_numbers.txt')
#percentages = normalize(it)
# print(percentages)

# 解決策としては，入力イテレータを明示的に終わるまで動かし，内容全体の複製をリストに保持する


def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result


#it = read_visits('my_numbers.txt')
#percentages = normalize_copy(it)
# print(percentages)
#assert sum(percentages) == 100


#もう一つの解決策として，ジェネレータを呼び出して，新たなイテレータをそのたびに生成する
def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100*value/total
        result.append(percent)
    return result


path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
assert sum(percentages) == 100
