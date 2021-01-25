# 離散数学(Discrete Mathmatics)

# Graph

- node(頂点)
- (辺)...頂点と頂点を繋いでいる線分
- 使用例
  - 最短経路探索

## 辺重みなしグラフ

## 辺重みありグラフ

## 有向グラフ

- 辺にぬきが付いているグラフ

## 無向グラフ

## グラフ探索

## 最短経路問題


## DFS(Depth First Search、深さ優先探索)

- 頂点を探索する際、１つの道を行けるところまで進んでいき、それ以上進むことができなくなったところで、引き返し、次の候補となる道を進む
- 再帰で書ける
- コールスタック（LIFO)を使用する
- 全ての解を生成する

### pre-order

- 前置探索

### in-order

- 中置記法

### post-order

- 後置記法

## BFS(Breath-First Search、幅優先探索)

- 頂点を探索する際、始点に一番近い頂点から優先的に探索する
- 計算量は O（状態数 x 遷移の仕方）
- キュー（FIFO）に状態を入れていくのでメモリーを必要とする
- 一度経験した経路を保存しなければならない
- メモリー使用量は深さ優先探索（最大の深さ分）<幅優先探索
- 反復進化深さ優先探索（IDDFS：Iterative Deepening Depth-First Search）
- 再帰の回数を１回に制限しておき、解が見つからなければ、どんどん再帰を深くしていく
- 適用
  - 最短経路問題

### ダイクストラ法

### ベルマン-フォード法