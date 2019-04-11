class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mydict = {'}':'{','>':'<',')':'(',']':'['}

        keys = mydict.keys()
        values = mydict.values()

        instack = []
        for r in s:
            if r in values:
                instack.append(r)
            elif r in keys:
                if instack and instack[-1] == mydict[r]:
                    instack.pop()
                else:
                    return False
        return False if instack else True


if __name__ == '__main__':
    mystr = '{}'
    result = Solution().isValid(mystr)
    print(result)