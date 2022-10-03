#!/usr/bin/env python
# coding: utf8

class Team():
    def __init__(self, nev, project, szerepkor):
        self.nev = nev
        self.project = project
        self.szerepkor = szerepkor
        print("-- Developer létrehozva. --")

    def __str__(self):
        return self.nev + " a " + self.project + "-en dolgozik " + self.szerepkor + " szerepkörben."

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

    developers = [dev1, dev2, dev3 ,dev4]
  
    for dev in developers:
        for other_dev in developers:
            if dev.project == other_dev.project and dev.nev != other_dev.nev:
                print(dev.nev + " és " + other_dev.nev + " dolgoznak egy projekten.")
        developers.remove(dev)

                

