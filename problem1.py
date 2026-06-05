#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:14:38 2026

@author: alissadinsmore
"""

# Problem 1: Quantity and Price
quantity = int(input("Enter the quantity: "))

if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

print(f"\n{"Description":<18} {"Value":>12}")
print("-" * 31)
print(f"{"Quantity:":<18} {quantity:>12,}")
print(f"{"Unit Price:":<18} ${unit_price:>11,.2f}")
print(f"{"Extended Price:":<18} ${extended_price:>11,.2f}")
print(f"{"Tax (7%):":<18} ${tax:>11,.2f}")
print(f"{"Total:":<18} ${total:>11,.2f}")