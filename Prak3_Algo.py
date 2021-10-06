# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 08:32:46 2021

@author: Rudolf
"""
kecil = int(input("Masukkan angka pertama : "))
besar = int(input("Masukkan angka terkahir : "))

while kecil and kecil <= besar:
    print(kecil, besar)
    kecil += 1
    besar -= 1

