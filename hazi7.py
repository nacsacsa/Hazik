#!/usr/bin/env python
# coding: utf8

import string


def szoveg_rombolas(szoveg):
    uj_szoveg = []
    massalhangzok = "qwrtzpsdfghjklyxcvbnmQWRTZPSDFGHJKLYXCVBNM"
    with open(szoveg, "r", encoding="utf8") as file:
        sor = file.readline()
        while sor:
            egysor = ""
            for betu in sor:
                if betu not in string.punctuation and betu != " " and betu in massalhangzok:
                    egysor += betu
            if egysor != "":
                uj_szoveg.append(egysor)
            sor = file.readline()

        with open("rombolt.txt", "w", encoding="utf8") as kesz_file:
            for szam, sor in enumerate(uj_szoveg):
                if (szam + 1) % 3 == 0:
                    kesz_file.write(sor + "\n")


if __name__ == "__main__":
    szoveg_rombolas("hazi.txt")