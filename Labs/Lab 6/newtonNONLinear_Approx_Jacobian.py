import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():

    x0 = np.array([1, 0])
    
    Nmax = 100
    tol = 1e-10

    
    t = time.time()
    for j in range(50):
      [xstar,ier,its] =  Newton(x0,tol,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Newton: the error message reads:',ier) 
    print('Newton: took this many seconds:',elapsed/50)
    print('Netwon: number of iterations is:',its)
     

    t = time.time()
    for j in range(20):
      [xstar,ier,its] =  SlackerNewton(x0,tol,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Slacker Newton: the error message reads:',ier)
    print('Slacker Newton: took this many seconds:',elapsed/20)
    print('Slacker Newton: number of iterations is:',its)

    t = time.time()
    for j in range(20):
      [xstar, ier,its] =  NewtonFinite(x0,tol,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Newton Finite: the error message reads:',ier)
    print('Newton Finite: took this many seconds:',elapsed/20)
    print('Newton Finite: number of iterations is:',its)


     
def evalF(x): 

    F = np.zeros(2)
    
    F[0] = 4*x[0]**2 + x[1]**2 - 4
    F[1] = x[0] + x[1] - np.sin(x[0] - x[1])
    return F
    
def evalJ(x): 

    
    J = np.array([[8*x[0], 2*x[1]], [1-np.cos(x[0]-x[1]), np.cos(x[0] - x[1])+1]])
    return J


def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
       J = evalJ(x0)
       Jinv = inv(J)
       F = evalF(x0)
       
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]
           

def SlackerNewton(x0,tol,Nmax):

    J = evalJ(x0)
    Jinv = inv(J)
    iterates = [x0]
    count = 0

    if count >= 1 and abs(iterates[count] - iterates[count -1 ]) > [0.01, 0.01]:
        J = evalJ(iterates[-1])
        Jinv = inv(J)
        


    for its in range(Nmax):

       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)
       count = count + 1 
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier,its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]


def NewtonFinite(x0,tol,Nmax):  

    ''' inputs: x0 = initial guess, y0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    J = np.zeros([2,2])

    F = eval(F)


    J[0,0] = forwardx(F[0])
    J[0,1] = forwardx(F[1])
    J[1,0] = forwardy(F[0])
    J[1,1] = forwardy(F[1])


    for its in range(Nmax):
       J = evalJ(x0)
       Jinv = inv(J)
       F = evalF(x0)
       
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]


def forwardx(x0):
    h = 2
    F = evalF(x0)
    return (F(x0[0]+h , x0[1]) - F(x0[0],x0[1])) / h

def forwardy(x0):
    h = 2
    F = evalF(x0)
    return (F(x0[0], x0[1]+h) - F(x0[0],x0[1])) / h
    
        
if __name__ == '__main__':
    # run the drivers only if this is called from the command line
    driver()       
