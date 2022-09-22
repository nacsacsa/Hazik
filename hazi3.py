#!/usr/bin/env python
# coding: utf8

def haromszog_szerkezheto_e():
    print("Adja meg a háromyszög három oldalát cm-ben:")
    a_oldal = int(input("a oldal (cm): "))
    b_oldal = int(input("b oldal (cm): "))
    c_oldal = int(input("c oldal (cm): "))
    if c_oldal < a_oldal + b_oldal and b_oldal < a_oldal + b_oldal and a_oldal < b_oldal + c_oldal:
        szoveg_igaz = "A {}, {} és {} oldalú háromszög szerkezhető."
        print(szoveg_igaz.format(a_oldal, b_oldal, c_oldal))
    else:
        szoveg_hamis = "A {}, {} és {} oldalú háromszög NEM szerkezhető."
        print(szoveg_hamis.format(a_oldal, b_oldal, c_oldal))

if __name__ == "__main__":
	haromszog_szerkezheto_e()