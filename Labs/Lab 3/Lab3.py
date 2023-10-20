Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\bisection_example.py
the approximate root is 0.9999999701976776
the error message reads: 0
f(astar) = -2.98023206113385e-08
## Solutions: 1(a)

=== RESTART: C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\bisection_example.py ==
the approximate root is 0.9999999701976776
the error message reads: 0
f(astar) = -2.98023206113385e-08
## 1(b)

=== RESTART: C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\bisection_example.py ==
the approximate root is -1
the error message reads: 1
f(astar) = -2
## 1(c)

=== RESTART: C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\bisection_example.py ==
the approximate root is 0.9999999701976776
the error message reads: 0
f(astar) = -2.98023206113385e-08
## For the intervals in (a) and (c) were successful in finding the root  (aprroximately x = 1) because the root that was found via bisection results in f(root) being effectively equal to 0. For part (b), this method was unable to find the root x=0. Bisection cannot find an x = 0 root.

## 2(a)

= RESTART: C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\bisection_example.py
the approximate root is 1.0000030517578122
the error message reads: 0
f(astar) = 2.4414006618542327e-05
# 2(b)

= RESTART: C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\bisection_example.py
the approximate root is 0
the error message reads: 1
f(astar) = -3
# 2(c)

= RESTART: C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\bisection_example.py
the approximate root is 0
the error message reads: 0
f(astar) = 0.0
# 2(c)_2

= RESTART: C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\bisection_example.py
the approximate root is 0.5
the error message reads: 1
f(astar) = 0.479425538604203
## This behavior is not what I expected because for 2(b) and the second part of 2(c), we did not get a true root. But it does work as expected for part (a) and the first section of part (c), with the root being accurate to 10^-5.

## 3(a)

= RESTART: C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py
Traceback (most recent call last):
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 54, in <module>
    driver()
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 18, in driver
    [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 42, in fixedpt
    x1 = f(x0)
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 7, in <lambda>
    f1 = lambda x: x * (1+(7-x**5)/x**2)**3
ZeroDivisionError: float division by zero

= RESTART: C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py
Traceback (most recent call last):
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 54, in <module>
    driver()
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 18, in driver
    [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 42, in fixedpt
    x1 = f(x0)
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 7, in <lambda>
    f1 = lambda x: x * (1+(7-x**5)/x**2)**3
OverflowError: (34, 'Result too large')
## 3(a) with the right inputs, whoops

= RESTART: C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py
Traceback (most recent call last):
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 54, in <module>
    driver()
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 18, in driver
    [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 42, in fixedpt
    x1 = f(x0)
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 7, in <lambda>
    f1 = lambda x: x * (1+(7-x**5)/x**2)**3
OverflowError: (34, 'Result too large')
>>> ## The result for 3(a) and 3(b) is too large, meaning that the fixed point method does not converge and the functions will go to infinity after x0=1.
>>> 
>>> ## 3(c)
>>> ## 3 (c) and (d)
>>> 
>>> 
= RESTART: C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py
Traceback (most recent call last):
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 54, in <module>
    driver()
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 18, in driver
    [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 42, in fixedpt
    x1 = f(x0)
  File "C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py", line 7, in <lambda>
    f1 = lambda x: x - (x**5-7)/5*x**4
OverflowError: (34, 'Result too large')
>>> 
= RESTART: C:\Users\emily\OneDrive\APPM 4600\Labs\Lab3\fixedpt_example.py
the approximate fixed point is: 1.475773161594552
f1(xstar): 1.4757731615945522
Error message reads: 0
the approximate fixed point is: 1.4735780454667078
f2(xstar): 1.4779035096682076
Error message reads: 1
