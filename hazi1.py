#!/usr/bin/env python
# coding: utf8

def main():

    mondat = input("Adjon meg egy mondatot: \n")
    betuk = {}
    for x in mondat:
        betuk[x] = 0
    for x in mondat:
        betuk[x] += 1

    print("Betűk gyakorisága: " , betuk)
    mondat_forditva = mondat[::-1]
    print("Fordítva: " , mondat_forditva)
    szavak_listaja = []
    szavak_listaja.extend(mondat.split(" "))
    print("Listába helyezve szavanként: " , szavak_listaja)

if __name__ == "__main__":
	main()
