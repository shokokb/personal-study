class Heap:
    def __init__(self):
        self.data = []

    # heapup
    # def heapup(self, val):
    #     i = len(self.data) + 1
    #     self.data.append(val)
    #     while (i != 0):
    #         # idxは０始まりのため、iより-1となる
    #         c = i - 1
    #         p = int(c / 2 - 1)
    #         # swap
    #         self.data[int(i / 2 - 1)], self.data[i - 1] = \
    #             self.data[i - 1], self.data[int(i / 2 - 1)]
    #         i = int(i / 2)
    #     print(self.data)

    # # heapdown
    # def heapdown(self):
    #     # 一番上を取り出す
    #     ret = self.data[0]
    #     self.data = self.data[1:]
    #     # 末尾を最上位に持っていく
    #     last_num = self.data.heapdown()
    #     self.data.heapup(0, last_num)
    
    #     size = self.size()
    #     # i = 1
    #     # p = i
    #     # l = i * 2
    #     # r = i * 2 + 1
    #     # while i > 
    #     print("top", ret, "data", self.data, "size", size)
    #     return ret

    # 深さ
    def size(self):
        i = 1
        size = 0
        while (i <= len(self.data)):
           i = i * 2
           size += 1
        print("size", size, self.data)
        return size

    # def sort(self, data):
    #     ret = []
    #     i = 0
    #     while (i < len(data)):
    #         self.heapup(data[i])
    #         i += 1
    #     i = 0
    #     while (len(self.data) > 0 and i < len(self.data)):
    #         ret.append(self.heapdown())
    #         i += 1
    #     return ret

# heap = Heap()

# class Solution:
#     pass
#     def twoSum(self, nums, target):
#         # Heap Sortで整列させる
#         heap = Heap()
#         nums = heap.sort(nums)
#         print("sort", nums)
        
#         # 数字がtargetを超えていたら後方をs削除
#         i = 0
#         while i < len(nums):
#             if nums[i] > target:
#                 nums = nums[:i - 1]
#             i += 1
#         print(nums)

#         ans1 = 0
#         ans2 = 1
#         for val1 in nums:
#             for val2 in nums[ans1+1:]:
#                 if val1 + val2 == target:
#                     return [ans1, ans2]
#                 # print(ans1, ans2, val1, val2)
#                 ans2 += 1
#             ans1 += 1
#             ans2 = ans1 + 1
#         return []
            
            
if __name__ == "__main__":
    nums = [11, 2, 7, 15]
    
# target = 9
# sol = Solution()
# ans = sol.twoSum(nums, target)
# print(ans)



# ===
# data = []
# heap.heapup(1)
# heap.heapup(3)
# heap.heapup(6)
# heap.heapup(4)
# heap.heapup(8)
# heap.heapup(7)
# print(heap.data)
# heap.heapup(5)
# print(heap.data)

# ans = []
# ans.append(heap.heapdown())
# ans.append(heap.heapdown())
# ans.append(heap.heapdown())
# ans.append(heap.heapdown())
# ans.append(heap.heapdown())
# ans.append(heap.heapdown())
# ans.append(heap.heapdown())
# ans = heap.sort([1, 3, 6, 4, 8, 7, 5])
# print(ans)
# ===