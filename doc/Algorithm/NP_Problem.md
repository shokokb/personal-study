# チューリング・マシン

- 決定性チューリング・マシン
  - データ x に決まった y が一意づけられて表示される；y = f(x)
  - 例）普通のコンピュータ
  - 現在の状態 S から次の状態へ N 分岐があり、その深さを H とするとき、計算量は N^H
- 非決定性チューリング・マシン
  - データ x に決まった y が一意づけられて表示されていない
  - 現在の状態から次の状態への遷移選択に置いて、解に近づく選択肢を選べるマシン
  - 例）量子コンピュータ・並列処理できる高性能のコンピュータ等
  - 現在の状態 S から次の状態へ N 分岐があり、その深さを H とするとき、計算量は H

# 判定問題

- 判定問題=二値分類問題
  - 二分：0 or 1, yes or no

# NP Problem

- P(Polynominal=多項式)

  - 0 or 1 で解ける問題で、解が一意付けされた数学的に理想的なマシンによって、多項式を解ける相当の時間で解かれる集合
  - 現実的に（効率的に）解ける問題クラス
  - 判定問題を多項式で計算できる問題
    - 判定問題のうち、ある決定性チューリング機械によって多項式時間で解かれるものの全体を P で表す。
  - 具体的例題
    - ダイクストラ法

- NP(Non-deterministic Polynomial time)

  - 非決定性チューリングマシンによって多項式時間で解くことができる問題
    - → 漸化式
  - yes となる証拠が与えられたとき、その証拠が本当に正しいかどうかを多項式時間で判定できる問題

- NP-Hard（NP 困難）
  - NP に属しているかわからないが、少なからず、NP よりは複雑。
  - 問題が「NP に属する任意の問題と比べて、少なくとも同等以上に難しい」ことである
  - 正確にいうと問題 H が NP 困難であるとは、「NP に属する任意の問題 L が H へ帰着可能である」と定義される
  - 具体的な問題
    - 巡回セールスマン問題
    - ナップサック問題
- NP-Complete

  - NP かつ NP-Hard、NP の中では最難関の問題
  - NP（Non-deterministic Polynomial）に属する決定問題（言語）で、かつ 任意のクラス NP に属する問題から多項式時間還元（帰着）可能なもののことである
  - 具体的な問題
    - 部分和
    - ハミルトン平路問題（全ての交差点を通過する経路があるか否かを解く問題、組み合わせ最適化問題）
    - 充足性問題
    - ３充足性
    - 頂点被覆
    - ゲーム：ぷよぷよ・テトリス

- 多項式時間還元(polynomial-time reduction)
  - 問題 A を１回の基本演算と同じ時間で解くアルゴリズム α があれば，α をサブルーチンとして用いることで問題 B を多項式時間で解くことが できるとき，B は A に多項式時間還元可能であるという．

# P/NP の違い

- 何を使って多項式で解けるかどうか
  - 決定性チューリングマシンを使って多項式で解ける場合：P
  - 非決定性チューリングマシンを使って多項式で解ける場合：NP

# NP-Hard/NP-Complete の違い

- NP-Complete:問題 A が NP で，全ての NP 問題が A へ多項式時間還元可能なとき
- NP-Hard:全ての NP 問題が A へ多項式時間還元可能なとき

---

# P≠NP 予想

- NP は P を自明に含む。しかし、P は NP と等しくない
