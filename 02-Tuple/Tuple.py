Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> A=range(10)
>>> list(A)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> tupal(A)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tupal(A)
NameError: name 'tupal' is not defined
>>> tupale(A)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tupale(A)
NameError: name 'tupale' is not defined
>>> tuple(A)
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> set(A)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> 
>>> 
>>> bool(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    bool(a)
NameError: name 'a' is not defined
>>> bool(A)
True
>>> tuple(range(5,15,3))
(5, 8, 11, 14)
>>> b=(5,15,15,20,25,30)
>>> type(b)
<class 'tuple'>
>>> 5 in b
True
>>> 2 in b
False
>>> 
>>> 10 in b
False
>>> b=(5,10,15,15,20,25,30)
>>> 10 in b
True
>>> 15 in b
True
>>> 