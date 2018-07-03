import math
class ft_math:
    def __init__(self):
        self.prior = "(^*%/+-"
        self.dic ={};
        self.dic["+"] = self.ft_sum
        self.dic["-"] = self.ft_sub
        self.dic["*"] = self.ft_mult
        self.dic["/"] = self.ft_div
        self.dic["%"] = self.ft_modu
        self.dic["^"] = self.ft_pow
    def ft_sum(self, a, b):
        return (a + b)
    
    def ft_sub(self, a, b):
        return (a - b)

    def ft_mult(s, a, b):
        return (a * b)
    
    def ft_div(s, a, b):
        return(a / b)
    
    def ft_modu (s, a, b):
        return (a % b)
    
    def ft_abs(s, a):
        return (-a if a < 0  else  a);

    def ft_sqrt(s, a):
        i = 1
        if (a == 0):
            return (0);
        while (i * i  < a):
            i += 1
        print(i, a)
        return (i if (i % a) == 0 else 0)
        
    def ft_pow(s, a, b):
        if (b is False):
            return (1);
        if (b == 1):
            return (a);
        return (a * s.ft_pow(a , b - 1))

    def ft_poly1(self, a, b):
        x = float(-b) / float(a);
        print ("The solution is " + str(x))
    def ft_poly2 (self, a, b, c):
        delta = self.ft_pow(b, 2.0) - (4.0 * a * c);
        den = 2 * a

        if (delta < 0):
            print("Discriminant is strictly negative, the two solutions are:");
            x1 = (-b / den) - (delta / den)
            print x1, "+ i /", den;
            x2 = (-b / den) + (delta / den)
            print x2, "- i /",  den;
 
        elif (delta is False):
            print("Discriminant is NULL, the solution is:");
            x1 = -b / 2 * a
            print(x1);
            #x2 = x1
        else:
            print("Discriminant is strictly positive, the two solutions are:");
            r = math.sqrt(delta)
            x1  = (-b - r) / den;
            x2  = (-b + r) / den;
            print (str(x1) + "\n" +  str(x2));
