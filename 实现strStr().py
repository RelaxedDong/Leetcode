# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         if not haystack and not needle:
#             return 0
#         if not needle:
#             return 0
#         if needle == haystack:
#             return 0
#         mydict = {}
#         for x in range(len(haystack)):
#             raw = haystack[x]
#             if raw not in mydict:
#                 mydict[raw] = x
#             for y in range(x+1,len(haystack)):
#                 raw += haystack[y]
#                 if raw not in mydict:
#                     mydict[raw] = x
#         return mydict[needle] if needle in mydict.keys() else -1
#
#
# result = Solution().strStr(haystack = "aaaaa", needle = "bba")
#
# print(result)
#
