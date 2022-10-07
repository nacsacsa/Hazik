#!/usr/bin/env python
# coding: utf8

class Team():
    def __init__(self, nev, projekt, szerepkor):
        self.nev = nev
        self.projekt = projekt
        self.szerepkor = szerepkor
        print("-- Developer létrehozva. --")

    def __str__(self):
        return "{} a {}-en dolgozik {} szerepkörben.".format(self.nev,self.projekt,self.szerepkor)

    def __eq__(self, other_dev):
        return self.projekt == other_dev.projekt and self.nev != other_dev.nev

    def Ugyan_az_project():
        developers = [dev1, dev2, dev3 ,dev4]
        for dev in developers:
            for other_dev in developers:
                if dev == other_dev:
                    print("{} és {} dolgoznak egy projekten.".format(dev.nev,other_dev.nev))
            developers.remove(dev)

if __name__ == "__main__":

    dev1 = Team("Ricsi", "SolArch", "Fronted")
    print(dev1)
    dev2 = Team("Angéla", "ZerTeng", "Tesztelő")
    print(dev2)
    dev3 = Team("Peti", "KefERP", "Backend")
    print(dev3)
    dev4 = Team("Éva", "KefERP", "Fronted")
    print(dev4)
    print()
    Team.Ugyan_az_project()


                

