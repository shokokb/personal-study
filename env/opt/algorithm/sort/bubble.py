# -*- coding: utf-8 -*-
class BubbleSort:
    @staticmethod
    def sort(list):

        # BubbleSortの場合、隣り合う2項目を比較する
        idx_r = len(list) - 1
        idx_l = idx_r - 1
        idx_min = 0
        while idx_min < len(list):
            while idx_l >= 0:
                if (list[idx_r] < list[idx_l]):
                    list[idx_r], list[idx_l] = list[idx_l], list[idx_r]
                # 左端・右端をずらす
                idx_r += -1
                idx_l += -1
            # 右端に戻る
            idx_r = len(list) - 1
            idx_l = idx_r - 1
            # 確定要素を１つ右にずらす
            idx_min += 1

    # 左端からソート
    # 右端に最大が来る
    def sort_from_left(list):
        idx_l = 0
        idx_r = idx_l + 1
        idx_max = len(list)
        while (idx_max >= 0):
            while (idx_r < len(list)):
                if (list[idx_l] > list[idx_r]):
                    list[idx_l], list[idx_r] = list[idx_r], list[idx_l]
                # １つずつ右にずらす
                idx_l += 1
                idx_r += 1
            # 先頭に戻り、確定位置を１つ左に移す
            idx_max -= 1
            idx_l = 0
            idx_r = idx_l + 1
            # 右端に最大が来る

if __name__ == "__main__":
    list = [5, 9, 3, 1, 2, 8, 4, 7, 6]
    BubbleSort.sort(list)
    print(list)

    list = [5, 9, 3, 1, 2, 8, 4, 7, 6]
    BubbleSort.sort_from_left(list)
    print(list)
