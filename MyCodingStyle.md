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


