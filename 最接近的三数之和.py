class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        minDiff = 1000
        result = 0
        diff = 0
        sum = 0
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                diff = abs(target - sum)
                if diff == 0:
                    return sum

                if diff < minDiff:
                    minDiff = diff
                    result = sum

                if sum>target:
                    k-=1
                else:
                    j+=1
        return result




if __name__ == '__main__':
    a = Solution().threeSumClosest([-1,2,1,-4],target=1)
    print(a)