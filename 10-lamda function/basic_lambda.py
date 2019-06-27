Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #LAMDA function
>>> 
>>> r = lambda x,y:x*y
>>> r(25,5)
125
>>> k = lambda a,b,c:a*b+c
>>> k(5,5,4)
29
>>> j = lambda m,n,o,p:m/n*o+p
>>> j(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    j(1,2,3,4,5)
TypeError: <lambda>() takes 4 positional arguments but 5 were given
>>> j(1,2,3,4,)
5.5
>>> j = lambda m,n,o,p:m-n/o*p
>>> j(2,5,4,3)
-1.75
>>> j = lambda m,n,o,p:m-n/o*p
>>> 
>>> 
>>> m= lambda a,b,c,d,e:a*b*c*d*e
>>> m(1*2*3*4)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    m(1*2*3*4)
TypeError: <lambda>() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
>>> m= lambda a,b,c,d,e:a*b*c*d*e
>>> m(1*2*3*4*5)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    m(1*2*3*4*5)
TypeError: <lambda>() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
>>> m(1*2*3*4*5)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    m(1*2*3*4*5)
TypeError: <lambda>() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
>>> m= lambda a,b,c,d,e:a*b*c*d*e
>>> m(5*4*3*2*1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    m(5*4*3*2*1)
TypeError: <lambda>() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
>>> m= lambda a,b,c,d,e:a*b*c*d*e
>>> m(5*4*3*2*1)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    m(5*4*3*2*1)
TypeError: <lambda>() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
>>> 
>>> m= lambda a,b,c,d,e:a*b*c*d*e
>>> m(1,2,3,4,5)
120
>>> list = [215,25,19,26,13,56,79,91,23,26,35,65,90,45,68,99,56,78,10,39,70,104]
>>> list = [215,25,19,26,13,56,79,91,23,26,35,65,90,45,68,99,56,78,10,39,70,104]
>>> result = list(filter(lambda x:(x % 13 ==0),list))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    result = list(filter(lambda x:(x % 13 ==0),list))
TypeError: 'list' object is not callable
>>> L = [215,25,19,26,13,56,79,91,23,26,35,65,90,45,68,99,56,78,10,39,70,104]
>>> result = l(filter(lambda x:(x % 13 ==0),l))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    result = l(filter(lambda x:(x % 13 ==0),l))
NameError: name 'l' is not defined
>>> result = L(filter(lambda x:(x % 13 ==0),L))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    result = L(filter(lambda x:(x % 13 ==0),L))
TypeError: 'list' object is not callable
>>> 
>>> 
>>> A = [10,20,30,2,4,6,7,9,11,13,15,18,21,22,25,35,17]
>>> result = list(filter(lambda x:(x % 5==0),A))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    result = list(filter(lambda x:(x % 5==0),A))
TypeError: 'list' object is not callable
>>> result = A(filter(lambda x:(x % 5==0),A))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    result = A(filter(lambda x:(x % 5==0),A))
TypeError: 'list' object is not callable
>>> result = list(filter(lambda x:(x % 5==0),A))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    result = list(filter(lambda x:(x % 5==0),A))
TypeError: 'list' object is not callable
>>> A = [10,20,30,2,4,6,7,9,11,13,15,18,21,22,25,35,17]result = list(filter(lambda x:(x % 5==0),A))
SyntaxError: invalid syntax
>>> list(filter(lambda x: x%2 == 0,range(101)))
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list(filter(lambda x: x%2 == 0,range(101)))
TypeError: 'list' object is not callable
>>> a=list(filter(lambda x: x%2 == 0,range(101)))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a=list(filter(lambda x: x%2 == 0,range(101)))
TypeError: 'list' object is not callable
>>> 
