Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = ('a','e','i','o','u')
>>> fset = frozenset(a)
>>> print(fset)
frozenset({'u', 'o', 'e', 'i', 'a'})
>>> print(fset)
frozenset({'u', 'o', 'e', 'i', 'a'})
>>> students = {"Name": "Kashyap", "Age": 29, "Subject": "Computer"}
>>> froset = frozenset(students)
>>> print(froset)
frozenset({'Subject', 'Age', 'Name'})
>>> ype(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ype(a)
NameError: name 'ype' is not defined
>>> type(a)
<class 'tuple'>
>>> type(fset)
<class 'frozenset'>
>>> 
