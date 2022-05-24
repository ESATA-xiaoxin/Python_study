# 用   户:张文薪
# 开发时间: 2021/2/18 23:13
'''会员  >=200  8折
        >=100  9折
       100以下  不打折
  非会员  >=200  9.5折
        200以下 不打折'''
answer=input('您是会员吗？Y/N')
money=float(input('请输入您的购物金额：'))
#外层判断是否是会员
if answer=='Y':  #会员
    if money>=200:
        print('打八折，您的付款金额为:',money*0.8)
    elif money>=100:
        print('打九折，您的付款金额为:',money*0.9)
    else:
        print('不打折，您的付款金额为:',money)
else:  #非会员
    if money>=200:
        print('打9.5折，您的付款金额为:',money*0.95)
    else:
        print('不打折，，您的付款金额为:',money)