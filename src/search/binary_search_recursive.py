# coding: utf-8

# TimeComplexity : O(logN)
def binary_search_recursive(arr, target, left, right):
    if left <= right:
        mid = (left + right) // 2 # 3
        # [1, 3, 5], 7, [9, 11, 13]
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)
    return -1

def main():
    numbers = [1, 3, 5, 7, 9, 11, 13]   # n = 7
    n = len(numbers) - 1
    print(binary_search_recursive(numbers, 7, 0, n))   # 出力: 3
    print(binary_search_recursive(numbers, 4, 0, n))   # 出力: -1

if __name__ == "__main__":
    main()