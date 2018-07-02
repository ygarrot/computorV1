from ft_math import *
test = ft_math()
def reduce(tab):
    i = 0;
    while ((i + 3) < len(tab)):
        for op in test.prior:
            if ((i + 3) > len(tab)):
                break
            if (tab[i] is "="):
                i += 1;
            elif ((type(tab[i]) is int or tab[i].isdigit()) and tab[i + 1] == op and (type(tab[i + 2]) is int or tab[i + 2].isdigit())):
               if (op != "*" and len(tab) - i > 3 and tab[i + 3] == "*"):
                    i += 2
               else:
                    tab[i] = test.dic[tab[i + 1]](int(tab[i]), int(tab[i + 2]))
                    del tab[i + 1:i + 3]
            elif tab[i + 1] == op:
                i += 2
        i+=1;
    return(tab);

def reduced(tab):
    side = "right"
    val = [0, 0, 0]
    dec = 0
    i = 0
    deg  = 0
    while (i < len(tab)):
        if (tab[i] is "="):
            side = "l"
        elif (i + 2 < len(tab) and tab[i + 2] == "X"):
            deg = tab[i + 4] if tab[i + 4] > deg else deg
            val[int(tab[i + 4])] += int(tab[i]) if side is "right" else -int(tab[i])
            i += 4 
        elif tab[i].isdigit():
            dec += int(tab[i]) if side is "right" else -int(tab[i])
            i += 1;
        elif tab[i] == "X":
            if (len(tab) - i >= 2 and tab[i + 1] == "^"):
                deg = tab[i + 2] if tab[i + 2] > deg else deg
                val[int(tab[i + 2])] += 1
                i += 2
        i += 1;
    dec += val[0];
    if (deg == "2"):
        print("Polynomial degree: 2")
        test.ft_poly2(val[2], val[1], dec)
    elif (deg == "1"):
        print("Polynomial degree: 1")
        test.ft_poly1(val[1], dec)
    else:
        print(dec)

    #print(val, dec)
