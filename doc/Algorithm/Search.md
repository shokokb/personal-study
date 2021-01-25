# Search(探索)

## Linear Search(線形探索）

- Time Complexity:O(n)
- 配列はソートされていなくて良い

## Binary Search

- Time Complex:O(logN)
- 配列は常に序列が守られている必要がある

## DFS

- 深さ優先探索 （DFS：Depth-First Search）連鎖で探索　再帰で書ける
- コールスタックを使用する
- 全ての解を生成する

### pre-order

### in-order

### post-order

## BFS

- 幅優先探索 （BFS：Breath-First Search）
- 計算量は O（状態数 x 遷移の仕方）
- キューに状態を入れていくのでメモリーを必要とする
- 一度経験した経路を保存しなければならない
- メモリー使用量は深さ優先探索（最大の深さ分）<幅優先探索
- 反復進化深さ優先探索（IDDFS：Iterative Deepening Depth-First Search）
- 再帰の回数を１回に制限しておき、解が見つからなければ、どんどん再帰を深くしていく
- 適用
  - 最短経路問題
