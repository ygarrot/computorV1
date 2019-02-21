import numpy as np
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
        | sum "=" sum -> ft_sub

    ?sum: product
        | sum "+" product    -> ft_sum
        | sum "-" product     -> ft_sub

    ?product: pow
        | product "*" pow        -> ft_mul
        | product "/" pow        -> ft_div

    ?pow: atom
        | pow "^" atom      -> ft_pow

    ?atom: DECIMAL        ->int_to_array
        | INTEGER         ->int_to_array
        | UCASE_LETTER    ->unknown
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

def more(tree):
  trees = list(tree.iter_subtrees())
  for tree in trees:
    print(tree.children)

def pretty_mode(tree):
     print("\nPretty mode\n~~~~~~~~~~~~~~~~~~~~~~\n")
     print(tree.pretty(pstr))
     print("~~~~~~~~~~~~~~~~~~~~~~\ndone")

@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from ft_math import ft_sum, ft_sub, ft_mul, ft_div, ft_neg, ft_pow2 as ft_pow, unknown, int_to_array
    number = float

    def __init__(self):
        self.vars = {}

def test(equation, is_pretty=False):
    calc_parser = Lark(calc_grammar, parser='lalr',debug=True, transformer=CalculateTree())
    pretty = Lark(calc_grammar, parser='lalr',debug=True)
    string = equation 

    try:
        tmp2 = pretty.parse(string)
        X = calc_parser.parse(string)
    except UnexpectedInput as it:
        print("there is an error in parsing(handled error):\n", file=sys.stderr)
        sys.exit(it)
    except Exception as e:
        print("there is an error in parsing:", file=sys.stderr)
        print(string, e, file=sys.stderr)
        sys.exit()

    if (is_pretty is True):
      pretty_mode(tmp2)

    c, b, a = X
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
  # parser.add_argument("-d", "--debug", default=False, action="store_true",
                                       # help="print all operation")
  args = parser.parse_args()
  # config.debug = args.debug
  test(args.string, args.pretty)
