import sys
from math import ft_math as math
from parse import *
from exe import *
def main():
    tab = conv("8*2*X^2 = 4 *5")
    tab = reduce(tab);
    reduced(tab)
if __name__ == "__main__":
    main()
