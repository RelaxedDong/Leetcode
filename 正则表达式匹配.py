#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/5 16:32

class Solution:
    def isMatch(self, str , regx):
        isregx = False
        for index,s in enumerate(str):
            if s == regx[index] or regx[index]=="*" or regx[index]==".":
                isregx = True
        return isregx

s = Solution()
mystr = 'aab'
p = 'a*'
result = s.isMatch(mystr,p)
print(result)