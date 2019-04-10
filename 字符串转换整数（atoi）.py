# encoding:utf8

def myreturn(strip_str):
    try:
        strip_str = int(strip_str)
        if isinstance(strip_str, int):
            if -2147483648 < strip_str < 2147483647:
                return strip_str
            if strip_str<-2147483648:
                return -2147483648
            if strip_str > 2147483648:
                return 2147483648
    except:
        pass


class Solution(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        if len(string) == 0:
            return 0
        try:
            if isinstance(int(string), int):
                return myreturn(string)
        except:
            if 'a'<string[0]<'z' or 'A' < string[0] < 'Z':
                return 0

        strip_str = ""
        for s in string:
            if s != " ":
                strip_str += s
        sub = ''
        pre = ""
        if strip_str.startswith('-'):
            pre = "-"
            if isinstance(strip_str[1], str):
                return 0

        try:
            if not isinstance(int(strip_str[1]), int) or strip_str.startswith('.'):
                return 0
        except:
            if "." in strip_str:
                re = strip_str.split('.')
                print(re)
                if int(re[0]) == 0:
                    return re[1]
                return re[0]
        for s in strip_str:
            try:
                if isinstance(int(s), int):
                    sub += s
                else:
                    break
            except:
                pass
        strip_str = pre + sub
        return myreturn(strip_str)



s = Solution().myAtoi("-91283472332")
print(s)




