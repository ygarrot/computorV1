from lark import Lark, Transformer, v_args, Tree
import config
from config import *
import math

def get_pow(a):
    return int(a.children[0])

def ft_neg(self, a):
    return (-float(a))

def ft_sum(self, a, b):


    if (config.debug == True):
       config.dstr += config.pstr
    print(config.dstr, a, "+", b, end=' ')  if config.debug == True else 0 

    if (isinstance(b, list) and isinstance(a, list)):
        if b[0] == a[0]:
           config.unknown[a[0]] += config.unknown[b[0]] 
        print("return %f" %(0)) if config.debug == True else 0 
        return (0)

    if (isinstance(b, list)):
        print(" return %f" %(a)) if config.debug == True else 0 
        return (a)

    if (isinstance(a, list)):
        print(" return %f" %(b)) if config.debug == True else 0 
        return (b)

    result = float(a) + float(b)
    print(" return %f" %(result)) if config.debug == True else 0 

    return (result)

def ft_sub(self, a, b):

    if (config.debug == True):
       config.dstr += config.pstr
    print(config.dstr, a, "-", b, end=' ') if config.debug == True else 0 

    if (isinstance(b, list) and isinstance(a, list)):
        if b[0] == a[0]:
           config.unknown[a[0]] -= config.unknown[b[0]] 
        print("return %f" %(0)) if config.debug == True else 0 
        return (0)

    if (isinstance(a, list)):
        config.unknown[a[0] - 1] *= -1 
        print("return %f" %(b)) if config.debug == True else 0 
        return (b)

    if (isinstance(b, list)):
        config.unknown[b[0] - 1] *= -1 
        print("return %f" %(a)) if config.debug == True else 0 
        return (a)

    result = float(a) - float(b)
    print("return %f" %(result)) if config.debug == True else 0 
    return (result)

def ft_mul(s, a, b):

    if (config.debug == True):
       config.dstr += config.pstr
    print(config.dstr, a, "*", b, end=' ') if config.debug == True else 0 

    if (isinstance(b, list) and isinstance(a, list)):
        if b[0] == a[0]:
           config.unknown[a[0]] += config.unknown[b[0]] 
        print("return %f" %(0)) if config.debug == True else 0 
        return (0)

    if (isinstance(a, list)):
        config.unknown[a[0] - 1] *= float(b)
        print("return %f" %(0)) if config.debug == True else 0 
        return (a)

    if (isinstance(b, list)):
        config.unknown[b[0] - 1] *= float(a)
        print("return %f" %(0)) if config.debug == True else 0 
        return (b)

    result = float(a) * float(b)
    print("return %f" %(result)) if config.debug == True else 0 
    return (result)

def ft_div(s, a, b):
    if (config.debug == True):
       config.dstr += config.pstr
    print(config.dstr, a, "/", b, end=' ') if config.debug == True else 0 

    if (isinstance(b, list)):
        config.unknown[b[0] - 1] /= float(a)
        print("return %f" %(0)) if config.debug == True else 0 
        return (b)

    result = float(a) / float(b)
    print("return %f" %(result)) if config.debug == True else 0 
    return (result)

def ft_modu(s, a, b):
    return (a % b)

def ft_abs(s, a):
    return (-a if a < 0 else  a)

def ft_sqrt(x):
    return x**(.5)

def ft_pow2(s, a, b):
   power = int(b) 
   if (power < 0 or power > 2):
       raise ValueError('power must be between 0 or 2')
   if (power == 0):
       return 1
   config.unknown[power - 1] += 1
   return [power] 

def ft_pow(a, b):

    if (b is 0):
        return (1)
    if (b == 1):
        return (a)
    return (a * ft_pow(a, b - 1))

def var(s, a):
   config.unknown[0] |= 1
   return [0] 

def ft_poly1(a, b):
    print("Polynomial degree: 1:")
    print("Reduced form: %f * X^1 + %f * X^0 = 0" % (a, b))
    print("x = %f / %f" % (float(-b), float(a)))
    x = float(-b) / float(a)
    print("The solution is " + str(x))

def ft_poly2(a, b, c):

    print("Polynomial degree: 2")
    print("Reduced form: %f * X^2 + %f * X^1 + %f * X^0 = 0" % (a, b, c))
    delta = ft_pow(abs(b), 2.0) - (4.0 * a * c)
    den = 2 * a

    if (delta < 0):
        r = ft_sqrt(-delta)
        print("Discriminant is strictly negative, the two solutions are:")
        print("%f + %f i " % (-b / den, r /den))
        print("%f - %f i " % (-b / den, r /den))
    elif (delta == 0.0):
        print("Discriminant is null, the solution is:")
        x1 = -b / 2 * a
        print(x1)
    else:
        r = ft_sqrt(delta)
        print("Discriminant is strictly positive, the two solutions are:")
        x1 = (-b - r) / den
        x2 = (-b + r) / den
        print (str(x1) + "\n" + str(x2))
