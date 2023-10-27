import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from numpy.linalg import inv

def driver(): 

    f = lambda x: 1./(1.+x**2)

    N = 20
    
    ''' interval'''
    a = -5
    b = 5



    ''' create equispaced interpolation nodes'''
    xint = np.linspace(a,b,N+1)
    

    ''' create chebychev nodes '''
##    xint = np.array([np.cos(((2*i)-1)*np.pi/(2*N + 2)) for i in range(1,N+2)])
##    xint = np.flip(5 * xint)


    
    ''' create interpolation data'''
    yint = f(xint)


    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_lagrange= np.zeros(Neval+1)



    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_lagrange[kk] = eval_lagrange(xeval[kk],xint,yint,N)

    ''' create vector with exact values'''
    fex = f(xeval)



    ''' Lagrange Plot '''    
    # plt.figure()
    plt.plot(xeval,fex, 'black', label = "f(x)")
    plt.plot(xeval,yeval_lagrange,'bs--', label = "Lagrange Approximation" )
   #  plt.legend()
    
   #  plt.figure()
    plt.semilogy(xeval, yeval_lagrange - fex, 'ro--' ,label='Lagrange Error')
    plt.legend()
    plt.show()



def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)











driver()
