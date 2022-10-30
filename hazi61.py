#!/usr/bin/env: python
# coding: utf8

def szorzas_tabla():
    elrendezes = "{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}"
    print(elrendezes.format("","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
    print("   :------------------------------------------------")
    for x in range(1,13):
        print(elrendezes.format("{}:".format(x), x * 1, x * 2, x * 3, x * 4, x *  5, x * 6, x * 7, x * 8, x * 9, x * 10, x * 11, x * 12))


if __name__ == "__main__":
    szorzas_tabla()