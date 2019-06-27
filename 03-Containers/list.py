Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L=[]
>>> type(L)
<class 'list'>
>>> bool(L)
False
>>> a=list()
>>> a
[]
>>> a=list(1,2,3)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a=list(1,2,3)
TypeError: list expected at most 1 arguments, got 3
>>> a=list({1,2,3,4})
>>> a
[1, 2, 3, 4]
>>> type(a)
<class 'list'>
>>> bool(a)
True
>>> L=[10,20,30[150,200],40,50,[250,300]]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    L=[10,20,30[150,200],40,50,[250,300]]
TypeError: 'int' object is not subscriptable
>>> L=[10,20,30[150,200],40,50,[250,300]]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    L=[10,20,30[150,200],40,50,[250,300]]
TypeError: 'int' object is not subscriptable
>>> L=[10,20,30[150,200]]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    L=[10,20,30[150,200]]
TypeError: 'int' object is not subscriptable
>>> L=[11,22,33,[111,222,333]]
>>> 
>>> l[0]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l[0]
NameError: name 'l' is not defined
>>> L[0]
11
>>> L=[10,20,30,[150,200,250],40,50]
>>> L[-1]
50
>>> L[-3]
[150, 200, 250]
>>> L[3]
[150, 200, 250]
>>> L[2]
30
>>> len(L)
6
>>> K[15,25,35,[300],45,55]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    K[15,25,35,[300],45,55]
NameError: name 'K' is not defined
>>> K=[15,25,35,[300],45,55]
>>> J=L+K
>>> print(J)
[10, 20, 30, [150, 200, 250], 40, 50, 15, 25, 35, [300], 45, 55]
>>> len(L+K)
12
>>> K*3
[15, 25, 35, [300], 45, 55, 15, 25, 35, [300], 45, 55, 15, 25, 35, [300], 45, 55]
>>> 20 in L
True
>>> 20 in K
False
>>> 20 in J
True
>>> K==L
False
>>> A=[9,8,7,6,5,4,3,2,1]
>>> B=[1,2,3,4,5,6,7,8,9]
>>> A==B
False
>>> C=[99,88,77,66]
>>> D=[99,88,77,66,55]
>>> C==D
False
>>> C=[99,88,77,66]D=[99,88,77,66,55]
SyntaxError: invalid syntax
>>> C=[99,88,77,66]
>>> D=[99,88,77,66]
>>> C==D
True
>>> A>B
True
>>> A<B
False
>>> B>A
False
>>> print(A)
[9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> A.append(0)
>>> print(A)
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> A.insert(-1,-2)
>>> print(A)
[9, 8, 7, 6, 5, 4, 3, 2, 1, -2, 0]
>>> A.insert(-1,-1)
>>> print(A)
[9, 8, 7, 6, 5, 4, 3, 2, 1, -2, -1, 0]
>>> A.extend(10)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    A.extend(10)
TypeError: 'int' object is not iterable
>>> A.extend(1)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    A.extend(1)
TypeError: 'int' object is not iterable
>>> A.extend(10)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    A.extend(10)
TypeError: 'int' object is not iterable
>>> A.extend[10]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    A.extend[10]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> A.extend[{10}]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    A.extend[{10}]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> A.reverse()
>>> 
>>> A.reverse()
>>> print(L)
[10, 20, 30, [150, 200, 250], 40, 50]
>>> L.reverse()
>>> print(L)
[50, 40, [150, 200, 250], 30, 20, 10]
L[0]
50
>>>
