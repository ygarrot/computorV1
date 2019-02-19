# !/usr/bin/python
import sys
# from ft_math import ft_math as math
from parse2 import *
# from exe import *

def main():
    # tab = conv(sys.argv[1])
    tab =conv("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
     
    tab = reduce(tab);
    reduced(tab)

if __name__ == "__main__":
    main()
