# class Solution(object):
#第一种
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         mydict = {}
#         for index in range(0,len(strs)):
#             substr = strs[index]
#             str = ""
#             for c in range(0,len(substr)):
#                 str += substr[c]
#                 if str not in mydict:
#                     mydict[str] = 1
#                 else:
#                     mydict[str] += 1
#         Maxlen = 0
#         str = ""
#         for key,value in mydict.items():
#             if value >= Maxlen and len(key)>len(str):
#                 str = key
#                 Maxlen = value
#         return str if len(strs) == Maxlen else ''
#
# end = Solution().longestCommonPrefix(["flower","flow","flight"])
# print(end)

#第二种
# def longestCommonPrefix(strs):
#     if not strs:return ""
#     str = list(map(set,zip(*strs)))
#     result = ""
#     for s in str:
#         s = list(s)
#         if len(s) > 1:
#             break
#         result = result+s[0]
#     return result


#第三种
# def longestCommonPrefix(strs):
#     if not strs: return ""
#     s1 = min(strs)
#     s2 = max(strs)
#     for i,x in enumerate(s1):
#         if x != s2[i]:
#             return s2[:i]
#     return s1
#
# s = longestCommonPrefix(["falower","flow","flight"])
