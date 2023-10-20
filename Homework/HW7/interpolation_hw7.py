import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from numpy.linalg import inv 

def driver():


    f = lambda x: 1/(1+(10*x)**2)

    N = 25
    ''' interval'''
    a = -1
    b = 1
   

    h = 2/(N-1)
    
    ''' create equispaced interpolation nodes'''
    # xint = np.linspace(a,b,N+1)
    # xint = np.array([(-1 + (i-1)*h) for i in range(1,N+2)])
    xint = np.array([np.cos(((2*i)-1)*np.pi/(2*N)) for i in range(1,N+2)])
    
    ''' create interpolation data'''
    yint = f(xint)

    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1001
    xeval = np.linspace(a,b,Neval+1)
    yeval_barycentric = np.zeros(Neval+1)
    yeval_dd = np.zeros(Neval+1)
  
    '''Initialize and populate the first columns of the 
     divided difference matrix. We will pass the x vector'''
    y = np.zeros( (N+1, N+1) )
     
    for j in range(N+1):
       y[j][0]  = yint[j]

    y = dividedDiffTable(xint, y, N+1)
    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_barycentric[kk] = barycentric(xeval[kk],xint,yint,N)
       yeval_dd[kk] = evalDDpoly(xeval[kk],xint,y,N)
          

    


    ''' create vector with exact values'''
    fex = f(xeval)

    ''' Monomial approximation and error plot'''
    [a, polynomial_eval] = eval_monomial(f, xint, N, xeval)
    plt.plot(xeval, polynomial_eval, 'o', label = "Monomial Approximation")
    plt.plot(xeval, fex - polynomial_eval, label = "Monomial Error")
    plt.legend()
    plt.show()
 
    ''' Barycentric approximation and error plot'''
##    plt.figure()     
##    plt.plot(xeval,yeval_barycentric,'black',marker = 'o', label = "Barycentric Approximation")
##    plt.plot(xeval, abs(fex - yeval_barycentric), label = "Barycentric Error")
##    plt.legend()
##    plt.show()



def eval_monomial(f,x, N, xeval):

    vander = np.zeros([N+1,N+1])
    for i in range(N+1):
        for v in range(N+1):
            vander[i][v] = x[i]**(v)

    
    inv_vander = la.inv(vander)

    y = f(x) 

    a = inv_vander.dot(y)

    polynomial_eval = []

    for v in xeval:
        num = 0 
        for i in range(N+1):
            num += a[i] * v**i

        polynomial_eval.append(num)

    return(a, polynomial_eval)

    
    

def barycentric(xeval,xint,yint,N):

    wj = np.ones(N+1)
    
    for i in range(N+1):
       for j in range(N+1):
           if (j != i):
              wj[i] = wj[i]*(xint[j]-xint[i])
    wj = 1/wj

    num = 0
    denom = 0
    for j in range(N+1):
        if (xeval!= xint[j]):
            num += wj[j]*yint[j] / (xeval-xint[j])
            denom += wj[j] / (xeval - xint[j])

    yeval = num / denom
  
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
