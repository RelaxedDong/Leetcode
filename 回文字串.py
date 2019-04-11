#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/9 20:30

def func(mystr):
    length = len(mystr)
    mylist = []
    for i in range(0,length-2):
        for j in range(i+1,length):
            newstr = mystr[i:j+1] #切出新的字符串
            midlength = len(newstr) // 2
            for k in range(0,midlength):
                if newstr[k]!=newstr[len(newstr)-k-1]:
                    break
            else:
                mylist.append(newstr)
                #是回文
    maxlength = 0
    for item in mylist:
        if len(item) > maxlength:
            maxlength = len(item)
    return maxlength
mystr='aacecaaa'

length = func(mystr)
print(length)
























