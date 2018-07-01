from math import ft_math
test = ft_math()
def reduce(tab):
    i = 0;
    while ((i + 3) < len(tab)):
        for op in test.prior:
            if ((i + 3) > len(tab)):
                break
            if (tab[i] is "="):
                i += 1;
            if ((type(tab[i]) is int or tab[i].isdigit()) and tab[i + 1] == op and (type(tab[i + 2]) is int or tab[i + 2].isdigit())):
                tab[i] = test.dic[tab[i + 1]](int(tab[i]), int(tab[i + 2]))
                del tab[i + 1:i + 3]
            elif tab[i + 1] == op:
                i += 2
        i+=1;
    return(tab);

def reduced(tab):
    side = "right"
    val = [0, 0, 0]
    dec  = 0 
    i = 0
    print(tab)
    while (i < len(tab)):
        if (i is "="):
            side = "l"
        if (i + 2 < len(tab)):
            if (tab[i + 2] == "X"):
                val[int(tab[i + 4])] += int(tab[i]) if side is "right" else -int(tab[i])
            i += 5 
        else:
            dec += int(tab[i]) if side is "right" else -int(tab[i])
        i += 1;
    test.ft_poly2(5.0, 4.0, -9.3)
    print(val, dec)
