Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=10
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> print(b)
10
>>> a=10
>>> id(a)
1387055376
>>> id(b)
1387055376
>>> a is b
True
>>> b is a
True
>>> a==b
True
>>> a=none
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a=none
NameError: name 'none' is not defined
>>> a=None
>>> type(a)
<class 'NoneType'>
>>> all[1,2,0]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    all[1,2,0]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> all([1,2,0])
False
>>> all([1,2,-1])
True
>>> any([1,2,0])
True
>>> ascii('a')
"'a'"
>>> '\u913'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-4: truncated \uXXXX escape
>>> '\u0913'
'ओ'
>>> ascii('ओ')
"'\\u0913'"
>>> n='\u0913'
>>> ascii(n)
"'\\u0913'"
>>> n
'ओ'
>>> d=1
>>> callable(d)
False
>>> callable(any)
True
>>> import math
>>> callable (math)
False
>>> math()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    math()
TypeError: 'module' object is not callable
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> callable(math.pi)
False
>>> callable(math.sin)
True
>>> for i,v in enumerate([5,6,7]):
	print(i,v)

	
0 5
1 6
2 7
>>> i=0
>>> for v in [5,6,7]
SyntaxError: invalid syntax
>>> for v in [5,6,7]:
	print (i,v)

	
0 5
0 6
0 7
>>> for v in [5,6,7]:
	print (i,v)
	i=i+1

	
0 5
1 6
2 7
>>> chr(97)
'a'
>>> ord('a')
97
>>> chr(65)
'A'
>>> chr("ka")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    chr("ka")
TypeError: an integer is required (got type str)
>>> ord('ka')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    ord('ka')
TypeError: ord() expected a character, but string of length 2 found
>>> ord('k')
107
>>> for i in 'kashyap':
	print(i)

	
k
a
s
h
y
a
p
>>> for i in 'kashyap':
	chr(i)

	
Traceback (most recent call last):
  File "<pyshell#55>", line 2, in <module>
    chr(i)
TypeError: an integer is required (got type str)
>>> for i in 'kashyap':
	ord(i)

	
107
97
115
104
121
97
112
>>> for i in 'kashyap':
	print(i,ord(i))

	
k 107
a 97
s 115
h 104
y 121
a 97
p 112
>>> a=10
>>> b=10
>>> id(a),id(b)
(1387055376, 1387055376)
>>> 1,2,3
(1, 2, 3)
>>> id(1,2,3)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    id(1,2,3)
TypeError: id() takes exactly one argument (3 given)
>>> id((1,2,3))
36522784
>>> a == b
True
>>> a is b
True
>>> a=300
>>> b=300
>>> id(b)
36383968
>>> id(a)
36383904
>>> a==b
True
>>> a is b
False
>>> a=harshil
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a=harshil
NameError: name 'harshil' is not defined
>>> a='harshil'
>>> b='harshil'
>>> a==b
True
>>> a is b
True
>>> a='harshil patel'
>>> b='harshil patel'
>>> a == b
True
>>> a is b
False
>>> a
'harshil patel'
>>> b=a
>>> a==b
True
>>> a is b
True
>>> a=(1,2,3)
>>> b=(1,2,3)
>>> a==b
True
>>> a is b
False
>>> b=a
>>> a==b
True
>>> a is b
True
>>> 
>>> 
>>> 
>>> 
>>> a=[1,2,3]
>>> type(a)
<class 'list'>
>>> b=[1,2,3]
>>> 
>>> 
>>> a == b
True
>>> id(a)
34398296
>>> id(b)
36556512
>>> a is b
False
>>> b=1
>>> b=a
>>> 
>>> 
>>> 
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]
>>> a is b
True
>>> 
>>> 
>>> 
>>> 
