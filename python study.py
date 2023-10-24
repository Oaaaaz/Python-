Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=1
A=2
print(a,A)
1 2
print(1/3)
0.3333333333333333
if a==1:
    print('YES!')

    
YES!
//数据类型
SyntaxError: invalid syntax
/数据类型
SyntaxError: invalid syntax
#数据类型
#list
x=[1,2,3,4,5,1]
print(x)
[1, 2, 3, 4, 5, 1]
x[0:2]
[1, 2]
#x[0,2]==x[:2]->0,1元素
x[2:]
[3, 4, 5, 1]
#左侧包括，右侧也包括
x[2:-1}#最右侧少一个
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
x[2:-1]
[3, 4, 5]
x[2]
3
x[2:3]
[3]
#String
#字符串会被理解为单个字符构成的特殊list
type("早上好")
<class 'str'>
"早上好"[0]
'早'
#元组(tuple)有顺序，可重复，不可修改。
y=(1,2,3,1)
print(y)
(1, 2, 3, 1)
y[2]
3
y[2,-1]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    y[2,-1]
TypeError: tuple indices must be integers or slices, not tuple
y[1,-1]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    y[1,-1]
TypeError: tuple indices must be integers or slices, not tuple
y[2:-1]
(3,)
y(2)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    y(2)
TypeError: 'tuple' object is not callable
#集合set
#集合无序，无索引，无重复。
z=set(x)
z
{1, 2, 3, 4, 5}
#set由list转移而来
z[2]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    z[2]
TypeError: 'set' object is not subscriptable
#集合里无位置，无索引。
#判断
2 in z
True
10 in z
False
10 not in z
True
#词典（Dictionary）无序，有索引，可修改，可重复。键名必须是常数，不重复，键值可以是变量。
d={'a':10,'b':2,'c':x}
d
{'a': 10, 'b': 2, 'c': [1, 2, 3, 4, 5, 1]}
d['a']
10
a
1
#字典里键名的数值定义不影响词典外的值。
'a' in d
True
c='新值'
d['c']
[1, 2, 3, 4, 5, 1]
#词典外的数值定义也不影响词典里的值。
d['c'][:2]
[1, 2]
print（c)
SyntaxError: invalid character '（' (U+FF08)
print (c)
新值
#选择分支if else
if a==1:
    print(YES!)
    
SyntaxError: invalid syntax
if a==1:
    print('YES!')

    
YES!
a ==2
False
a =2
if a==1:
    print('YES!')
else:
    print('NO!')

    
NO!
#For/While
for x in "早上好"
SyntaxError: incomplete input
for x in "早上好"
SyntaxError: incomplete input
for x in ["早上好"]
SyntaxError: incomplete input
for x in "早上好":
    print(x)

    
早
上
好
#string处理方式等同list
for x in["早上好","中午好","晚上好"]:
    print(x)

    
早上好
中午好
晚上好
for x in["早上好","中午好","晚上好"]:
    for y in x:
        print(y,end=" ")#end
        print("")#""空字符 表示换行

        
早 
上 
好 
中 
午 
好 
晚 
上 
好 
for x in["早上好","中午好","晚上好"]:
    for y in x:
        print(y,end=" ")

        
早 上 好 中 午 好 晚 上 好 
for x in["早上好","中午好","晚上好"]:
    for y in x:
        print(y,end=" ")
    print("")

    
早 上 好 
中 午 好 
晚 上 好 
#缩进表示代码的级别
for x in["早上好","中午好","晚上好"]:
    for y in x:
        print(y)

        
早
上
好
中
午
好
晚
上
好
#while
x=1
while <5:
    
SyntaxError: invalid syntax
while x<5:
    print(x)
    x+=1

    
1
2
3
4
#函数
def fun1():#def
    print('调用函数')
fun1()
SyntaxError: invalid syntax
fun1()
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    fun1()
NameError: name 'fun1' is not defined
def fun1():
    print('调用函数')

    
fun1()
调用函数
def fun2(var):
    b=var*2
    return b

a=1
fun2(a)
2
#无return语句时默认返回最后一句赋值 fun1返回null
#错误处理
#try except else
# try:需要进行错误捕获的代码段
# except:出错后需要执行的代码段
# else:没有出错时需要执行的代码段
a=None#删除变量a
a=a+1
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    a=a+1
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
try:
    a=a+1
except:
    print("wrong!")

    
wrong!
try:
    a=a+1
except Exception as e:#更常用的写法
    print(e)          #python中在想要输出字符串时print括号里加引号

    
unsupported operand type(s) for +: 'NoneType' and 'int'
try:
    a+=1
except:
    pass
#pass 使这段代码无输出 无报错
a=None
SyntaxError: invalid syntax

a=None
a=a.astype(int)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    a=a.astype(int)
AttributeError: 'NoneType' object has no attribute 'astype'
a=a.astype('int')
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    a=a.astype('int')
AttributeError: 'NoneType' object has no attribute 'astype'
exception TypeError as e:
    
SyntaxError: invalid syntax
exception TypeError as e:
    
SyntaxError: invalid syntax
except TypeError as e:
    
SyntaxError: invalid syntax
except TypeError as e:
    
SyntaxError: invalid syntax
try :
    a=a.astype(int)
except TypeError as e:
    print(e)
except:
    pass

>>> 
>>> 
>>> a=None
>>> try :
...     a=a.astype(int)
... except TypeError as e:
...     print(e)
... except:
...     pass
... 
>>> 
>>> a=None
>>> a=a.astype(int)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    a=a.astype(int)
AttributeError: 'NoneType' object has no attribute 'astype'
>>> try :
...     a=a.astype(int)
... except TypeError as e:
...     print(e)
... except:
...     pass
... try :
...     a=a.astype(int)
... except TypeError as e:
...     print(e)
...     
SyntaxError: invalid syntax
>>> try :
...     a=a.astype(int)
... except TypeError as e:
...     print(e)
... except:
...     print("new error")
... 
...     
new error
>>> #Why Pandas
