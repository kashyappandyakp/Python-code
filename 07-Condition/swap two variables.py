Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 26
>>> y = 08
SyntaxError: invalid token
>>> x = 26
>>> y = 8
>>> temp = x
>>> print(x)
26
>>> print(y)
8
>>> temp = x
>>> x=y
>>> print(x)
8
>>> print(y)
8
>>> y = temp
>>> print(y)
26
>>> print(x)
8
>>> 
