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
        i = 0
        if (a is False):
            return (0);
        while (i * i  < a):
            i+=1
        return (0 if i % nb else i)
        
    def ft_pow(s, a, b):
        if (b is False):
            return (1);
        if (b == 1):
            return (a);
        return (a * s.ft_pow(a , b - 1))

    def ft_poly2(s, a, b, c):
        delta = ft_pow(b, 2) - 4 * a * c;

        if (delta < 0):
            print("Discriminant is strictly negative, the two solutions are:");
            x1 = (-b / 2 * a) - (delta /2 * a)
            print(x1, "i / ",  2 * a);
            x2 = (-b / 2 * a) + (delta /2 * a)
            print(x2, "i / ",  2 * a);
 
        elif (delta is False):
            print("Discriminant is NULL, the solution is:");
            x1 = -b / 2 * a
            print(x1);
            #x2 = x1
        else:
            print("Discriminant is strictly positive, the two solutions are:");
            x1  = (-b + ft_sqrt(delta)) / 2 * a;
            x2  = (-b - ft_sqrt(delta)) / 2 * a;
            print (x1, x2);
