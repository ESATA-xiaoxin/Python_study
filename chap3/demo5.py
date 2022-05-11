# 用   户:张文薪
# 开发时间: 2021/2/17 18:02

#比较运算符,比较运算符的结果为bool类型
a,b=10,20
print('a>b吗？',a>b)
print('a<b吗？',a<b)
print('a<=b吗？',a<=b)
print('a>=b吗？',a>=b)
print('a==b吗？',a==b)
print('a!=b吗？',a!=b)

'''一个 = 称为赋值运算符， == 称为比较运算符
一个变量由三部分组成，标识，类型，值
== 比较的是值还是标识呢？比较的是值
  比较对象的标识使用 is
'''
a=10
b=10
print(a==b)  #True,说明a与b的value相等
print(a is b)  #True,说明a与b的id标识相等

#以下代码没学过，后面会有讲解
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)
print(lst1 is lst2)
print(id(lst1))
print(id(lst2))

print(a is not b)
print(lst1 is not lst2)