# 🚀 LeetCode DP ロードマップ（解く順番ガイド）

## 🥉 Step 1: 超基礎（DPの型に慣れる）
- [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)  
- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)  
- [198. House Robber](https://leetcode.com/problems/house-robber/)  
- [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)  

👉 DP配列 or 2変数での「状態遷移」の感覚を掴む。

---

## 🥈 Step 2: グリッド系・パス探索
- [62. Unique Paths](https://leetcode.com/problems/unique-paths/)  
- [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)  
- [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)  
- [120. Triangle](https://leetcode.com/problems/triangle/)  

👉 2次元DP（dp[i][j]）の感覚を習得。

---

## 🥉 Step 3: 部分和・ナップサック系
- [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)  
- [494. Target Sum](https://leetcode.com/problems/target-sum/)  
- [322. Coin Change](https://leetcode.com/problems/coin-change/)  
- [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/)  

👉 「dp[i] = ○○できるか/方法数/最小枚数」といった **定義の工夫** を練習。

---

## 🥈 Step 4: 文字列系 DP
- [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)  
- [72. Edit Distance](https://leetcode.com/problems/edit-distance/)  
- [97. Interleaving String](https://leetcode.com/problems/interleaving-string/)  
- [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)  

👉 LCSや編集距離など「文字列比較型のDP」に慣れる。

---

## 🥇 Step 5: LIS・発展
- [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)  
- [354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)  

👉 LIS型（n^2 DP → n log n最適化）を理解。

---

## 🔥 Step 6: 区間DP・応用
- [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)  
- [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)  
- [132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)  
- [139. Word Break](https://leetcode.com/problems/word-break/)  
- [140. Word Break II](https://leetcode.com/problems/word-break-ii/)  
- [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/)  

👉 「区間を切って最適化」「分割統治＋DP」をマスター。

---

## 💎 Step 7: 高難度チャレンジ
- [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)  
- [44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)  
- [887. Super Egg Drop](https://leetcode.com/problems/super-egg-drop/)  

👉 応用力試し。面接でも頻出。

---

# ✅ まとめ
1. **基礎（階段/ハウスロバー）** → 2. **グリッド** →  
3. **ナップサック** → 4. **文字列** → 5. **LIS** →  
6. **区間DP** → 7. **応用** の順に進めると無理なく習得できる。