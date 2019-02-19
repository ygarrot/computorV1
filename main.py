import argparse
from lark import Lark, Transformer, v_args, Tree
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
        | sum "=" sum    -> assign_var

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
    from ft_math import ft_sum, ft_sub, ft_mul, ft_div, ft_neg
    number = float

    def __init__(self):
        self.vars = {}

    # def assign_var(self, name, value):
        # self.vars[name] = value
        # return value

    # def var(self, name):
        # return self.vars[name]

# def set_fact(tree):
#   ifact = tree.find_data("initial_fact")
#   for fact in ifact:
#      computer.iter_subtree(fact)

def test(interactive=False):
    if (interactive == True):
      interactive_m.interactive()
      return
    calc_parser = Lark(calc_grammar, parser='lalr',debug=True, transformer=CalculateTree())
    calc_parser2 = Lark(calc_grammar, parser='lalr',debug=True)
    string = """5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"""
    print(string)
    try:
        tree = calc_parser.parse(string)
        # t = calc_parser2.parse(string)
    except Exception as e:
        logging.error(traceback.format_exc())
        return
    # print(t.pretty())
    print(tree.pretty())
    ft_math.ft_poly2(unknown[1][val], unknown[0][val], 4)
    return 
    al = list(tree.iter_subtrees())
    for truc in al:
        print(truc)

                
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Smarter expert system you have ever seen')
  parser.add_argument("-i", "--interactive", default=False, action="store_true",
                                       help="interactive expert system")
  args = parser.parse_args()
  test(args.interactive)
  # main()
