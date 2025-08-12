# coding: utf-8

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1 # 6
    while left <= right:
        mid = (left + right) // 2 # 3
        # [1, 3, 5], 7, [9, 11, 13]
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    numbers = [1, 3, 5, 7, 9, 11, 13]   # n = 7
    print(binary_search(numbers, 7))   # 出力: 3
    print(binary_search(numbers, 4))   # 出力: -1

if __name__ == "__main__":
    main()