#list非常重要的数据结构
# 特点：
# 1.支持增删改查
# 2.数据类型可变
# 3.用[]表示数据间用逗号来分割
from operator import index

# list[start:end:step]
# list1 =[1,2,3,4]
#list.append()表示在列表后面追加一个列表
# list1.append([5,6,7])
# #insert插入
# list1.insert(1,"这是我刚加的")
# print(list1)
# rs=list(range(5))#强制转换成list对象
# list1.extend(rs)#拓展  等于批量添加
# print(list1)
# print(rs)

#修改列表的数据
# list1[0]="hi"
# print(list1)

#删除
list2=list(range(10,40))
# print(list2)
# del list2[:6] #删除只能删除一个或者1到几，不能选择删除
# print(list2)

# remove 移除指定元素
# list2.remove(10)
# print(list2)

# pop移除指定项的索引值
# list2.pop(3)
# print(list2)

# index函数
#返回索引下标
print(list2.index(13,1,9))#后两个数据都是用的索引值，下标值

#len函数获取列表对象中的数据个数