#String Formating

Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '{} {} {}'.formate(123,'s',[1,2,3])
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    '{} {} {}'.formate(123,'s',[1,2,3])
AttributeError: 'str' object has no attribute 'formate'
>>> '{} {} {}'.format(123,'s',[1,2,3])
'123 s [1, 2, 3]'
>>> '{a}{b}{c}'.format(a='aaa',b='ccc',c='ddd')
'aaacccddd'
>>> '{a} {b} {c}'.format(a='aaa',b='ccc',c='ddd')
'aaa ccc ddd'
>>> l=[1,2,3,4,5]
>>> L=[1,2,3,4,5]
>>> '{0},{1}'format(*l)
SyntaxError: invalid syntax
>>> '{0},{1}'format(*L)
SyntaxError: invalid syntax
>>> '{0},{1}'.format(*L)
'1,2'
>>> 
>>> 
>>> D={'a':11,'b':22,'c':33}
>>> '{a} {b}'.format(**D)
'11 22'
>>> 
>>> 
>>> '{a} {b}'.format(***D)
SyntaxError: invalid syntax
>>> 
>>> 
>>> L=[11,22,33]
>>> '{0} {1}'.format(L,99)
'[11, 22, 33] 99'
>>> 
>>> '{0[0]} !={0[2]}'.format(L)
'11 !=33'
>>> 
>>> 
>>> 'G[0]' !={G[2]}'.format(G=L)
SyntaxError: EOL while scanning string literal
>>> '{G[0]} !={G[2]}'.format(G=L)
'11 !=33'
>>> 
>>> 
>>> K={'First':'KASHYAP','Last':'PANDYA'}
>>> '{P[First]}{P[Last]}'.format(P=K)
'KASHYAPPANDYA'
>>> '{P[First]} {P[Last]}'.format(P=K)
'KASHYAP PANDYA'
>>> 
>>> 
>>> '{1:d}'.format(11,22,33.00,'dd')
'22'
>>> 
>>> 
>>> '{1:f}'.format(11,22,33.000,'dd')
'22.000000'
>>> '{2:f}'.format(11,22,33.000,'dd')
'33.000000'
>>> '{4:f}'.format(11,22,33.000,'dd')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    '{4:f}'.format(11,22,33.000,'dd')
IndexError: tuple index out of range
>>> 
>>> 
>>> '{1:c}'.format(64,65,33.0000,'dd')
'A'
>>> '{1:k}'.format(64,65,33.0000,'dd')
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    '{1:k}'.format(64,65,33.0000,'dd')
ValueError: Unknown format code 'k' for object of type 'int'
>>> '{1:d}'.format(64,65,33.0000,'dd')
'65'
>>> 
>>> 
>>> 
>>> '{1:0}'.format(164,64)
'64'
>>> '{1:1}'.format(164,64)
'64'
>>> '{0:1}'.format(164,64)
'164'
>>> 
>>> 
>>> '{1:2}'.format(164,64)
'64'
>>> '{1:3}'.format(164,64)
' 64'
>>> '{1:9}'.format(164,64)
'       64'
>>> 
>>> 
>>> '{1:x} {1:X}'.format(11,10)
'a A'
>>> 
>>> 
>>> '{0:b}'.format(10)
'1010'
>>> '{0:b}'.format(15)
'1111'
>>> '{0:b}'.format(15000)
'11101010011000'
>>> 
>>> '{0:e}'.format(10)
'1.000000e+01'
>>> '{0:e}'.format(9)
'9.000000e+00'
>>> 
>>> '{0:E}'.format(10)
'1.000000E+01'
>>> '{0:E}'.format(21)
'2.100000E+01'
>>> 
>>> 
>>> 
