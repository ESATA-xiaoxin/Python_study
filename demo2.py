# 用   户:张文薪
# 开发时间: 2021/2/15 22:48
print('hello\nworld')#n是newline,意思是换行
print('hello\tworld')#t是Tab，是制表符
print('helloo\tworld')
print('hello\rworld')#r是回车，表示world将hello覆盖
print('hel\rworld')
print('hellooo\rworld')
print('hello\rworrld')
print('hello\bworld')#b指的是退一个格，即删除一个字母，将o退没了
print('hello\b\bworld')
print('hello\n\nworld')
print('hello\r\rworld')
print('hello\rworld\rhi')
print('hello\t\tworld')


print('http:\\www.baidu.com')#输出单斜杠
print('http:\\\\www.baidu.com')#输出双斜杠


print('老师说:\‘大家好\’')#斜杠后中文引号
print('老师说:\'大家好\'')#斜杠后英文引号
print('老师说:’大家好’')
print('老师说:”大家好“')#不用反斜杠时，要用中文的引号

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在 字符串之前加上r或者R
print(r'hello\nworld')#r
print(r'hello\nworld\\')#单反斜杠不行，双反斜杠可以输出
