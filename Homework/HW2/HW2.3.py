Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> x = 9.999999995000000 * 10**-10
>>> y = math.e**x
>>> y - 1
1.000000082740371e-09
>>> x + x**2 / 2
1e-09
