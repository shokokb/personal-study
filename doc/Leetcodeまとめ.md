# LeetCode問題 典型パターンまとめ

## 🟢 Easy問題パターン

| パターン | 例題 | 処理の特徴 | コメント |
|-----------|------|------------|----------|
| Linear Search（線形走査） | Longest Common Prefix | 文字列や配列を先頭から順に比較、違ったら終了 | 早期リターンで効率的 |
| Dictionary / HashMap | Valid Anagram, Valid Parentheses | 出現回数や対応関係を辞書で管理 | 文字・数値の対応を簡単に確認 |
| Stack（番兵） | Valid Parentheses | 開き括弧を積み、閉じ括弧で対応確認 | 空スタックチェックで安全に処理 |
| Back-loop（末尾走査） | Length of Last Word | 文字列の末尾から逆順走査、空白スキップ | Space O(1)で効率的 |
| Two Pointer / In-place | Remove Element | 配列の2つのポインタで不要要素を飛ばす | in-placeでメモリ効率良し |
| Sort + Edge Check | Longest Common Prefix (Dictionary Sort版) | 配列をソートして先頭と末尾だけ比較 | 中間の要素は無視 |
| Sliding Window（窓スライド） | Max Consecutive Ones, Longest Substring Without Repeating Characters | 連続部分や条件に合う範囲を左右でスライド | Mediumに応用されやすい |
| Counting / Frequency Array | Missing Number, Single Number | 出現回数やフラグで管理 | Easy問題の整数配列パターン |

## 🟠 Medium問題パターン

| パターン | 例題 | 処理の特徴 | コメント |
|-----------|------|------------|----------|
| Two Pointer / Sliding Window | Longest Substring Without Repeating Characters | 可変長の範囲で条件チェック | 文字列・配列どちらも応用可 |
| Stack / Monotonic Stack | Daily Temperatures, Next Greater Element | 条件を満たすまで積み上げ・消去 | 番兵や条件判定で管理 |
| Divide & Conquer | Longest Common Prefix (Pivot版), Merge Intervals | 配列や文字列を分割して再帰で処理 | Medium～Hardでよく出る |
| Binary Search / Search Space | Search in Rotated Sorted Array | 範囲を半分に絞って探索 | O(log n)の高速探索 |
| Dynamic Programming (DP) | Unique Paths, Climbing Stairs | 部分問題を保存して計算 | Easy→Mediumで段階的に学習 |
| Backtracking | Letter Combinations of a Phone Number | 条件に従って全パターン生成 | Medium問題で頻出 |
| Heap / Priority Queue | Kth Largest Element | 最大/最小の条件で取り出す | Priorityを意識する |
| Graph / BFS / DFS | Number of Islands, Clone Graph | 隣接関係を探索 | Medium～Hardの定番 |

