# !/usr/bin/python
import sys
from ft_math import ft_math as math
from parse import *
from exe import *
def main():
    tab = conv(sys.argv[1])#conv("8*2*X^2 = 4 *5+4*X^2")
    tab = reduce(tab);
    reduced(tab)
if __name__ == "__main__":
    main()
