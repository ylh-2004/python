# t = "python"
# print(type(t))
# print('获取第一个字符：%s' %t[0])


# for i in t :
#     print(i,end=" ")


# #姓名首字母大写 就是正常引用加(.函数)
# print("首字母大写: %s" %t.capitalize())


# #移除左右两边的空格  #限定左or右空格
# a ='      hello    '
#b=a.strip()
# # b=a.lstrip()
# b=a.rstrip()
# print(b)


#查找字符串:找找数据，并且知道他在哪里，只要找到一个就返回值
#如果没有找到就返回（-1)
#index函数查找返回的也是下标,没有找到就报错
# d ='I LOve PYthon'
# print(d.find('m'))
# print(d.index('m'))
# print(d.startswith('I'))
# print(d.endswith('m'))
# print(d.lower())
# print(d.upper())


#切片 slice[start:end:step]左闭右开，左包含右不包含
c = 'hello world'
print(c)
print(c[0])
print(c[2:6:1])
print(c[2:])
#0可以省略掉
print(c[:4])
#倒序输出，符号表示方向，从右向左
print(c[::-1])