    # Сортировка с выбором
# def smallest_elem(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = smallest_elem(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr
#
# arr = list(map(int, input().split()))
# print(selectionSort(arr))

# Задачи с Leetcode
#sort colors
#
# def sortColors(nums):
#     newnewArr = []
#     newArr = nums[:]
#     while len(newArr) > 0:
#         smallest = nums[0]
#         smallest_index = 0
#         for j in range(len(newArr)):
#             if newArr[j] < smallest:
#                 smallest = newArr[j]
#                 smallest_index = j
#         newnewArr.append(newArr.pop(smallest_index))
#     nums[:] = newnewArr
#
# nums = list(map(int, input().split()))
# print(sortColors(nums))

# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         j = n - 1
#         for i in range(m + n - 1, -1, -1):
#             if nums1[i] == 0 and j >= 0:
#                 nums1[i] = nums2[j]
#                 if i != 0 and nums1[i - 1] != 0 and nums1[i - 1] > nums1[i]:
#                      nums1[i - 1], nums1[i] = nums1[i], nums1[i - 1]
#                 j -= 1
#
# def merge(nums1, m, nums2, n):
#     i = m - 1
#     j = n - 1
#     k = m + n - 1
#     while j >= 0:
#         if i >= 0 and nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             i -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1
#         k -= 1

# def sortedSquares(self, nums):
#             left = 0
#             right = len(nums) - 1
#             pos = len(nums) - 1  # заполняем с конца
#
#             result = [0] * len(nums)
#
#             while left <= right:
#                 left_sq = nums[left] ** 2
#                 right_sq = nums[right] ** 2
#
#                 if left_sq > right_sq:
#                     result[pos] = left_sq
#                     left += 1
#                 else:
#                     result[pos] = right_sq
#                     right -= 1
#                 pos -= 1
#
#             return result

