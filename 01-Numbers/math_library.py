Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> math.cos(1)
0.5403023058681398
>>> math.cos(5)
0.28366218546322625
>>> math.cos(9)
-0.9111302618846769
>>> math.sin(1)
0.8414709848078965
>>> math.sin(5)
-0.9589242746631385
>>> math.sin(9)
0.4121184852417566
>>> math.tan(1)
1.5574077246549023
>>> 
>>> 
>>> math.tan(1)
1.5574077246549023
>>> math.tan(5)
-3.380515006246586
>>> math.tan(9)
-0.45231565944180985
>>> 
>>> 
>>> math.log(1)
0.0
>>> math.log(5)
1.6094379124341003
>>> math.log(9)
2.1972245773362196
>>> 
>>> 
>>> math.pi
3.141592653589793
>>> math.pi(5)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    math.pi(5)
TypeError: 'float' object is not callable
>>> 
>>> math.e
2.718281828459045
>>> 
>>> 
>>> math.power(2,5)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    math.power(2,5)
AttributeError: module 'math' has no attribute 'power'
>>> math.pow(2,5)
32.0
>>> math.pow(10,5)
100000.0
>>> math.pow(5,5)
3125.0
>>> math.pow(5,4)
625.0
>>> 
>>> 
>>> math.gcd(10,15)
5
>>> math.lcd(10,15)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    math.lcd(10,15)
AttributeError: module 'math' has no attribute 'lcd'
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> math.sqrt(100)
10.0
>>> math.sqrt(10)
3.1622776601683795
>>> 
>>> math.sqrt(9)
3.0
>>> 
>>> math.sqrt(81)
9.0
>>> math.sqrt(1032)
32.12475680841802
>>> math.sqrt(1024)
32.0
>>> math.hcf(10,15)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    math.hcf(10,15)
AttributeError: module 'math' has no attribute 'hcf'
>>> math.isfinite(5)
True
>>> math.isnan(5)
False
>>> 
>>> math.factorial(6)
720
>>> math.factorial(15)
1307674368000
>>> math.factorial(1)
1
>>> math.factorial(10)
3628800
>>> math.degre(360)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    math.degre(360)
AttributeError: module 'math' has no attribute 'degre'
>>> math.degrees(150)
8594.366926962348
>>> math.degrees(360)
20626.480624709635
>>> 
>>> 
>>> math.reminder(25)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    math.reminder(25)
AttributeError: module 'math' has no attribute 'reminder'
>>> math.remainder(25)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    math.remainder(25)
TypeError: remainder expected 2 arguments, got 1
>>> math.remainder(25,3)
1.0
>>> math.remainder(25,7)
-3.0
>>> math.remainder(25,5)
0.0
>>> 
