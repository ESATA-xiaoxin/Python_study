# 用   户:张文薪
# 开发时间: 2021/2/18 22:25
'''多分支结构，多选一执行
从键盘录入一个整数 成绩
90-100  A
80-89   B
70-79   C
60-69   D
0-59    E
小于 0或大于 100为非法数据（不是成绩的有效范围）
'''
score=int(input('请输入成绩:'))
if score>=90 and score<=100:
#可以写成 if 90<=score<=100，这样更方便
    print('A级')
elif score>=80 and score<=89:
    print('B级')
elif score>=70 and score <80:
    print('C级')
elif score>=60 and score<70:
    print('D级')
elif score>=0 and score<=59:
    print('E级')
else:
    print('对不起，成绩有误，不在有效范围内')