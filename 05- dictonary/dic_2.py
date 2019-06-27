Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #DICTIONARY
>>> students = {'ashish':26,'dushyan':26,'mitul':35,'kashyap':30}
>>> students["kashyap"]
30
>>> del students["ashish"]
>>> print(students)
{'dushyan': 26, 'mitul': 35, 'kashyap': 30}
>>> students.clear()
>>> print(students)
{}
>>> 
>>> students = {'a':20,'b':10,'c':15}
>>> len(students)
3
>>> students.keys()
dict_keys(['a', 'b', 'c'])
>>> students.values()
dict_values([20, 10, 15])
>>> 
>>> 
>>> k = {'a':45,'b':40,'c':35,'d':30,'e':25,'f':20,'g':15,'h':10}
>>> p = {'Z':5,'Y':0,'X':-5,'W':-10}
>>> k.update(p)
>>> print(k)
{'a': 45, 'b': 40, 'c': 35, 'd': 30, 'e': 25, 'f': 20, 'g': 15, 'h': 10, 'Z': 5, 'Y': 0, 'X': -5, 'W': -10}
>>> 
>>> 
>>> A = {1:'one', 2:'two', 3:'three'}
>>> B = {4:'four', 5:'five', 6:'six'}
>>> A = C
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    A = C
NameError: name 'C' is not defined
>>> A = B
>>> print(B)
{4: 'four', 5: 'five', 6: 'six'}
>>> B = A
>>> print(B)
{4: 'four', 5: 'five', 6: 'six'}
>>> B.clear()
>>> 
>>> print(A)
{}
>>> print(B)
{}
>>> A = {1:'one', 2:'two', 3:'three'}
>>> B = A
>>> B.clear()
>>> print('B',B)
B {}
>>> 
>>> 
>>> 
>>> A = {1:'one', 2:'two', 3:'three'}
>>> B = A.copy()
>>> print("C:"A)
SyntaxError: invalid syntax
>>> print("C:",A)
C: {1: 'one', 2: 'two', 3: 'three'}
>>> 
>>> 
>>> B = {4:'four', 5:'five', 6:'six'}
>>> D = B.copy()
>>> print("E:"B)
SyntaxError: invalid syntax
>>> print("E:",B)
E: {4: 'four', 5: 'five', 6: 'six'}
>>> 
>>> 
>>> K = {"KASH":25, 'KUNAL':28, 'MIHIR':30, 'PARTH':32}
>>> P K.copy()
SyntaxError: invalid syntax
>>> K = {"KASH":25, 'KUNAL':28, 'MIHIR':30, 'PARTH':32}
>>> P = K.copy()
>>> print("P:",k)
P: {'a': 45, 'b': 40, 'c': 35, 'd': 30, 'e': 25, 'f': 20, 'g': 15, 'h': 10, 'Z': 5, 'Y': 0, 'X': -5, 'W': -10}
>>> print("P:",K)
P: {'KASH': 25, 'KUNAL': 28, 'MIHIR': 30, 'PARTH': 32}
>>> 
>>> 
>>> x = {'jay':93, 'dhaval':80, 'jasmin':81, 'kashyap':76}
>>> y = x.copy()
>>> print("y:",x)
y: {'jay': 93, 'dhaval': 80, 'jasmin': 81, 'kashyap': 76}
>>> 
>>> 
>>> 
>>> K = {"KASH":25, 'KUNAL':28, 'MIHIR':30, 'PARTH':32}
>>> k.pop("KASH")
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    k.pop("KASH")
KeyError: 'KASH'
>>> K.pop("KASH")
25
>>> print(K)
{'KUNAL': 28, 'MIHIR': 30, 'PARTH': 32}
>>> K.pop("MIHIR")
30
>>> PRINT(K)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    PRINT(K)
NameError: name 'PRINT' is not defined
>>> print(K)
{'KUNAL': 28, 'PARTH': 32}
>>> 
