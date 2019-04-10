mydict = {}
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #第二种  存储字典
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # else:
        #     if n and n-1 in mydict:
        #         s1 = mydict.get(n-1)
        #         s2 = mydict.get(n-2)
        #     else:
        #         s1 = self.climbStairs(n - 1)
        #         s2 = self.climbStairs(n - 2)
        #         mydict[n-1] = s1  #保存在字典中
        #         mydict[n-2] = s2
        #     return s1+s2

        #第一种
        #return self.climbStairs(n-1)+self.climbStairs(n-2) # 递归，会超时

        # 第三种：  斐波那契数列
        a, b = 1, 1
        while n - 1:
            a, b = b, a + b
            n -= 1
        return b

s = Solution().climbStairs(30) #1346269

print(s)
