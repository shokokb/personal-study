# My Coding Style

## 🎯 Overall Policy: Why and What

With Google SWE interviews in mind, I practice coding design through the following steps:

1. **Step 1 & Step 4: Simultaneously design the intent and working code**  
2. **Step 2: Practice writing code without autocomplete (Google Docs style)**  
3. **Step 3: Memorize the design and implementation to reproduce from memory**

What I especially focus on is clearly defining **Why (background of design)** and **What (the final code product)**.

---

## 🧱 Block Style vs Indentation Style vs Hybrid Style

| Style           | Strengths                                         | Weaknesses                           |
| --------------- | ------------------------------------------------ | ---------------------------------- |
| Block Style     | - Clear start/end with `{}` braces → prevents structural collapse in nesting | - Can result in verbose code        |
| Indentation Style | - Bullet-like, high readability, less code      | - Vulnerable to indentation errors which are hard to recover from |
| Hybrid Style    | - Flexible structuring depending on scale, visual grouping achieved | - Hard to unify style for beginners |

I adopt the **Hybrid Style** among these.

---

## 🛠️ Operational Points of Hybrid Style

### ✅ Small Units

Use **indentation and comments** to clarify processing structure

    # Validate user input
    if not user_input:
        raise ValueError("Empty input")

---

### ✅ Large Units

Create visual blocks using **"=== Block Name ===" comment format**

    # === Data Fetch ===
    def fetch_data():
        ...

    # === Data Processing ===
    def process_data():
        ...

---

## 🚀 Practical Benefits Summary

| Effect           | Description                                             |
| ---------------- | ------------------------------------------------------- |
| 🔁 Refactoring    | - Easy to split and merge by modular units              |
| 🧩 Debug Efficiency | - Intuitive identification of error locations by blocks |
| 💡 Sustained Focus | - Code structure stays intact, lowering cognitive load  |
| ✨ Team Sharing    | - Comment blocks and clear structure make intentions easy to convey |

---

## 💬 Summary Quote

> **"Raise quality without sacrificing speed" — that’s the hybrid style with visual design in mind.**


---

# コーディングスタイル（私的メモ）

## 🎯 全体方針：WhyとWhat

GoogleのSWE面接を見据え、以下のステップでコーディング設計を進めている。  

1. **Step1・Step4：設計意図と動作コードを同時に設計する**  
2. **Step2：コード補完なしで書く練習（Google Docs形式）**  
3. **Step3：設計・実装を暗唱できるレベルまで記憶する**

特に重視しているのは、**設計の背景（Why）と成果物としてのコード（What）を明確にすること**。

---

## 🧱 ブロック型・インデント型・ハイブリッド型の比較

| タイプ        | 長所                                           | 短所                                  |
| ------------ | ---------------------------------------------- | ----------------------------------- |
| ブロック型    | - `{}`で開始・終端が明示され、ネスト構造が崩れにくい | - 記述量が増えやすい                  |
| インデント型  | - 箇条書きのようで可読性が高くコード量も少ない     | - インデント崩れに弱く復旧が難しい    |
| ハイブリッド型 | - 規模に応じ柔軟な構造化と視覚的まとまりを実現    | - 初学者にはスタイル統一が難しいこともある |

自分はこの中で**ハイブリッドスタイル**を採用している。

---

## 🛠️ ハイブリッドスタイル運用ポイント

### ✅ 小さな単位

* **インデントとコメント**で処理構造を明確にする

    # ユーザー入力の検証
    if not user_input:
        raise ValueError("Empty input")

---

### ✅ 大きな単位

* **「=== ブロック名 ===」形式のコメント**で視覚的ブロック化

    # === データ取得 ===
    def fetch_data():
        ...

    # === データ加工 ===
    def process_data():
        ...

---

## 🚀 実務的メリットまとめ

| 効果          | 説明                             |
| ----------- | ------------------------------ |
| 🔁 リファクタリング | - モジュール単位で分割・統合がしやすい      |
| 🧩 デバッグ効率   | - ブロック単位でエラー箇所を直感的に特定可能  |
| 💡 集中力持続    | - コードの形が崩れにくく認知負荷が低い       |
| ✨ チーム共有性    | - コメントブロックと明確な構造で意図が伝わりやすい |

---

## 💬 一言まとめ

> **「スピードを落とさず、品質を上げる」──視覚設計を意識したハイブリッドスタイル。**
