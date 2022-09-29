# -*- coding: utf-8 -*-

#class funcion(){
        #}
"""


"""

import matplotlib.pyplot as mpl

pi = 3.1415926535897

def factorial (n):
    f = 1
    for i in range (2, n+1):
        f = f*i
    return (f)

class Funcion:
    
    def __init__(self, func, x, n):
            self.func = func
            self.x = x
            self.n = n
#-----------------------------------------------------------------------------            
    def func_e( x, n):
        e_approx = 0
        for i in range(n):
            e_approx += x**i/factorial(i)
        return e_approx
#-----------------------------------------------------------------------------
    def func_sen(self, x, n):
        sen_approx = 0 
        for i in range(n):
            coef = x**(2*i +1)
            num =  (-1)**i
            denom = factorial(2*i+1)
            sen_approx += ( coef ) * ( (num)/(denom) )
        return sen_approx
#-----------------------------------------------------------------------------           
    def func_cos(self, x, n):
        cos_approx = 0
        for i in range(n):
            coef = (-1)**i
            num = x**(2*i)
            denom = factorial(2*i)
            cos_approx += ( coef ) * ( (num)/(denom) )
    
        return cos_approx



e1= Funcion.func_e( 5, 19)


print(e1)

#----------------------------------------------------------------------------



        
        
        
        

