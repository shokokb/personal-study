# Python 面接対策 TODOリスト

---

## 1. 必須レベル（反射的に書ける）

### 基本制御構文
- [ o ] 条件分岐（`if`, `elif`, `else`）
- [ ] ループ（`for` + `range` / 直接イテレーション）
- [ ] ループ（`while`）
- [ ] `break` / `continue` の使い方

### データ構造の基本操作
- [ ] `list` の生成・`append`・`pop`・スライス
- [ ] `dict` の生成・アクセス・更新・ループ
- [ ] `set` の生成・追加・集合演算（`&`, `|`, `-`）
- [ ] `tuple`（アンパック含む）

### 組み込み関数
- [ ] `len()`, `min()`, `max()`, `sum()`, `sorted()`
- [ ] `enumerate()`, `zip()`, `map()`, `filter()`
- [ ] `any()`, `all()`

### 内包表記
- [ ] リスト内包表記（例：`[x*2 for x in arr if x > 0]`）
- [ ] 辞書内包表記（例：`{k: v for k, v in data if 条件}`）

### 関数定義
- [ ] 引数（デフォルト値, 可変長 `*args`, `**kwargs`）
- [ ] `return`

### アルゴリズム系小技
- [ ] `sorted(..., key=..., reverse=True)`
- [ ] `heapq`（優先度付きキュー）
- [ ] 二分探索（`bisect`）

---

## 2. 便利レベル（加点要素）

### Python 3.10+ の新機能
- [ ] `match-case`（パターンマッチ）
- [ ] 構造的パターンマッチ（部分一致, アンパック）

### 列挙型
- [ ] `Enum` クラスで定数管理

### デコレータ
- [ ] `@staticmethod`, `@classmethod`
- [ ] カスタムデコレータ

### ジェネレータ
- [ ] `yield` を使った遅延評価

### `functools` / `itertools`
- [ ] `lru_cache`
- [ ] `permutations`, `combinations`, `groupby`

### 型ヒント
- [ ] `list[int]`, `dict[str, int]`
- [ ] `Optional`, `Union`（`from typing import ...`）

### コンテキストマネージャ
- [ ] `with` 文（ファイル操作やリソース管理）

---

## まとめ
- **必須レベル**：基本制御構文・データ構造・組み込み関数は迷わず書けるように
- **便利レベル**：余裕があれば `match-case` や `Enum` で差別化
