#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/10 13:42

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mydict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rseult = 0
        for index in range(0,len(s)-1):
            if mydict[s[index]]<mydict[s[index+1]]:
                rseult -= mydict.get(s[index])
            else:
                rseult += mydict.get(s[index])
        rseult += mydict.get(s[-1])
        return rseult


Solution().romanToInt('MCMXCIV')

