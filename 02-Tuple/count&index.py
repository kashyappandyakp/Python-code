Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A = ('m','i','h','i','r')
>>> A.count('m')
1
>>> A.count('m')
1
>>> A.count('i')
2
>>> A = ('m','i','h','i','r','m','m','m','h','i','r','r')
>>> A.count('i')
3
>>> A.count('m')
4
>>> A.index('m')
0
>>> A = ('i','h','i','r','m','m','m','h','i','r','r')
>>> A.index('m')
4
>>> A.index('r')
3
>>> A = ('i','h','i','r','m','m','m','h','i','r','r')
>>> A.index('H')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    A.index('H')
ValueError: tuple.index(x): x not in tuple
>>> 
