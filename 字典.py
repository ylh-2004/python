# 字典：python中重要的数据类型，字典是有 键值对 组成的集合，通常使用键来访问数据，效率高，和list一样支持对数据的增、删、改、查
# 特点：
# 1.不是序列类型，没有下标的概念，是一个无序的 键值 集合，是内置的高级数据类型
# 2.用{}来表示字典对象，每个键值用逗号分割
# 3.键 必须是不可变的类型（eg：元组，字符串）值可以是任意类型
#4.每个键必定是唯一的，如果存在重复的键，后者会覆盖前者

 #如何创建字典
d1={'pro':'artist','school':'htu'}#empty dictation
# #添加字典数据
d1['number']="234"
d1['pos']='singer'
d1['age']="78"
# #结束添加
# print(type(d1))
# print(d1)
# print(len(d1))
#
# #seek操作
# #通过键获取对应的值
# print(d1['school'])
#
# #修改键对应的值
# d1['pos']='drawer'
# print(d1)

#获取左右的键
# print(d1.keys())
#获取所有的值
# print(d1.values())
#获取所有的数据项-----键和值
# print(d1.items())
# for key,value in d1.items():
#     print('%s=%s' %(key,value))

#修改数据,可以修改和添加
# d1.update({'age':3})
# d1.update({'heiht':890})
# print(d1)

#删除操作
# print(d1)
# del d1['school']
# print(d1)
# d1.pop('number')
# print(d1)

#排序字典，利用sorted函数，按照key或者value排序
print(d1)
s = sorted(d1.items(),key=lambda d:d[0])
m = sorted(d1.items(),value=lambda d:d[1])
print(s)
print(m)
