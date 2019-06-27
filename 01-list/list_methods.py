Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [5,10,15,20]
>>> b = [10,20,,15,5]
SyntaxError: invalid syntax
>>> a = [5,10,15,20]
>>> b = [10,20,15,5]
>>> a==b
False
>>> c=(5,10,15,20)
>>> d=(15,20,10,5)
>>> c==d
False
>>> a = [5,10,15,20]
>>> b = [5,10,15,20]
>>> a==b
True
>>> A=[10,20]
>>> B=[25,30]
>>> A>B
False
>>> B>A
True
>>> A=[10,20]
>>> B=[5,25,30]
>>> A>B
True
>>> B>A
False
>>> A=[25,30,35,40,45]
>>> A.append(0)
>>> print(A)
[25, 30, 35, 40, 45, 0]
>>> A.append(0,5)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    A.append(0,5)
TypeError: append() takes exactly one argument (2 given)
>>> A.insert(0,5)
>>> print(A)
[5, 25, 30, 35, 40, 45, 0]
>>> A.insert[-1,50]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    A.insert[-1,50]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> A.insert(-1,55)
>>> print(A)
[5, 25, 30, 35, 40, 45, 55, 0]
>>> print(A)
[5, 25, 30, 35, 40, 45, 55, 0]
>>> 
>>> B=[9,16,24]
>>> B.extend(0)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    B.extend(0)
TypeError: 'int' object is not iterable
>>> B.extend(9)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    B.extend(9)
TypeError: 'int' object is not iterable
>>> 
>>> 
>>> a=['kash',26,'om',13]
>>> b=[3,4,5]
>>> a.extend(b)
>>> print(a)
['kash', 26, 'om', 13, 3, 4, 5]
>>> c=['nandu',24,'kash',26]
>>> d=['rekha',02,'sudhir',12]
SyntaxError: invalid token
>>> c=['nandu',24,'kash',26]
>>> d=['rekha',2,'sudhir',12]
>>> d.extend(c)
>>> print(c)
['nandu', 24, 'kash', 26]
>>> print(d)
['rekha', 2, 'sudhir', 12, 'nandu', 24, 'kash', 26]
>>> 
>>> 
>>> c=['nandu',24,'kash',26]
>>> d=['rekha',2,'sudhir',12]
>>> 
>>> 
>>> 
>>> 
>>> language['java','python','php','.net',5,10,15]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    language['java','python','php','.net',5,10,15]
NameError: name 'language' is not defined
>>> language=['java','python','php','.net',5,10,15]
>>> language.remove('python')
>>> print(language)
['java', 'php', '.net', 5, 10, 15]
>>> 
>>> x=[10,20,30,40]
>>> x.remove(10,20)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    x.remove(10,20)
TypeError: remove() takes exactly one argument (2 given)
>>> x.remove(15)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    x.remove(15)
ValueError: list.remove(x): x not in list
>>> x.remove(10)
>>> print(x)
[20, 30, 40]
>>> 
>>> 
>>> k = ['a', 'e', 'i',  'o', 'u']
>>> k.count("i")
1
>>> k.count("u")
1
>>> k.count("m")
0
>>> k = ['a', 'e', 'i',  'o', 'u']
>>> k.pop(0)
'a'
>>> print(k)
['e', 'i', 'o', 'u']
>>> k.pop(-1)
'u'
>>> print(k)
['e', 'i', 'o']
>>> 
>>> 
>>> a=['K', 'A', 'S', 'H', 'Y', 'A', 'P']
>>> a.reverse()
>>> print(a)
['P', 'A', 'Y', 'H', 'S', 'A', 'K']
>>> 
>>> 
>>> b=[9, 19, 29, 39]
>>> b.reverse()
>>> print(b)
[39, 29, 19, 9]
>>> 
>>> 
>>> fruites = ['apple', 'banana', 'mango', 'orange']
>>> for o in revers(fruites):
	print(o)

	
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    for o in revers(fruites):
NameError: name 'revers' is not defined
>>> fruites = ['apple', 'banana', 'mango', 'orange']
>>> for o in reversed(fruites):
	print(o)

	
orange
mango
banana
apple
>>> 
>>> 
>>> a = ['a', 'e', 'i', 'o', 'u']
>>> a.sort()
>>> print(a)
['a', 'e', 'i', 'o', 'u']
>>> a = ['o', 'i', 'e', 'u', 'a']
>>> a.sort()
>>> print(a)
['a', 'e', 'i', 'o', 'u']
>>> 
>>> 
>>> b = [19,15,2,9,5,3,99,10,6]
>>> b.sort()
>>> print(b)
[2, 3, 5, 6, 9, 10, 15, 19, 99]
>>> b = [19,15,2,9,5,3,99,15,10,6,3,,3,19,]
SyntaxError: invalid syntax
>>> b = [19,15,2,9,5,3,99,15,10,6,3,3,19,]
>>> b.sort()
>>> print(b)
[2, 3, 3, 3, 5, 6, 9, 10, 15, 15, 19, 19, 99]
>>> 
>>> d = [2,,19,3,25,14,20,'a',5,'z',3,'b']
SyntaxError: invalid syntax
>>> d = [2,19,3,25,14,20,'a',5,'z',3,'b']
>>> d.sort()
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    d.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
>>> 
>>> A = ['a','b','c','d']
>>> A = B
>>> print(B)
[9, 16, 24]
>>> x = [1,2,3]
>>> x=y
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    x=y
NameError: name 'y' is not defined
>>> x = [1,2,3]
>>> y=x
>>> y.append('w')
>>> print(y)
[1, 2, 3, 'w']
>>> print(x)
[1, 2, 3, 'w']
>>> y.append()
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    y.append()
TypeError: append() takes exactly one argument (0 given)
>>> 
>>> A = ['k','a','s','h']
>>> B=A
>>> B=A.copy()
>>> print(b)
[2, 3, 3, 3, 5, 6, 9, 10, 15, 15, 19, 19, 99]
>>> print(B)
['k', 'a', 's', 'h']
>>> print(A)
['k', 'a', 's', 'h']
>>> 
>>> 
>>> J = [99,98,97]
>>> J.clear()
>>> print(J)
[]
>>> 
>>> 
>>> X = ['d','a','d','d','y',2,3,5]
>>> X.clear()
>>> print(X)
[]
>>> 
