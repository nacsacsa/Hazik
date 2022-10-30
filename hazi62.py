#!/usr/bin/env python
# coding: utf8
import string

def ly_bol_j(szoveg):
    szamlalo = 0
    uj_szoveg = ""
    while szamlalo < len(szoveg):
        ketto = ""
        if szamlalo != len(szoveg) - 1:
            ketto = szoveg[szamlalo] + szoveg[szamlalo + 1]
        if ketto == "ly":
            uj_szoveg += "j"
            szamlalo += 1
        else:
            uj_szoveg += szoveg[szamlalo]
        szamlalo += 1
    return uj_szoveg

def kiszedes(szoveg):
    negyszeres_massalhangzok = {"ygyg": "ygg", "ynyn": "ynn", "zszs": "zss", "ytyt": "ytt", "scsc": "scc"}
    negyszeres_massalhangzok_normal = {"gygy": "gyy", "nyny": "nny", "szsz": "ssz", "tyty": "tty", "cscs": "css"}
    uj_szoveg = ""
    szamlalo = 0
    while szamlalo < len(szoveg):
        negy = ""
        if szamlalo < len(szoveg) - 3:
            negy = szoveg[szamlalo] + szoveg[szamlalo + 1] + szoveg[szamlalo + 2] + szoveg[szamlalo + 3]
        if negy in negyszeres_massalhangzok.keys():
            for x, y in negyszeres_massalhangzok.items():
                if negy == x:
                    uj_szoveg += y
                    szamlalo += 3
                    break
        elif negy in negyszeres_massalhangzok_normal.keys():
            for x, y in negyszeres_massalhangzok_normal.items():
                if negy == x:
                    uj_szoveg += y
                    szamlalo += 3
                    break
        else:
            uj_szoveg += szoveg[szamlalo]
        szamlalo += 1
    return uj_szoveg

def palindrom(szoveg):
    uj_szoveg1 = ""
    uj_szoveg2 = ""
    uj_szoveg3 = ""
    szamlalo = 0
    maganhangzo_csere = {"a": "á", "e": "é", "i": "í", "o": "óöő", "u": "úüű"}
    dupla_massalhangzok = ["dz", "gy", "ny", "sz", "ty", "zs", "cs", "ly"]
    tripla_massalhangzok = ["dzs", "ggy", "nny", "ssz", "tty", "css"]

    for x in szoveg:
        if x not in string.punctuation and x != " ":
            uj_szoveg1 += x.lower()

    for i in uj_szoveg1:
        if i not in "áéíóöőúüű":
            uj_szoveg2 += i
        else:
            for x, y in maganhangzo_csere.items():
                if i in y:
                    uj_szoveg2 += x
                    break

    while szamlalo < len(uj_szoveg2):
        ketto = ""
        harom = ""
        if szamlalo != len(uj_szoveg2) - 1:
            ketto = uj_szoveg2[szamlalo] + uj_szoveg2[szamlalo + 1]
        if szamlalo < len(uj_szoveg2) - 2:
            harom = uj_szoveg2[szamlalo] + uj_szoveg2[szamlalo + 1] + uj_szoveg2[szamlalo + 2]
        if harom in tripla_massalhangzok:
                uj_szoveg3 += harom[::-1]
                szamlalo += 2
        elif ketto in dupla_massalhangzok:
                uj_szoveg3 += ketto[::-1]
                szamlalo += 1
        else:
            uj_szoveg3 += uj_szoveg2[szamlalo]
        szamlalo += 1

    teljes_normal = kiszedes(uj_szoveg2)
    teljes_vissza = kiszedes(uj_szoveg3)[::-1]

    if "ly" in teljes_normal:
        teljes_normal = ly_bol_j(teljes_normal)
        teljes_vissza = ly_bol_j(teljes_vissza)

    if teljes_normal == teljes_vissza:
        print("palindrom!")
    else:
        print("NEM palindrom!")

if __name__ == "__main__":
    palindrom("arany nyara")
    palindrom("Ennyi dinnye!")
    palindrom("A sári pap írása.")
    palindrom("Emez égi lakkozó placcra, távol Afrika fölé, néger regén élő fakír falovát arccal, pózokkal igézem-e?")
    palindrom("Ön óv Ottót, a vak asszír is. Rí szotyoladobó, bánt is e mentolos út. Táci e régi bor, a vakolatjel, ó, néz rám székilile-szem. Eldob a hatóság agya, kelet rekkenő híre, botkocsány. Ég el a bálozó, rí vargabetű, tar ausztrál vekni. Csikósé a bér, ó, halkan hasít Elek. Panel, Ági-ridikül lemarad, óh, ki se lógat Nagy Ernő, ó, Ida, magőr ő. Cserre néző kósza lett erők, mór kajakosok, tufa te is, a járóletét gélelegye is ómódi. Kis, ámori patak a bálon a horkantó, Benőt, agutit, Natit, Antit ugat. Ön e botnak rohanó láb. A Kata-pír, ó, másik idom, ó, sí, egyel elégtétel órája. Siet a futkosó kaja króm körettel, a szóközén erre csörög ama dió. Önre gyantagól esik, hódaramellű, ki dirigál e napkeleti sahnak Lahoréba. És, ó, kicsin kevlárt szú arat, üt, eb, a gravírozó lába. Legényács, októberi hőnek kertelek agyagásót. A habod lemeszel, Ili, kész már Zénó. Lejt a ló kavaró bigére, Icát, tusolót nemesít nábobod. A lotyó szír, s Írisz szakavatott óvónő.")