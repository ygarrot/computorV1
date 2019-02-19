from lark import Lark, Transformer, v_args, Tree
import config
from config import *
import math

# def mule(self, a)
    
# def manage_tree(s, a, b, type)
    # if (isinstance(b, Tree)):
        # return (a)

def get_pow(a):
    return int(a.children[1])

def ft_neg(self, a):
    return (-a)

def ft_sum(self, a, b):

    if (isinstance(b, Tree)):
        return (a)

    if (isinstance(a, Tree)):
        return (b)

    print(a, "+", b) if debug == True else 0 

    return (float(a) + float(b))

def ft_sub(self, a, b):

    print(a, "-", b) if debug == True else 0 

    if (isinstance(b, Tree)):
        config.unknown[get_pow(b) -1][val] *= -1 
        print("return %f" %(a)) if debug == True else 0 
        return (a)

    if (isinstance(b, Tree) and isinstance(a, Tree)):
        print("return %f" %(0)) if debug == True else 0 
        return (0)

    result = float(a) - float(b)
    print("return %f" %(result)) if debug == True else 0 
    return (result)

def ft_mul(s, a, b):

    print(a, "*", b) if debug == True else 0 

    if (isinstance(b, Tree)):
        if (get_pow(b) == 0):
            return (0)
        config.unknown[get_pow(b) -1][val] *= float(a)
        print("return %f" %(0)) if debug == True else 0 
        return (b)

    result = a * b
    print("return %f" %(result)) if debug == True else 0 
    return (result)

def ft_div(s, a, b):
    return(a / b)

def ft_modu(s, a, b):
    return (a % b)

def ft_abs(s, a):
    return (-a if a < 0 else  a)

def ft_sqrt(s, a):
    i = 1
    if (a == 0):
        return (0)
    while (i * i < a):
        i += 1
    print(i, a)
    return (i if (i % a) == 0 else 0)

def ft_pow(s, a, b):

    print(a, "^", b) if debug == True else 0 

    if (b is False):
        return (1)
    if (b == 1):
        return (a)
    
    return (a * s.ft_pow(a, b - 1))

def ft_poly1(a, b):
    x = float(-b) / float(a)
    print("The solution is " + str(x))

def ft_poly2(a, b, c):
    print(a, b)
    delta = math.pow(b, 2.0) - (4.0 * a * c)
    den = 2 * a

    if (delta < 0):
        print("Discriminant is strictly negative, the two solutions are:")
        x1 = (-b / den) - (delta / den)
        print(x1, "+ i /", den)
        x2 = (-b / den) + (delta / den)
        print(x2, "- i /",  den)

    elif (delta is False):
        print("Discriminant is NULL, the solution is:")
        x1 = -b / 2 * a
        print(x1)
        #x2 = x1
    else:
        print("Discriminant is strictly positive, the two solutions are:")
        r = math.sqrt(delta)
        x1 = (-b - r) / den
        x2 = (-b + r) / den
        print (str(x1) + "\n" + str(x2))
