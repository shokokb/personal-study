# -*- coding: utf-8 -*-
import bubble

# Bubble Sort

if __name__ == "__main__":
    # 右からのバージョン（アルゴリズム図鑑）
    list = [5, 9, 3, 1, 2, 8, 4, 7, 6]
    bubble.BubbleSort.sort(list)
    print(list)

    # 左からのバージョン
    list = [5, 9, 3, 1, 2, 8, 4, 7, 6]
    bubble.BubbleSort.sort_from_left(list)
    print(list)
