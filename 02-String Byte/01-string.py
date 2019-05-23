Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #string concatination
>>> 
>>> a="kashyap"
>>> b="Sudhirchandra"
>>> c="Pandya"
>>> d=a+b+c
>>> print(d)
kashyapSudhirchandraPandya
>>> 
>>> a*5
'kashyapkashyapkashyapkashyapkashyap'
>>> b*2
'SudhirchandraSudhirchandra'
>>> e="10"
>>> f="20"
>>> g=e+f
>>> print(g)
1020
>>> k="Mahadev"
>>> l=" 108"
>>> 
>>> p=k+l
>>> print(p)
Mahadev 108
>>> 
>>> 
>>> print 'om ' + 'Namahsivay'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('om ' + 'Namahsivay')?
>>> print ('om ' + 'Namahsivay')
om Namahsivay
>>> 
om Namahsivay
SyntaxError: invalid syntax
>>> 
>>> 
>>> print'kashyap' + str(3)
SyntaxError: invalid syntax
>>> print('kashyap' + str(3))
kashyap3
>>> a=10
>>> 
>>> print('harshil' + str(s))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print('harshil' + str(s))
NameError: name 's' is not defined
>>> print('harshil' + str(a))
harshil10
>>> 
>>> 
>>> print('darshan' * str(a))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print('darshan' * str(a))
TypeError: can't multiply sequence by non-int of type 'str'
>>> print('darshan' + str( a))
darshan10
>>> print('darshan' + str(      a))
darshan10
>>> 
>>> x="JAY"
>>> y=" hind"
>>> z= "indi@ is %s and %s"(x,y)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    z= "indi@ is %s and %s"(x,y)
TypeError: 'str' object is not callable
>>> 
>>> 
>>> ''.join(['a','b','c','d','e'])
'abcde'
>>> .join(['a','b','c','d','e'])
SyntaxError: invalid syntax
>>> ''.join(['India',' Is',' BEST',' country',' in',' THE',' wold'])
'India Is BEST country in THE wold'
>>> 
>>> p=["python ","is ","the ","best ","language ","for ","automation "]
>>> print"".join(p)
SyntaxError: invalid syntax
>>> print''.join(p)
SyntaxError: invalid syntax
>>> print''.join(p)
SyntaxError: invalid syntax
>>> 
