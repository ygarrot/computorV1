class ft_math:

    ft_sum(a, b):
        return (a + b)
    
    ft_sub(a, b):
        return (a - b)

    ft_mult(a, b):
        return (a * b)
    
    ft_div(a, b):
        return(a / b)
    
    ft_modu (a, b):
        return (a % b)
    
    ft_abs(a)
        return (a < 0 ? -a : a);

    ft_sqrt(a):
        i = 0
        if (!a)
            return (0);
        while (i * i  < a)
            i++;
        return (i % nb ? 0 : i)
        
    ft_pow(a, b):
        if (!b):
            return (1);
        if (b == 1):
            return (a);
        return (ft_pow(a  * a, b - 1))

    ft_poly2(a, b, c)
        delta = ft_pow(b, 2) - 4 * a * c;

        if (delta < 0)
            print("Discriminant is strictly negative, the two solutions are:");
            x1 = (-b / 2 * a) - (delta /2 * a)
            print(x1, "i / ",  2 * a);
            x2 = (-b / 2 * a) + (delta /2 * a)
            print(x2, "i / ",  2 * a);
 
        else if (!delta)
            print("Discriminant is NULL, the solution is:");
            x1 = -b / 2a
            print(x1);
            #x2 = x1
        else
            print("Discriminant is strictly positive, the two solutions are:");
            x1  = (-b + ft_sqrt(delta)) / 2 * a;
            x2  = (-b - ft_sqrt(delta)) / 2 * a;
            print (x1, x2);
