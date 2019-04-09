import itertools 
from functools import reduce 
l=[] 
l1=[-1,0,1,2,-1,-4] 
m=list(itertools.combinations(l1,3)) #为了拿出所有的三元组 数学组合 
lis=[]#用来添加目标列表 
for n in m: 
    b=reduce(lambda x,y:x+y, n)#题干要求求和
    if b==0:
        if sorted(n) not in lis:#这一步是为了去掉重复的元素
            lis.append(sorted(n))#题意答案
        else:
            continue
