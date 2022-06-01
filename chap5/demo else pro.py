# 用   户:张文薪
# 开发时间: 2021/2/20 9:37
a=0
while a<3:
    pwd=input('请输入密码:')
    if pwd=='888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a+=1
else:
    print('账户已被锁定')