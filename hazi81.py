#!/usr/bin/env python
# coding: utf8


def buborek(lista):
    N = len(lista)
    for k in range(0, N):
        for i in range(1, N - k):
            if lista[i - 1] > lista[i]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
    print(lista)


def bin_kerese(lista, keresett_szam):
    kimenet = False
    szamlalo = 0
    N = len(lista)
    also, felso = 0, N-1
    while also <= felso:
        szamlalo = szamlalo + 1
        k = (felso + also) // 2
        print(lista[also], lista[k], lista[felso])
        if keresett_szam < lista[k]:
            felso = k - 1
        elif keresett_szam > lista[k]:
            also = k + 1
        else:
            kimenet = True, "index: " + str(k)
            break
    else: 
        kimenet = False 
    print("{}, lépések száma: {}".format(kimenet, szamlalo))


if __name__ == "__main__":
    szamok = [54, 76, 23, 45, 21, 5, 67, 22, 12, 64, 26, 59, 82, 99]
    buborek(szamok)
    bin_szamok = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]
    bin_kerese(bin_szamok, 70)