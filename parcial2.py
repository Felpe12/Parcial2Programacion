# -*- coding: utf-8 -*-

#class funcion(){
        #}
"""


"""
import numpy as np
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
    def func_e(x, n):
        e_approx = 0
        for i in range(n):
            e_approx += x**i/factorial(i)
        return e_approx
#-----------------------------------------------------------------------------
    def func_sen(x, n):
        sen_approx = 0 
        for i in range(n):
            coef = x**(2*i +1)
            num =  (-1)**i
            denom = factorial(2*i+1)
            sen_approx += ( coef ) * ( (num)/(denom) )
        return sen_approx
#-----------------------------------------------------------------------------           
    def func_cos(x, n):
        cos_approx = 0
        for i in range(n):
            coef = (-1)**i
            num = x**(2*i)
            denom = factorial(2*i)
            cos_approx += ( coef ) * ( (num)/(denom) )
    
        return cos_approx





sen1= Funcion.func_sen(1.5, 10)

cos1= Funcion.func_cos(1.5, 10)




#----------------------------------------------------------------------------

x= np.linspace(0, 5, 100)
ep= np.exp(x)
cos=np.cos(x)
sin=np.sin(x)

e1= Funcion.func_e( x, 3)      

sen1= Funcion.func_sen(x, 20)

cos1= Funcion.func_cos(x, 3)

mpl.title("Aproximaciones a las funciones")
mpl.subplot(1,1,1)
mpl.title("Aproximaciones a las funciones")
mpl.plot(x, e1)
mpl.plot(x, ep)
mpl.xlabel("X")
mpl.ylabel("Aproximación")
        

#-------------------------------------------------------------------------------


mpl.subplot(1,1,1)

mpl.plot(x, sen1)
mpl.plot(x, sin)
#------------------------------------------------------------------------------

mpl.subplot(1,1,1)

mpl.plot(x, cos1)
mpl.plot(x, cos)

mpl.show()




