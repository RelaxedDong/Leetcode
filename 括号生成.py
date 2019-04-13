class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        res = []
        self.generate(n, n, "", res)
        return res

    def generate(self, left, right, str, res):
        print(str)
        if left == 0 and right == 0:
            res.append(str)
            return
        if left > 0:
            self.generate(left - 1, right, str + '(', res)
        if right > left:
            self.generate(left, right - 1, str + ')', res)
