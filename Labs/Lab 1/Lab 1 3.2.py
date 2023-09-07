Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,1,100)
y = np.arange(0,1,0.01)
x.size
100
>>> y.size
100
>>> x[:3]
array([0.        , 0.01010101, 0.02020202])
>>> print('the first 3 elements of of x are', x[:3])
the first 3 elements of of x are [0.         0.01010101 0.02020202]
>>> w = 10 ** (-np.linspace(1,10,10))
>>> print('the entries of w are', w)
the entries of w are [1.e-01 1.e-02 1.e-03 1.e-04 1.e-05 1.e-06 1.e-07 1.e-08 1.e-09 1.e-10]
>>> x = np.arange(1,10,1)
>>> x = np.arange(1,11,1)
>>> plt.semilogy(x,w)
[<matplotlib.lines.Line2D object at 0x00000227240E9190>]
>>> plt.show()
>>> plt.semilogy(x,w)
[<matplotlib.lines.Line2D object at 0x0000022724DB1F50>]
>>> plt.xlabel('x')
Text(0.5, 0, 'x')
>>> plt.ylabel('log w')
Text(0, 0.5, 'log w')
>>> plt.show()
>>> s = 3 * w
>>> plt.semilogy(x,w)
[<matplotlib.lines.Line2D object at 0x000002272723E4D0>]
>>> plt.semilogy(x,s)
[<matplotlib.lines.Line2D object at 0x000002272727D850>]
>>> plt.show()
>>> plt.show()
>>> plt.semilogy(x,w)
[<matplotlib.lines.Line2D object at 0x000002272B73B110>]
>>> plt.semilogy(x,s)
[<matplotlib.lines.Line2D object at 0x000002272B719890>]
>>> plt.xlabel('x')
Text(0.5, 0, 'x')
>>> plt.ylabel('log w and log s')
Text(0, 0.5, 'log w and log s')
>>> plt.show()
