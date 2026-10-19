# def count_new(arr):
#     if arr == []:
#         return 0
#     else:
#         return 1 + count_new(arr[1:])
#
# print(sum_new([1,2,3,4,5]))
from numpy.ma.core import greater


# def sum_new(arr):
#     if arr == []:
#         return 0
#     else:
#         return 1 + sum_new(arr[1:])
#
# print(sum_new([1,2,3,4,5]))

# def max_new(arr):
#     if len(arr) == 2:
#         return arr[0] if arr[0] > arr[1] else arr[1]
#     sub_max = max_new(arr[1:])
#     return arr[0] if arr[0] > sub_max else sub_max
#
# print(max_new([1,2,3,4,5]))

# def quicksort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [i for i in arr[1:] if i <= pivot]
#
#         greater = [i for i in arr[1:] if i > pivot]
#
#         return quicksort(less) + [pivot] + quicksort(greater)
#
# print(quicksort([5, 4, 3, 2, 1]))

# class Solution(object):
#     def sortArray(self, nums):
#         if len(nums) < 2:
#             return nums
#         pivot = nums[len(nums) // 2]
#         less = [i for i in nums if i < pivot]
#         equal = [x for x in nums if x == pivot]
#         greater = [i for i in nums if i > pivot]
#         return self.sortArray(less) + equal + self.sortArray(greater)