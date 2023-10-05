import numpy as np

def driver():
    

    f = lambda x: np.cos(x)
    h = 0.01 * 2.**(-np.arange(0,10))
    s = np.pi / 2

    point = -1
    vector = forward(f,h,s)

    (forward_difference) = forward(f,h,s)
    print('the forward difference is', forward(f,h,s))

    (centered_difference) = center(f,h,s)
    print('the centered difference is', center(f,h,s))

    (convergence_order) = convergence(point,vector)
    print('the order of convergence is', convergence(point, vector))

    
    
def forward(f, h, s):
    return (f(s+h) - f(s)) / h


def center(f,h,s):
    return (f(s+h) - f(s-h)) / (2*h)


def convergence(point, vector): # this does not work
    N = len(vector)

    errors = np.abs(np.array(vector) - point)

    log_errors = np.log(errors)
    log_ratios = np.diff(log_errors) / np.diff(np.log(np.array(vector[:-1] - point)))

    order = np.mean(log_ratios)

    return order 
    
driver()
 
    
