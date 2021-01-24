# Complexity

- Time Complexity:時間計算量
- Space Complexity:空間計算量

# Search(探索)

## 線形探索

- O(n)

## DFS

- 深さ優先探索 （DFS：Depth-First Search）連鎖で探索　再帰で書ける
- コールスタックを使用する
- 全ての解を生成する

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

## 枝刈り

### ダイクストラ法

### ベルマンフォード

# グラフ

## P/NP/NP-Complete/NP-Hard 問題

- 貪欲（どんよく）法：
  　各ステップで局所的最適解を選ぶ
  　証明）帰納法・背理法で証明できる
  　応用）ハフマン符号　文字列 ⇨ 数値化（頻度の大きいものを短い文字列にする）
  解なし：NP 完全問題

- Dynamic Programing
  - Knapsack Problem

## 集合カバー問題

- べき集合
- O(2^n)

## 巡回セールスマン問題

- O(n!)
- 階乗関数(factual function)

## 動的計画法 Dynamic Programming（部分ナップサック）グリッド

ファインマンアルゴリズム
最長共通部分文字列
最長共通部分列 DNA
diff
レーベンシュタイン距離　類似度
行の折り返し

K 近傍法(k nearest neighbor algorithm)　
分類システム　制限
特徴量：例）サイズ、色
類似度　
Distance
コサイン類似度(coscine similarity) ベクトルの角度
特徴(feature)抽出 A と B がどれだけ似通っているか
Distance の正規化　ルート n の近傍
回帰　 regression（星の数の平均値）Distance が最も近い例
OCR トレーニング
スパムフィルタ：ナイーブ(単純)ベイズ分類

Binary search tree 小-中(親)-大
B 木
赤黒木
ヒープ
スプレー木

転置インデックス inverted index：検索ハッシュ

フーリエ変換　圧縮

並列アルゴリズム　非線形
　並列処理管理のオーバーヘッド（マージ）
　ロードバランシング
分散アルゴリズム

ブルームフィルタ　おそらく正しい答え　確率的データ構造(probablistic data structure)　
　偽陽性・偽陰性
　非常に大きな集合

SHA アルゴリズム(Secure Hash Algorithm)　文字列 ⇨ スロット番号

LS ハッシュ　似たようなデータを入れたときに似たようなスロット番号　 SlimHash
　クロールの類似、文書の類似

ディフィーヘルマン鍵交換　メッセージを暗号化して、相手だけようにする
　公開鍵・秘密鍵　 RSA が後継

線形計画法　グラフアルゴリズム　シンプレックス法

ワンパスアルゴリズム

- ビットベクトル