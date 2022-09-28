# -*- coding: utf-8 -*-
"""


"""



def factorial (n):
    f = 1
    for i in range (2, n+1):
        f = f*i
    return (f)





def func_e(x, n):
    e_approx = 0
    for i in range(n):
        e_approx += x**i/factorial(i)
    
    return e_approx


def func_cos(x, n):
    cos_approx = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i)
        denom = factorial(2*i)
        cos_approx += ( coef ) * ( (num)/(denom) )
    
    return cos_approx


"""
class aproximaciondefunciones():
     
    def __init___(self, x, precision):
        self.x = x
        self.precision = precision 
        
   
"""        
        
        
        
        
        
        
        
        


