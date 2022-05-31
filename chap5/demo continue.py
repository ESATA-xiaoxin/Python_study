# 用   户:张文薪
# 开发时间: 2021/2/20 9:07

'''要求输出1到50之间所有5的倍数'''
'''a=1
while a<=50:
    if a%5==0:
        print(a)
    a+=1'''
for item in range(1,51):
    if item%5!=0:
        continue
    else:
        print(item)