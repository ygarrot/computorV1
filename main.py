import argparse
from lark import Lark, Transformer, v_args, Tree, UnexpectedInput
import sys
import ft_math
import traceback
import logging
import config
from config import *


try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass

calc_grammar = r"""
    ?start: sum

    ?sum: product
        | sum "+" product    -> ft_sum
        | sum "-" product     -> ft_sub

    ?product: pow
        | product "*" pow        -> ft_mul
        | product "/" pow        -> ft_div

    ?pow: atom
        | pow "^" atom      -> ft_pow

    ?atom: DECIMAL         
        | INTEGER         
        | UCASE_LETTER 
        | "-" atom         -> ft_neg
        | "(" sum ")"

    DECIMAL: INTEGER "." INTEGER 
    INTEGER : /[0-9]+/

    %import common.UCASE_LETTER
    %import common.NUMBER
    %import common.WS_INLINE
    %import common.LF
    %ignore WS_INLINE
"""

def pretty_mode(left_print, right_print):
     print("\nPretty mode\n~~~~~~~~~~~~~~~~~~~~~~\n")
     print(left_print.pretty(config.pstr)) if isinstance(left_print, Tree) else print(left_print)
     print ("=\n")
     print(right_print.pretty(config.pstr)) if isinstance(right_print, Tree) else print(right_print)
     print("~~~~~~~~~~~~~~~~~~~~~~\ndone")

@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from ft_math import var, ft_sum, ft_sub, ft_mul, ft_div, ft_neg, ft_pow2 as ft_pow
    number = float

    def __init__(self):
        self.vars = {}

def test(equation, is_pretty=False):
    calc_parser = Lark(calc_grammar, parser='lalr',debug=True, transformer=CalculateTree())
    pretty = Lark(calc_grammar, parser='lalr',debug=True)
    string = equation 
    try:
      l_str, r_str = string.split("=")
    except Exception as e:
      sys.exit("please give me something like ax^{2}+bx+c=0")

    left = [0,0,0]
    right = [0,0,0]
    print(l_str, "=", r_str)
    try:
        tmp = calc_parser.parse(r_str)
        left_print = pretty.parse(r_str)
        right = config.unknown 
        right[c1] = tmp if type(tmp) is not list else 0 

        config.dstr= ""
        config.unknown = [0, 0, 0]
        tmp = calc_parser.parse(l_str)
        right_print = pretty.parse(l_str)
        left = config.unknown 
        left[c1] = tmp if type(tmp) is not list else 0 
    except UnexpectedInput as it:
        print("there is an error in parsing(handled error):\n", file=sys.stderr)
        sys.exit(it)
    except Exception as e:
        print("there is an error in parsing:", file=sys.stderr)
        print(l_str, r_str, ":" , e, file=sys.stderr)
        sys.exit()

    if is_pretty is True:
      pretty_mode(left_print, right_print)
    a = float(left[a1]) - float(right[a1])
    b = float(left[b1]) - float(right[b1])
    c = float(left[c1]) - float(right[c1])
    if (b == 0):
      sys.exit(" Cannot Solve, pas d'inconnue : " + string)
    elif (a == 0):
      ft_math.ft_poly1(b, c)
    else:
      ft_math.ft_poly2(a, b, c)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='basic polynome equation solver')
  parser.add_argument("string", type=str, help="equation")
  parser.add_argument("-p", "--pretty", default=False, action="store_true",
                                       help="print equation in ast")
  parser.add_argument("-d", "--debug", default=False, action="store_true",
                                       help="print all operation")
  args = parser.parse_args()
  config.debug = args.debug
  test(args.string, args.pretty)
