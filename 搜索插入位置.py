#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/12 14:27


# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index in range(len(nums)):
            if nums[index] == target:
                return index
            else:
                try:
                    if nums[index] < target < nums[index + 1]:
                        return index + 1
                except:
                    return index + 1
        return 0
result = Solution().searchInsert([1,3,5,6], 0)
print(result)