"""
数据类型作业
1.下面集合的定义正确的是： C
A. s = {}
B. s = {1,2,['a']}
C. s = {1,2,('a',)}
D. s = {1 2 3}
解题思路:A.创建一个空集合方法:s = set()
        B.集合里不可以放list,list是可变类型
        C.是集合
        D.集合是用{}括起来的，并使用逗号来分隔



2.下面关于字典的定义正确的是：  C
A. d = {1,}
B. d = {1,2:3,4}
C. d = {'name':'xinlan','age':18}
D. d = {[1,2]:[3,4],'age':18}
解题思路:A.是集合
        B.没有2：3这种写法
        C.是字典
        D.key不能是list,不能是可变类型


3.请创建一个字典用来表示你自己的个人信息
personal_information = {'name':'GY','age':'24','sex':'男','height':'179','weight':'75kg'}
print(personal_information)



4.下面代码的正确结果是   C
a = 1
b = '2'
a < b

A. True
B. False
C. 报错
解题思路：a是整型int，b是字符串，二者无法比较


5.下面代码正确的结果是   A
s = 'abcdef'
'ac' not in s

A. True
B. False
解题思路：ac是个整体，s中没有ac


6.下面代码正确的结果是  C
True + 1

A. True
B. False
C. 2
D. 报错
解题思路：bool是int的子类,True和False也就可以进行运算，True==1，False==0


7. 下面的表达式的结果是
a = 0
b = 1
a and b or b

A. True
B. False
C. 1
D. 0
解题思路：逻辑运算输出数值，比较运算输入bool
        and:有假则假，都为真，选后者；都为假，选前者
        or：有真则真，；都为真，选前者；都为假，选后者
"""

a = 1
b = 2
print(1 and 2)

c = 0
d = 1
print(c and d)