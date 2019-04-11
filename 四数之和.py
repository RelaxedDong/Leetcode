class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        from itertools import combinations
        in_stack = []
        for item in combinations(sorted(nums),4):
            if sum(item) == target:
                in_stack.append(item)
        result = []
        for index in range(len(in_stack)):
            result.append(str(in_stack[index]))
        result = list(set(result))
        print(result)
        end = [eval(s) for s in result]
        return end

end = Solution().fourSum([-498,-492,-473,-455,-441,-412,-390,-378,-365,-359,-358,-326,-311,-305,-277,-265,-264,-256,-254,-240,-237,-234,-222,-211,-203,-201,-187,-172,-164,-134,-131,-91,-84,-55,-54,-52,-50,-27,-23,-4,0,4,20,39,45,53,53,55,60,82,88,89,89,98,101,111,134,136,209,214,220,221,224,254,281,288,289,301,304,308,318,321,342,348,354,360,383,388,410,423,442,455,457,471,488,488],-2808)
print(end)

