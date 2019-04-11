# -*- coding: utf8 -*-
charactors = {'}': '{', ']': '[', ')': '(', '>': '<'}

CharLeft = charactors.values()
CharRight = charactors.keys()

def check(s):
    LeftStack = []
    for c in s:
        if c in CharLeft:
            LeftStack.append(c)
        elif c in CharRight:
            if LeftStack and LeftStack[-1] == charactors[c]:
                LeftStack.pop()
            else:
                return False
    return True

print(check("3 * {3 +[(2 -3) * (4+5)]}"))
print(check("3 * {3+ [4 - 6]"))