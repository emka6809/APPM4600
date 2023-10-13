import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from numpy.linalg import inv 

def driver():


    f = lambda x: 1/(1 + (10*x)**2)

    N = 18
    ''' interval'''
    a = -1
    b = 1
   
   
    ''' create equispaced interpolation nodes'''
    xint = np.linspace(a,b,N+1)
    
    ''' create interpolation data'''
    yint = f(xint)

    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_l= np.zeros(Neval+1)
    yeval_dd = np.zeros(Neval+1)
  
    '''Initialize and populate the first columns of the 
     divided difference matrix. We will pass the x vector'''
    y = np.zeros( (N+1, N+1) )
     
    for j in range(N+1):
       y[j][0]  = yint[j]

    y = dividedDiffTable(xint, y, N+1)
    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_l[kk] = eval_lagrange(xeval[kk],xint,yint,N)
       yeval_dd[kk] = evalDDpoly(xeval[kk],xint,y,N)
          

    


    ''' create vector with exact values'''
    fex = f(xeval)


    '''monomial plot'''
    [a, polynomial_eval] = eval_monomial(f, xint, N, xeval)
    plt.plot(xeval, fex, label = "Monomial Approximation")
    plt.plot(xeval, fex - polynomial_eval, label = "Monomial Error")
    plt.legend()
       

    plt.figure()    
    plt.plot(xeval,fex,'ro-', label = "f(x)")
    plt.plot(xeval,yeval_l,'bs--', label = "lagrange" ) 
    plt.plot(xeval,yeval_dd,'c.--', label = "divided difference")
    plt.legend()

    plt.figure() 
    err_l = abs(yeval_l-fex)
    err_dd = abs(yeval_dd-fex)
    plt.semilogy(xeval,err_l,'ro--',label='lagrange')
    plt.semilogy(xeval,err_dd,'bs--',label='Newton DD')
    plt.legend()
    plt.show()

def eval_monomial(f,x, N, xeval):

    vander = np.zeros([N+1,N+1])
    for i in range(N+1):
        for v in range(N+1):
            vander[i][v] = x[i]**(v)

    
    inv_vander = inv(vander)

    y = f(x) 

    a = inv_vander.dot(y)

    polynomial_eval = []

    for v in xeval:
        num = 0 
        for i in range(N+1):
            num += a[i] * v**i

        polynomial_eval.append(num)

    return(a, polynomial_eval)

    
    

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
  
    


''' create divided difference matrix'''
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
    
def evalDDpoly(xval, xint,y,N):
    ''' evaluate the polynomial terms'''
    ptmp = np.zeros(N+1)
    
    ptmp[0] = 1.
    for j in range(N):
      ptmp[j+1] = ptmp[j]*(xval-xint[j])
     
    '''evaluate the divided difference polynomial'''
    yeval = 0.
    for j in range(N+1):
       yeval = yeval + y[0][j]*ptmp[j]  

    return yeval

     

driver()        
