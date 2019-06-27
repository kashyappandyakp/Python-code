Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=9
>>> b=12
>>> bin(9)
'0b1001'
>>> bin(12)
'0b1100'

>>> 
>>> a & b
8
>>> a | b
13
>>> a ^ b
5
>>> 
>>> 
>>> 
>>> 
>>> not a
False
>>> a
9
>>> bool(a)
True
>>> not a
False
>>> a=0
>>> bool(a)
False
>>> not a
True
>>> 
>>> 
>>> 
>>> not 10
False
>>> not -10
False
>>> not 0
True
>>> not 0.0
True
>>> not 0.01
False
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 12 < 13
True
>>> 12 < 12
False
>>> 12 <= 12
True
>>> 0 < a < 12
False
>>> a
0
>>> 0<= a <= 12
True
>>> 1 <> 12
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> name="darshan"
>>> surname="patel"
>>> age="25"
>>> education="IT"
>>> 
>>> 
>>> name == "darshan"
True
>>> age == 25
False
>>> age == "25"
True
>>> 
>>> 
>>> name == "darshan" and surname == "patel" and age == "25" and education == "IT"
True
>>> age="26"
>>> name == "darshan" and surname == "patel" and age == "25" and education == "IT"
False
>>> age="25"
>>> name == "darshan" and surname == "patel" and age == "25" and education == "IT"
True
>>> 
>>> 
>>> name == "darshan" and surname == "patel" or age == "25" and education == "IT"
True
>>> 
>>> 
>>> age="26"
>>> name == "darshan" and surname == "patel" or age == "25" and education == "IT"
True
>>> name == "darshan" and surname == "patel"
True
>>> 
>>> True or False
True
>>> False or False
False
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=10
>>> b=10
>>> a == b
True
>>> a is b
True
>>> id(a)
1827719440
>>> id(b)
1827719440
>>> 
>>> 
>>> a=1
>>> type(a)
<class 'int'>
>>> float(a)
1.0
>>> complex(a)
(1+0j)
>>> bool(a)
True
>>> str(a)
'1'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> bool(0)
False
>>> bool(-0)
False
>>> bool(-0.1)
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> round(11.152)
11
>>> round(11.552)
12
>>> 
>>> 
>>> 
>>> round(11.152, 1)
11.2
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> abs(-10)
10
>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

>>> abs(-10, /)
SyntaxError: invalid syntax
>>> abs(-10, 2)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    abs(-10, 2)
TypeError: abs() takes exactly one argument (2 given)
>>> abs(-10)
10
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=9
>>> a << 2
36
>>> a >> 2
2
>>> hex()
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    hex()
TypeError: hex() takes exactly one argument (0 given)
>>> hex(555555555515555555555)
'0x1e1de1d2482b7ea8e3'
55555
>>> 5555555555555555555555
555555555555555555555
55555
>>> 
555
>>> 555
55
5555555
>>> 55555555555555555555555555555555555555555555555555555555555555555555555555555555555
55555555555555555555555555555555555555555555555555555555555555555555555555555555555
55555
55
>>> 555
55
555555
>>> 555555555555555555555555555555555555555555555555
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 5555555555555555
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
>>> 
>>> 
>>> 
>>> hex(15)
'0xf'
\
>>> a
9
>>> -a
-9
>>> --a
9
>>> 
>>> 
>>> a=10
>>> a = a + 10
>>> a
20
>>> a+=10
>>> a
30
>>> 
>>> 
>>> a=10
>>> b=10
>>> a == b
True
>>> a is b
True
>>> id(a)
1827719440
>>> id(b)
1827719440
>>> a=157
>>> a=257
>>> b=257
>>> a is b
False
>>> a == b
True
>>> 
>>> 
>>> 
>>> id(a)
63396960
>>> id(b)
63397072
>>> id(a) == id(b)
False
>>> a is b
False
>>> 257 == 257
True
>>> a == b
True
>>> 
>>> 
>>> 
>>> round(11.152)
11
>>> round(11.552)
12
>>> 
>>> 
>>> round(11.452, 1)
11.5
>>> round(11.442, 1)
11.4
>>> 
>>> 
>>> a=-10
>>> abs(a)
10
>>> abs=10
>>> abs(10)
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    abs(10)
TypeError: 'int' object is not callable
>>> bin(9)
'0b1001'
>>> bin-10
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    bin-10
TypeError: unsupported operand type(s) for -: 'builtin_function_or_method' and 'int'
>>> bin=10
>>> 
>>> 
>>> 
>>> bin(10)
Traceback (most recent call last):
  File "<pyshell#247>", line 1, in <module>
    bin(10)
