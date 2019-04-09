class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        x = str(x)
        if x.startswith('-'):
            y = x[:0:-1]
            y = "-"+y
        else:
            y = x[::-1]
        index = 0
        for i in y:
            if i == str(0):
                index += 1
            elif i != str(0) and i!='-':
                break
        y = y.replace('0', '', index)
        return y if -2147483648 < int(y) < 2147483647 else 0

end = Solution().reverse(-10)
print(end)
