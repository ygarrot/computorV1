class ft_math:

    ft_sum(a, b):
        return (a + b)
    
    ft_sub(a, b):
        return (a - b)

    ft_mult(a, b):
        return (a * b)
    
    ft_div(a, b):
        return(a / b)
    
    ft_mode (a, b):
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
        return (this.pow(a  * a, b - 1))

    ft_poly(a, b, c)
        delta = ft_pow(b, 2) - 4 * a * c;

        if (delta < 0)
            break ;
        else if (!delta)
            x1 = -b / 2a
            x2 = x1
        else
            x1  = (-b + ft_sqrt(delta)) / 2 * a;
            x1  = (-b - ft_sqrt(delta)) / 2 * a;