TypeError: 'int' object is not callable
>>> from builtins import *
>>> bin(9)
'0b1001'
>>> abs(10)
10
>>> 
>>> 
>>> a=9
>>> bin(9)
'0b1001'
>>> a << 2
36
>>> a >> 2
2
>>> a=12
>>> a << 2
48
>>> a >> 1
6
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
555
>>> 5555555555555555555555555555555
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 5555555555555
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 55555555555555555
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 555555555555555555555555555555555555555555555555555555555555555555555555555
555555555555555555555555555555555555555555555555555555555555555555555555555
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=10
>>> a=10.10
>>> a=True
>>> a="Harshil"
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a={"harshil", "ronak", "raj", "hemal"}
>>> type(a)
<class 'set'>
>>> b={"darshan", "harshil", "hemal", "raju", "kasyap", "kasyap"}
>>> type(b)
<class 'set'>
>>> 
>>> 
>>> print(a)
{'hemal', 'harshil', 'ronak', 'raj'}
>>> print(b)
{'hemal', 'raju', 'harshil', 'kasyap', 'darshan'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> c={}
>>> type(c)
<class 'dict'>
>>> c={"name": "kasyap", "age": 26, "CPI": 7}
>>> 
>>> 
>>> c
{'name': 'kasyap', 'age': 26, 'CPI': 7}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a
{'hemal', 'harshil', 'ronak', 'raj'}
>>> b
{'hemal', 'raju', 'harshil', 'kasyap', 'darshan'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> type(a)
<class 'set'>
t
>>> y
Traceback (most recent call last):
  File "<pyshell#356>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> type(b)
<class 'set'>
>>> 
>>> 
>>> 
>>> dir(a)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 
>>> 
>>> a
{'hemal', 'harshil', 'ronak', 'raj'}
>>> b
{'hemal', 'raju', 'harshil', 'kasyap', 'darshan'}
>>> 
>>> 
>>> dir(a)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> q=1
>>> dir(q)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> q+10
11
>>> q.__add__(10)
11
>>> q > 10
False
>>> q
1
>>> q.__gt__(10)
False
>>> 
>>> q
1
>>> dir(q)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> q.bit_length()
1
>>> q=10
>>> q.bit_length()
4
>>> q.re
Traceback (most recent call last):
  File "<pyshell#382>", line 1, in <module>
    q.re
AttributeError: 'int' object has no attribute 're'
>>> q.real
10
>>> q
10
>>> q
10
>>> q.real
10
>>> q.imag
0
>>> dir(q)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=10
>>> b=20
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
d
>>> 
>>> dir(b)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 
>>> 
>>> 
>>> a={'a', 'b', 'c', 'd'}
>>> b={'a', 'c', 'q', 'w'}
>>> dir(a)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> type(a)
<class 'set'>
>>> 
>>> 
>>> a.union(b)
{'d', 'w', 'a', 'q', 'c', 'b'}
>>> a
{'d', 'a', 'c', 'b'}
>>> b
{'w', 'a', 'c', 'q'}
>>> a.union(b)
{'d', 'w', 'a', 'q', 'c', 'b'}
>>> q=12
>>> q1=12
>>> q + q1
24
>>> 
>>> 
>>> 
>>> q
12
>>> q.union(q1)
Traceback (most recent call last):
  File "<pyshell#422>", line 1, in <module>
    q.union(q1)
AttributeError: 'int' object has no attribute 'union'
>>> dir(q)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> q.imag
0
>>> q.real
12
>>> q.__add__
<method-wrapper '__add__' of int object at 0x6CF0C930>
>>> q.union
Traceback (most recent call last):
  File "<pyshell#427>", line 1, in <module>
    q.union
AttributeError: 'int' object has no attribute 'union'
>>> dir(a)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> a
{'d', 'a', 'c', 'b'}
>>> a.imag
Traceback (most recent call last):
  File "<pyshell#430>", line 1, in <module>
    a.imag
AttributeError: 'set' object has no attribute 'imag'
>>> dir(q)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> q
12
>>> q.imag
0
>>> q.real
12
>>> 
>>> 
>>> dir(a)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> a.imag
Traceback (most recent call last):
  File "<pyshell#438>", line 1, in <module>
    a.imag
AttributeError: 'set' object has no attribute 'imag'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> q.imag
0
>>> q.imag()
Traceback (most recent call last):
  File "<pyshell#447>", line 1, in <module>
    q.imag()
TypeError: 'int' object is not callable
>>> q.bit_length
<built-in method bit_length of int object at 0x6CF0C930>
>>> q.bit_length()
4
>>> 
>>> 
>>> print
<built-in function print>
>>> print()

>>> print("A")
A
>>> 
>>> 
>>> 
>>> bin
<built-in function bin>
>>> bin()
Traceback (most recent call last):
  File "<pyshell#459>", line 1, in <module>
    bin()
TypeError: bin() takes exactly one argument (0 given)
>>> bin(3)
'0b11'
>>> bin(13)
'0b1101'
>>> bin(131)
'0b10000011'
>>> bin()
Traceback (most recent call last):
  File "<pyshell#463>", line 1, in <module>
    bin()
TypeError: bin() takes exactly one argument (0 given)
>>> bin(234525)
'0b111001010000011101'
>>> 
>>> help(bin)
Help on built-in function bin in module builtins:

bin(number, /)
    Return the binary representation of an integer.
    
    >>> bin(2796202)
    '0b1010101010101010101010'

>>> 
>>> 
>>> 
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> print("Harshil")
Harshil
>>> print("Harshil", "ronak")
Harshil ronak
>>> print("Harshil", "ronak", "darshan")
Harshil ronak darshan
>>> print("Harshil", "ronak", "darshan", "kasyap")
Harshil ronak darshan kasyap
>>> print("Harshil","ronak","darshan","kasyap")
Harshil ronak darshan kasyap
>>> print("Harshil","ronak","darshan","kasyap", sep="#")
Harshil#ronak#darshan#kasyap
>>> print("Harshil","ronak","darshan","kasyap", sep="################")
Harshil################ronak################darshan################kasyap
>>> 
>>> 
>>> 
>>> a
{'d', 'a', 'c', 'b'}
>>> 
>>> 
>>> import fb
Traceback (most recent call last):
  File "<pyshell#484>", line 1, in <module>
    import fb
ModuleNotFoundError: No module named 'fb'
>>> import math
>>> math.sin(123)
-0.45990349068959124
>>> 
>>> 
>>> 
>>> a
{'d', 'a', 'c', 'b'}
>>> type(a)
<class 'set'>
>>> dir(a)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> help(a)
Help on set object:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a
{'d', 'a', 'c', 'b'}
>>> b
{'w', 'a', 'c', 'q'}
>>> 

>>> a | b
{'d', 'w', 'a', 'q', 'c', 'b'}
>>> a.union(b)
{'d', 'w', 'a', 'q', 'c', 'b'}
>>> 9 | 12
13
>>> 9 & 12
8
>>> 9 ^ 12
5
>>> 1+2
3
>>> '1' + '2'
'12'
>>> 1.__add__(2)
SyntaxError: invalid syntax
>>> a=1
>>> a.__add__(2)
3
>>> b='1'
>>> b.__add__('2')
'12'
>>> 
>>> 
>>> 9 | 12
13
>>> a= {'d', 'a', 'c', 'b'}
>>> b = {'w', 'a', 'c', 'q'}
>>> a | b
{'d', 'w', 'a', 'q', 'c', 'b'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> a.union(b)
{'d', 'w', 'a', 'q', 'c', 'b'}
>>> a | b
{'d', 'w', 'a', 'q', 'c', 'b'}
>>> 
>>> a & b
{'a', 'c'}
>>> a - b
{'d', 'b'}
>>> a
{'d', 'a', 'c', 'b'}
>>> b
{'a', 'c', 'q', 'w'}
>>> a - b
{'d', 'b'}
>>> b-a
{'w', 'q'}
>>> 
>>> 
>>> 
>>> 
>>> a^b
{'d', 'w', 'q', 'b'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> 
>>> 
>>> a
{'d', 'a', 'c', 'b'}
>>> 'b' in a
True
>>> 'q' in a
False
>>> b
{'a', 'c', 'q', 'w'}
>>> 'q' in b
True
>>> a
{'d', 'a', 'c', 'b'}
>>> 
>>> 
>>> 
>>> a
{'d', 'a', 'c', 'b'}
>>> b
{'a', 'c', 'q', 'w'}
>>> 'q' in a
False
>>> 'q' in b
True
>>> 
>>> 
>>> 
>>> 
>>> 'q' in a
False
>>> 'q' in not a
SyntaxError: invalid syntax
>>> 'q'not  in a
True
>>> 'q' not  in a
True
>>> a
{'d', 'a', 'c', 'b'}
>>> 'q' not  in b
False
>>> b
{'a', 'c', 'q', 'w'}
>>> 
>>> 
>>> 
>>> a='harshil
SyntaxError: EOL while scanning string literal
>>> a='harshil'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a
'harshil'
>>> 'h' in a
True
>>> 'H' in a
False
>>> 'H'  not in a
True
>>> 
>>> 
>>> a
'harshil'
>>> a = {'d', 'a', 'c', 'b'}
>>> 
>>> 
>>> b
{'a', 'c', 'q', 'w'}
>>> dir(a)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> a.add('Z')
>>> a
{'Z', 'd', 'a', 'c', 'b'}
>>> a.remove('Z')
>>> a
{'d', 'a', 'c', 'b'}
>>> a.remove('Z')
Traceback (most recent call last):
  File "<pyshell#605>", line 1, in <module>
    a.remove('Z')
KeyError: 'Z'
>>> a.discard('Z')
>>> a
{'d', 'a', 'c', 'b'}
>>> a.discard('c')
>>> a
{'d', 'a', 'b'}
>>> a.discard('c')
>>> a
{'d', 'a', 'b'}
>>> 
>>> 
>>> 
>>> a
{'d', 'a', 'b'}
>>> b
{'a', 'c', 'q', 'w'}
>>> dir(a)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> a.clear()
>>> a
set()
>>> a
set()
>>> type(a)
<class 'set'>
>>> bool(a)
False
>>> q=0
>>> bool(q)
False
>>> a
set()
>>> a={1}
>>> type(a)
<class 'set'>
>>> bool(a)
True
>>> 
>>> 
>>> 
>>> 
>>> dir(a)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> a.add(1)
>>> a
{1}
>>> ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
KeyboardInterrupt
>>> a.add(1)
>>> a.add(1)
>>> a.add(1)
>>> a
{1}
>>> a.__sub__
<method-wrapper '__sub__' of set object at 0x01025030>
>>> a.__sub__()
Traceback (most recent call last):
  File "<pyshell#641>", line 1, in <module>
    a.__sub__()
TypeError: expected 1 arguments, got 0
>>> a.__sub__(1)
NotImplemented
>>> dir(a)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 
>>> 
>>> a=10
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a
10
>>> a()
Traceback (most recent call last):
  File "<pyshell#653>", line 1, in <module>
    a()
TypeError: 'int' object is not callable
>>> print
<built-in function print>
>>> print()

>>> 
>>> 
>>> 
>>> def darshan(a, b):
	""" This is my function uses for summation"""
	return a + b

>>> help(darshan)
Help on function darshan in module __main__:

darshan(a, b)
    This is my function uses for summation

>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> 
>>> darshan
<function darshan at 0x03C6F780>
>>> type(darshan)
<class 'function'>
>>> darshan
<function darshan at 0x03C6F780>
>>> darshan()
Traceback (most recent call last):
  File "<pyshell#669>", line 1, in <module>
    darshan()
TypeError: darshan() missing 2 required positional arguments: 'a' and 'b'
>>> darshan(12)
Traceback (most recent call last):
  File "<pyshell#670>", line 1, in <module>
    darshan(12)
TypeError: darshan() missing 1 required positional argument: 'b'
>>> darshan(12, 12)
24
>>> darshan(10, 12)
22
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> a={1}
>>> dir(a)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a={1,2,3}
>>> b=set('harshil')
>>> b
{'h', 'l', 'i', 'a', 's', 'r'}
>>> b=set(123)
Traceback (most recent call last):
  File "<pyshell#699>", line 1, in <module>
    b=set(123)
TypeError: 'int' object is not iterable
>>> b=set(123")
	  
SyntaxError: EOL while scanning string literal
>>> b=set("123")
	  
>>> b
	  
{'2', '3', '1'}
>>> 
	  
>>> 
	  
>>> 
	  
>>> a=frozenset(
	)
>>> a
	  
frozenset()
>>> a=frozenset({'a', 'b', 'c'})
	  
>>> 
	  
>>> a
	  
frozenset({'a', 'c', 'b'})
>>> type(a)
	  
<class 'frozenset'>
>>> dir(a)
	  
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>> dir(b)
	  
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> type(b)
	  
<class 'set'>
>>> type(a)
	  
<class 'frozenset'>
>>> dir(b)
	  
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

>>> a
	  
frozenset({'a', 'c', 'b'})
>>> a.add(10)
	  
Traceback (most recent call last):
  File "<pyshell#718>", line 1, in <module>
    a.add(10)
AttributeError: 'frozenset' object has no attribute 'add'
>>> b
	  
{'2', '3', '1'}
>>> b.add(10)
	  
>>> b
	  
{'2', '3', 10, '1'}
>>> a=123
	  
>>> a=124
	  
>>> a={1,2,3}
	  
>>> id(a)
	  
16920744
>>> a={2,3,4}
	  
>>> id(a)
	  
16921344
>>> a
	  
{2, 3, 4}
>>> a.add(5)
	  
>>> a
	  
{2, 3, 4, 5}
>>> id(a)
	  
16921344
>>> a=123
	  
>>> id(a)
	  
1827721248
>>> a=124
	  
>>> id(a)
	  
1827721264
>>> a=123
	  
>>> b=124
	  
>>> a={'a'}
	  
>>> 
	  
>>> 
	  
>>> a.add('b')
	  
>>> a
	  
{'a', 'b'}
>>> a=frozenset({'a})
		 
SyntaxError: EOL while scanning string literal
>>> a=frozenset({'a'})
		 
>>> a
		 
frozenset({'a'})
>>> a.add('b')
		 
Traceback (most recent call last):
  File "<pyshell#746>", line 1, in <module>
    a.add('b')
AttributeError: 'frozenset' object has no attribute 'add'
>>> id(a)
		 
16920744
>>> a=frozenset({'a', 'b'})
		 
>>> id(a)
		 
16922064
>>> 
		 

>>> 
		 
>>> 
		 
>>> 
