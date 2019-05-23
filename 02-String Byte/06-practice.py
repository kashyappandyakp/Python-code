Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Replacing
>>> s = "kashyap pandya"
>>> s = s[:3]+ 'xx'+ s[5:]
>>> print(s)
kasxxap pandya
>>> 	s = s[:3]+ 'xx'+ s[7:]
SyntaxError: unexpected indent
>>> s = s[:3]+ 'xx'+ s[6:]
>>> print(s)
kasxxp pandya
>>> 
>>> a = 'python java'
>>> a = replace ('python','java')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a = replace ('python','java')
NameError: name 'replace' is not defined
>>> a = a.replace ('python','java')
>>> print(a)
java java
>>> b = ('DAVE KUNAL')
>>> b = b.replace('DAVE','PATEL','KUNAL','HARSHIL')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    b = b.replace('DAVE','PATEL','KUNAL','HARSHIL')
TypeError: replace() takes at most 3 arguments (4 given)
>>> b = b.replace('DAVE','PATEL','KUNAL')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    b = b.replace('DAVE','PATEL','KUNAL')
TypeError: 'str' object cannot be interpreted as an integer
>>> b = b.replace('DAVE','PATEL')
>>> print(b)
PATEL KUNAL
>>> b = b.replace('DAVE KUNAL','PATEL HARSHIL')
>>> print(b)
PATEL KUNAL
>>> b = b.replace('DAVEKUNAL','PATELHARSHIL')
>>> print(b)
PATEL KUNAL
>>> c = c.replace('DAVEKUNAL','PATELHARSHIL')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    c = c.replace('DAVEKUNAL','PATELHARSHIL')
NameError: name 'c' is not defined
>>> c = ('DAVEKUNAL','PATELHARSHIL')
>>> c = c.replace('DAVEKUNAL','PATELHARSHIL')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    c = c.replace('DAVEKUNAL','PATELHARSHIL')
AttributeError: 'tuple' object has no attribute 'replace'
>>> c = c.replace('DAVEKUNAL','PATELHARSHIL')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    c = c.replace('DAVEKUNAL','PATELHARSHIL')
AttributeError: 'tuple' object has no attribute 'replace'
>>> c = ('DAVEKUNAL','PATELHARSHIL')
>>> c = c.replace('DAVEKUNAL','PATELHARSHIL')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    c = c.replace('DAVEKUNAL','PATELHARSHIL')
AttributeError: 'tuple' object has no attribute 'replace'
>>> #
>>> #STRING FORMATING
>>> a= "pthon is BEST language"
>>> a.capitalize()
'Pthon is best language'
>>> b = "IF YOU HAVE SUCCESS THEN U HARD WORK"
>>> b.capitalize()
'If you have success then u hard work'
>>> b.lower()
'if you have success then u hard work'
>>> 
>>> 
>>> c = "Ppython is the most popular language"
>>> c = "python is the most popular language"
>>> c.upper()
'PYTHON IS THE MOST POPULAR LANGUAGE'
>>> 
>>> 
>>> c.swapecase()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    c.swapecase()
AttributeError: 'str' object has no attribute 'swapecase'
>>> 
>>> d = 'python learning'
>>> d.swapcase()
'PYTHON LEARNING'
>>> d.title()
'Python Learning'
>>> 
>>> d.casefold()
'python learning'
>>> 
>>> 
>>> d = 'python\t learning'
>>> print(d)
python	 learning
>>> d = '     python learning       '
>>> d.strip()
'python learning'
>>> d = '     python learning       '
>>> d.lstrip()
'python learning       '
>>> d.rstrip()
'     python learning'
>>> k='kashyap'
>>> k.center()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    k.center()
TypeError: center() takes at least 1 argument (0 given)
>>> k.center(3)
'kashyap'
>>> k.center(6)
'kashyap'
>>> k.center(7)
'kashyap'
>>> k.center(8)
'kashyap '
>>> k.center(8,'#')
'kashyap#'
>>> k.center(3,'#')
'kashyap'
>>> k.center(7,'#')
'kashyap'
>>> k.ljust(7)
'kashyap'
>>> k.ljust(7,*)
SyntaxError: invalid syntax
>>> k.ljust(7,'*')
'kashyap'
>>> k.ljust(8,'*')
'kashyap*'
>>> k.rjust(8,'*')
'*kashyap'
>>> k.rjust(9,'*')
'**kashyap'
>>> k.rjust(15,'*')
'********kashyap'
>>> k.ljust(15,'*')
'kashyap********'
>>> k.zfill(5)
'kashyap'
>>> k.zfill(8)
'0kashyap'
>>> k.zfill(15)
'00000000kashyap'
>>> k.zfill(11)
'0000kashyap'
>>> 
>>> 
>>> print(k)
kashyap
>>> k='kashyap'
>>> 
>>> 
>>> 
>>> 
>>> k='kashyap'
>>> k.islower()
True
>>> k.isupper()
False
>>> 
>>> s ='sudhir pandya'
>>> s.istitle()
False
>>> s ='Sudhir Pandya'
>>> s.istitle()
True
>>> l="  "
>>> l.isspace()
True
>>> s.isspace()
False
>>> 
