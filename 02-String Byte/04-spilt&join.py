Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 'a*b*c'
>>> s.split()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s.split()
NameError: name 's' is not defined
>>> s.split(*)
SyntaxError: invalid syntax
>>> a = 'a*b*c'
>>> a.split()
['a*b*c']
>>> a.split('*')
['a', 'b', 'c']
>>> a.split('*',1)
['a', 'b*c']
>>> 
>>> a.split('*',2)
['a', 'b', 'c']
>>> a = 'a*b*c*d'
>>> a.split('*',2)
['a', 'b', 'c*d']
>>> k= (k*a*s*h*y*a*p)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    k= (k*a*s*h*y*a*p)
NameError: name 'k' is not defined
>>> k= (k*a*s*h*y*a*p)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    k= (k*a*s*h*y*a*p)
NameError: name 'k' is not defined
>>> K= (k*a*s*h*y*a*p)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    K= (k*a*s*h*y*a*p)
NameError: name 'k' is not defined
>>> c= (k*a*s*h*y*a*p)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    c= (k*a*s*h*y*a*p)
NameError: name 'k' is not defined
>>> c= ("k*a*s*h*y*a*p")
>>> c.split('*'5)
SyntaxError: invalid syntax
>>> c.split('*',5)
['k', 'a', 's', 'h', 'y', 'a*p']
>>> a=['p','a','n','d','y','a']
>>> join(a)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    join(a)
NameError: name 'join' is not defined
>>> .join(a)
SyntaxError: invalid syntax
>>> ''.join(a)
'pandya'
>>> c= ('kashyap','kunal')
>>> c.replace()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    c.replace()
AttributeError: 'tuple' object has no attribute 'replace'
>>> c= ('kashyap','kunal','pandya')
>>> c.replace()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c.replace()
AttributeError: 'tuple' object has no attribute 'replace'
>>> b=('a*b*c*d*e)
       
SyntaxError: EOL while scanning string literal
>>> b=('a*b*c*d*e')
       
>>> b.count('*')
       
4
>>> c= ('a*b*c#d#e@f')
       
>>> c.count('*')
       
2
>>> c.count('#')
       
2
>>> c.count('@')
       
1
>>> #finding
       
>>> f='a*b#c%d$e&f#g'
       
>>> a.find()
       
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.find()
AttributeError: 'list' object has no attribute 'find'
>>> a.find('1')
       
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.find('1')
AttributeError: 'list' object has no attribute 'find'
>>> a.find('3')
       
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.find('3')
AttributeError: 'list' object has no attribute 'find'
>>> a.find('a')
       
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.find('a')
AttributeError: 'list' object has no attribute 'find'
>>> f='a*b#c%d$e&f#g'
       
>>> a.find('#')
       
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.find('#')
AttributeError: 'list' object has no attribute 'find'
>>> a.find('-1')
       
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.find('-1')
AttributeError: 'list' object has no attribute 'find'
>>> a.find['-1']
       
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.find['-1']
AttributeError: 'list' object has no attribute 'find'
>>> f='a*b#c%d$e&f#g'
       
>>> f.find('1')
       
-1
>>> f.find('4')
       
-1
>>> f.find('-1')
       
-1
>>> f.find('-5')
       
-1
>>> k = 'kashyap'
       
>>> k.find(1)
       
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    k.find(1)
TypeError: must be str, not int
>>> k.find('1')
       
-1
>>> k.find('5')
       
-1
>>> k.index('2')
       
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    k.index('2')
ValueError: substring not found
>>> k.index('1')
       
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    k.index('1')
ValueError: substring not found
>>> k = 'kashyap'
       
>>> k.startwith('k')
       
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    k.startwith('k')
AttributeError: 'str' object has no attribute 'startwith'
>>> k = 'kashyap'k.startwith('k')
       
SyntaxError: invalid syntax
>>> k = 'kashyap'
       
>>> k.startswith('k')
       
True
>>> k.startswith('p')
       
False
>>> k.endswith('p')
       
True
>>> k.endswith('k')
       
False
>>> k.endswith('m')
       
False
>>> 
