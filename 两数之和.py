#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/19 13:29

"""
定给一个整数数组nums 状语从句：一个目标值target，请在你该数组中找出状语从句：为目标值的那  两个  整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例：

给定nums = [2,7,11,15]，目标= 9

因为nums [ 0 ] + nums [ 1 ] = 2 + 7 = 9
所以返回[ 0,1 ]
"""

#解法1
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         result = []
#         for x in range(len(nums)-1):
#             for y in range(x+1,len(nums)):
#                 if nums[x] + nums[y] == target:
#                     result = [x,y]
#         print(result)
#         return result
# Solution().twoSum([2,7,11,15],9)
# Solution().twoSum([2,5,5,11],10)



# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         d = {}
#         for index in range(len(nums)):
#             current = target - nums[index]
#             if nums[index] in d:
#                 return d[nums[index]],index
#             else:
#                 d[current] = index
#
# s1 =  Solution().twoSum([2,7,11,15],9)
# s2 =  Solution().twoSum([2,5,5,11],10)
