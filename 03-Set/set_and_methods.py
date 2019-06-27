Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #SET
>>> a = {1,2,3,4,5}
>>> b = {4,5,6,7,8}
>>> print(a)
{1, 2, 3, 4, 5}
>>> print(b)
{4, 5, 6, 7, 8}
>>> a.add(0)
>>> print(a)
{0, 1, 2, 3, 4, 5}
>>> a.add(9,10)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.add(9,10)
TypeError: add() takes exactly one argument (2 given)
>>> a.add(9)
>>> print(a)
{0, 1, 2, 3, 4, 5, 9}
>>> a.add(10)
>>> print(a)
{0, 1, 2, 3, 4, 5, 9, 10}
>>> a.pop(10)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.pop(10)
TypeError: pop() takes no arguments (1 given)
>>> a.pop()
0
>>> print(a)
{1, 2, 3, 4, 5, 9, 10}
>>> a.pop()
1
>>> a.pop(6)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.pop(6)
TypeError: pop() takes no arguments (1 given)
>>> print(a)
{2, 3, 4, 5, 9, 10}
>>> a.discart(6)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.discart(6)
AttributeError: 'set' object has no attribute 'discart'
>>> a.discart(10)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.discart(10)
AttributeError: 'set' object has no attribute 'discart'
>>> a.discard(10)
>>> print(a)
{2, 3, 4, 5, 9}
>>> a.discard(3)
>>> print(a)
{2, 4, 5, 9}
>>> a.clear()
>>> print(a)
set()
>>> a={'KashyaP','Pandya','5',5,9,{1,2,3},'KASH'}
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a={'KashyaP','Pandya','5',5,9,{1,2,3},'KASH'}
TypeError: unhashable type: 'set'
>>> print(a)
set()
>>> a = {"kash"}
>>> print(a)
{'kash'}
>>> a={"sKashyaP","Pandya","5",5,9,{1,2,3},"KASH"}
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a={"sKashyaP","Pandya","5",5,9,{1,2,3},"KASH"}
TypeError: unhashable type: 'set'
>>> a={"sKashyaP","Pandya","5",5,9,[1,2,3],"KASH"}
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a={"sKashyaP","Pandya","5",5,9,[1,2,3],"KASH"}
TypeError: unhashable type: 'list'
>>> a={"sKashyaP","Pandya","5",5,9,"KASH"}
>>> a={"sKashyaP","Pandya","5",5,9,"KASH",(1,2,3)}
>>> a.remove("KASH")
>>> print(a)
{5, 9, (1, 2, 3), '5', 'Pandya', 'sKashyaP'}
>>> print(a)
{5, 9, (1, 2, 3), '5', 'Pandya', 'sKashyaP'}
>>> a = {1,2,3,4,5}
>>> b = {4,5,6,7,8}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> b.union(a)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> a.intersectin(b)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.intersectin(b)
AttributeError: 'set' object has no attribute 'intersectin'
>>> a.intersection(b)
{4, 5}
>>> 
