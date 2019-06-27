Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def double():
	pass

>>> double()
>>> 
>>> def double():
	return 4*2

>>> 
>>> double()
8
>>> def double(n):
	return n * 2

>>> double(4)
8
>>> double(20)
40
>>> 
>>> double(50)
100
>>> help(double)
Help on function double in module __main__:

double(n)

>>> def test(a,b,c)
SyntaxError: invalid syntax
>>> def est(a,b,c):
	print(a,b,c)

	
>>> a=test(1,2,3)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a=test(1,2,3)
NameError: name 'test' is not defined
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> def test(a,b,c):
	print(a,b,c)

	
>>> a=test(1,2,3)
1 2 3
>>> print(a)
None
>>> print(b)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(b)
NameError: name 'b' is not defined
>>> print(a)
None
>>> def test(a,b,c)
SyntaxError: invalid syntax
>>> def test(a,b,c):
	print(a,b,c)
	return 10

>>> a=test(1,2,3)
1 2 3
>>> a
10
>>> a
10
>>> def test(a,b,c)
SyntaxError: invalid syntax
>>> def test(a,b,c):
	return 10
        print(a,b,c)
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> a=test(1,2,3)
1 2 3
>>> a
10
>>> test(1,2)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    test(1,2)
TypeError: test() missing 1 required positional argument: 'c'
>>> test(1,2)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    test(1,2)
TypeError: test() missing 1 required positional argument: 'c'
>>> test()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    test()
TypeError: test() missing 3 required positional arguments: 'a', 'b', and 'c'
>>> test(1,2,3)
1 2 3
10
>>> test(10,20,30)
10 20 30
10
>>> test(10,20)Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    test(10,20)
TypeError: test() missing 1 required positional argument: 'c'
>>> def test(a,b=2,c=3):
	print(a,b,c)

	
>>> test(10,20,30)
10 20 30
>>> test(10,20)
10 20 3
>>> test(10)
10 2 3
>>> 
00