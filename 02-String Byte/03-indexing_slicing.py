Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

>>> F = ['kashyap','jay','abhay','darshan','mehul','nishant','milan','kunal',]
>>> F[0]
'kashyap'
>>> F[-1]
'kunal'
>>> F[2]
'abhay'
>>> F[9]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    F[9]
IndexError: list index out of range
>>> F[8]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    F[8]
IndexError: list index out of range
>>> F[7]
'kunal'
>>> F[5]
'nishant'
>>> F[-5]
'darshan'
>>> F[-7]
'jay'
>>> F[-8]
'kashyap'
>>> F[-2]
'milan'
>>> del F[-1]
>>> print(F)
['kashyap', 'jay', 'abhay', 'darshan', 'mehul', 'nishant', 'milan']
>>> del F[0]
>>> print(F)
['jay', 'abhay', 'darshan', 'mehul', 'nishant', 'milan']
>>> del F[1]
>>> print(F)
['jay', 'darshan', 'mehul', 'nishant', 'milan']
>>> #Basic use of Slicing
>>> 
>>> a = [9,7,6,5,3,11,15,19,52,21,25,35,45,99,65,45,33,66]
>>> a = [9,7,6,5,3,11,15,19,52,21,25]
>>> b = a[2:6]
>>> print(b)
[6, 5, 3, 11]
>>> a = [9,7,6,5,3,11,15,19,52,21,25]
>>> b = a[2:-1]
>>> print(b)
[6, 5, 3, 11, 15, 19, 52, 21]
>>> a[-1]
25
>>> # join
>>> k = ('kashyap')
>>> p = ('pandya')
>>> print(k.join(p))
pkashyapakashyapnkashyapdkashyapykashyapa
>>> p = ('*')
>>> print(k.join(p))
*
>>> print(k.join(p))
*
>>> p = ('*')
>>> print(k.join(p))
*
>>> print(p.join(k))
k*a*s*h*y*a*p
>>> 
