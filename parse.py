def bracket(tab, i):
    if (tab[i] != "("):
        return (0);
    i += 1
    while (i < lent):
        if (tab[i] == '('):
            i = bracket(tab, i);
            if (i <= 0):
                return (-1);
        elif (tab[i] == ')'):
            return (i + 1);
        elif (tab[i]):
            i += 1
    return (-1);

def conv(string):
    mathsplit = "=/*-+()^"
    test = string
    test = test.replace(" ", "")
    te = [];
    for op in mathsplit.split():
        for add in test.split(op):
            te += add
    return (te)
