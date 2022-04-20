# 用   户:张文薪
# 开发时间: 2021/2/16 11:05
a=3.14159
print(a,type(a))
print(1.1+2.2)
print(1.1+2.1)
n1=1.1
n2=2.2
print(n1+n2)

from decimal import Decimal#from后小写，import后大写
print(Decimal('1.1')+Decimal('2.2'))


print(Decimal(n1+n2))#错误的