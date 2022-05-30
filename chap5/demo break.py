# 用   户:张文薪
# 开发时间: 2021/2/20 12:05

'''流程控制语句break与continue在二重循环中的使用'''
for i in range(5):
    for j in range(1,11):
        if j%2==0:
           continue  # break
        print(j,end='\t')
    print()