""" 第一种
class Solution(object):
    def removeDuplicates(self, nums):
        "
        :type nums: List[int]
        :rtype: int
        "
        count = 1
        for x in range(len(nums)-1):
            if nums[x] != nums[x+1]:
                count +=1
        print(count)
        #return nums
"""


""" 第二种
class Solution:
    def removeDuplicates(self, nums):
        "
        :type nums: List[int]
        :rtype: int
        "
        for i in range(len(nums)-1,0,-1):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i-1])
        print(nums)"""

if __name__ == '__main__':
    #Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4,5,5,5,5,5,6])
