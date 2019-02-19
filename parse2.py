import argparse
from lark import Lark, Transformer, v_args, Tree
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
        | UCASE_LETTER     -> var
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

@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from ft_math import ft_sum, ft_sub, ft_mul, ft_div, ft_neg, ft_pow2 as ft_pow
    number = float

    def __init__(self):
        self.vars = {}

def test(interactive=False):
    if (interactive == True):
      interactive_m.interactive()
      return
    calc_parser = Lark(calc_grammar, parser='lalr',debug=True, transformer=CalculateTree())
    string = """5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"""
    string = sys.argv[1]
    l_str, r_str = string.split("=")

    left = [0,0,0]
    right = [0,0,0]
    try:
        tmp = calc_parser.parse(r_str)
        right = config.unknown 
        right[c1] = tmp 
        config.unknown = [0, 0, 0]
        tmp = calc_parser.parse(l_str)
        left = config.unknown 
        left[c1] = tmp 
    except Exception as e:
        print(l_str, r_str)
        sys.exit(": parse error")
        # logging.error(traceback.format_exc())

    # print(right, left)
    # print(tree.pretty())
    # print(left[a1] - right[a1])

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
  parser = argparse.ArgumentParser(description='Smarter expert system you have ever seen')
  parser.add_argument("-i", "--interactive", default=False, action="store_true",
                                       help="interactive expert system")
  # args = parser.parse_args()
  test()
  # main()
