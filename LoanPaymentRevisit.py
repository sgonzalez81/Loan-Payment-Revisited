# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:26:36 2022

@author: salva
"""

import numpy as np

Pmt = float(input('input payment -> '))

rAPR = float(input('input intrest rate, APR -> '))
rDEC = rAPR/1200 # 1200 because monthly pmts
nMonths = int(input('number of months to pay off -> '))

PV = Pmt/rDEC*(1 - (1+rDEC)**(-nMonths))

print(f"for APR={rAPR :.2f}, Pmt = {Pmt :.2f}, number of months = {nMonths :d}")
print(f"Amount you can borrow is {PV :.2f}")

if PV < 20000:
    print('sorry, you gotta buy a used car')
elif PV < 30000:
    print('you can get a Kia Seltos')
else:
    print("you got enough $$ for a Tesla")