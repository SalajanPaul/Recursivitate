def cautare_sir(sirprincipal, subsir):
    i = 0  # indice pt parcurgere sir principal
    n = len(sirprincipal) - len(subsir)  # cat de mult din sirul principal are rost sa parcurgem
    while i <= n:
        j = 0
        flg = True
        while flg and j < len(subsir):  # verific daca subsirul meu il gasesc in sir principal.Daca difera = ies
            if sirprincipal[i + j] != subsir[j]:
                flg = False
            j = j + 1
            # daca din while ul precedent s a iesit cu flg==true este posibil ca subsirul meu sa fi gasit
            # daca j == lungime subsirul meu atunci sigur am gasit potrivirea si pot iesi
        if flg and j == len(subsir):
            return 1
            # ma mut in sirul principal cu val lui j pt care nu am gasit potrivirea
        i = i + 1
    return -1


def adunare(n):         #1+2+3+4 = 10
    s = 0
    i = 1
    while i <= n:
        s = s + i
        i = i + 1
    return s

def adunarerec(n):                      #adunarerec(5) = 5 + adunarerec(4)
    if n <= 1:                          #adunarerec(4) = 4 + adunarerec(3)
        return 1
    else:
        return n + adunarerec(n-1)

def factrec(n):
    if n <= 1 :
        return 1
    else:
        return n * factrec(n-1)

if __name__ == '__main__':
    print(cautare_sir("masina", "sin"))
    # print(adunare(4))
    # print(adunarerec(4))
    # print(factrec(4))
