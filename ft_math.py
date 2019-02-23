from lark import Lark, Transformer, v_args, Tree
import sys
import numpy as np
import config
from config import *
import math

def set_reduce(res):
    config.reduced[config.count] = res
    config.count+=1
    return res

def int_to_array(s, a):
    res = np.array([float(a), 0, 0])
    return set_reduce(res)


def get_pow(a):
    res = int(a.children[0])
    return set_reduce(res)


def ft_equ(s, a, b):
    res = ft_sub(s, a, b)
    return set_reduce(res)

def ft_neg(s, a):
    res = (-a)
    return set_reduce(res)


def ft_sum(s, a, b):
    res = a + b
    return set_reduce(res)


def ft_sub(s, a, b):
    res = a - b
    return set_reduce(res)


def ft_mul(s, a, b):
    if (a[0] or b[0]):
       res = a[0] * b if a[0] else b[0] * a
       return set_reduce(res)
    res = a * b
    return set_reduce(res)


def ft_div(s, a, b):
    res = a / b
    return set_reduce(res)


def ft_modu(s, a, b):
    res = (a % b)
    return set_reduce(res)


def ft_abs(a):
    res = (-a if a < 0 else a)
    return set_reduce(res)


def unknown(s, a):
    res = np.array([0, 1, 0])
    return set_reduce(res)


def ft_pow2(s, a, b):
   if (a[1]):
      if (int(b[0]) >= 3):
         raise Exception("power must be lower than 3")
      a[1] = 0
      a[int(b[0])] = 1
      res = a
      return set_reduce(res) 
   res = ft_pow(a, b)
   return set_reduce(res) 


def ft_sqrt(x):
    return x**(.5)


def ft_pow(a, b):
    if (b is 0):
        return (1)
    if (b == 1):
        return (a)
    return (a * ft_pow(a, b - 1))


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
        print("%f + %f i " % (-b / den, r / den))
        print("%f - %f i " % (-b / den, r / den))
    elif (delta == 0.0):
        print("Discriminant is null, the solution is:")
        x1 = -b / 2 * a
        print(x1)
    else:
        r = ft_sqrt(delta)
        print("Discriminant is strictly positive, the two solutions are:")
        x1 = (-b - r) / den
        x2 = (-b + r) / den
        print(str(x1) + "\n" + str(x2))
