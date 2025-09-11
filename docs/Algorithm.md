# アプローチ

- 注意深く聞く
- 例を描いてみる
- ブルートフォースで記述する
- 最適化する
  - まだ使われていない情報を見つける
  - 新しい例を描いてみる
  - 間違って描いてみる
  - 実行時間とメモリ消費量のトレードオフを作り出す
  - 前処理を入れる
  - ハッシュテーブルを使う
  - 考える一番良い実行時間を考える
- 見直しする
- 少量のコードで実装する
  - 美しいコード
    - モジュール化されたコード
    - エラーチェックができている
    - クラス／構造体を使っている
    - 良い変数名を使っている
- テストする
  - コンセプト・テスト
  - 怪しいコード
  - ホット・スポット
  - 小さなテストケース
  - 特殊なテストケース　例）空の配列、要素数が１の配列
- BUD を探す
  - B = Bottle-neck
  - U = Unnecessary Work
  - D = Duplicated Work

# Complexity

- Time Complexity:時間計算量 BigO
- Space Complexity:空間計算量

---

# ビット操作

# 再帰(recursive)

# 動的計画法(DP)

# Tree

- Graph には平路が存在するが、Tree には平路は存在しない

## 枝刈り

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

線形計画法　グラフアルゴリズム　シンプレックス法

ワンパスアルゴリズム

# ビット演算子

- Brian Kernighan's Algorithm:2 進数の 1 の個数を求める
- Hamming distance(ハミング距離)

# 素因数分解

- prime number=素数
- 試し割り法　https://note.nkmk.me/python-prime-factorization/

- ビットベクトル

https://qiita.com/drken/items/872ebc3a2b5caaa4a0d0

# BCR(Best convervable Runtime)

# BackTrack