#JUAN FELIPE VILLARREAL RESTREPO



import numpy as np
import matplotlib.pyplot as mpl

pi = 3.1415926535897
"""
Defino una función factorial que me permitirá evitar la librería math, y 
hacer mis respectivas aproximaciones ciertas funciones en específico.

"""

def factorial (n):
    f = 1
    for i in range (2, n+1):
        f = f*i
    return (f)

#se procede a crear una clase Funciones donde estarán los métodos de aproximación.

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










#----------------------------------------------------------------------------
"""
como siguiente paso, es gtraficar las funciones aproximaciones(exp(x), cos(x),
sen(x) junto con lo que corresponde a las funciones dasdas en sí.

"""
#---------------------------------------------------------------------------
x= np.linspace(0, 5, 100) #que nos dará los puntos que se evaluarán el la función.

n= int(input("ingrese la presición que deseas en la serie: "))


ep= np.exp(x)  #
cos=np.cos(x)  #Las funciones exactas.
sin=np.sin(x)  #

e1= Funcion.func_e( x, n)      

sen1= Funcion.func_sen(x, n)

cos1= Funcion.func_cos(x, n)

mpl.title("Aproximaciones a las funciones")
 
                 
mpl.subplot(3,1,1)
mpl.title("Aproximaciones a las funciones")
mpl.plot(x, e1, 'r',ls='--',label='Aproxexp(x)')
mpl.plot(x, ep, label="exp(x)")
mpl.ylabel("exp(X)")        
#-------------------------------------------------------------------------------

mpl.subplot(3,1,2)

mpl.plot(x, sen1, 'r',ls='--',label="Aproxsen(x)")
mpl.plot(x, sin, label= "sen(x)")
mpl.ylabel("sen(X)")  
#------------------------------------------------------------------------------

mpl.subplot(3,1,3)

mpl.plot(x, cos1,'r',ls='--',label='Aproxcos(x)')
mpl.plot(x, cos, label= "cos(x)")
mpl.ylabel("cos(X)")  
mpl.show()




