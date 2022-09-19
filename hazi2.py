#!/usr/bin/env python
# coding: utf8

def main():
    print("Adjon meg egy számot és egy mértékegységet (cm/inch):")
    szam = input()
    mertek = input()
    if mertek == "cm":
        print(float(szam) * 2.54 , "inches")
    elif mertek == "inch":
        print(float(szam) / 2.54 , "cm")
    else:
        print("Not correct unit!")

if __name__ == "__main__":
	main()