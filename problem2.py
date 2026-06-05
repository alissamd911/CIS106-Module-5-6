#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:18:28 2026

@author: alissadinsmore
"""

# Problem 2: Widget Quantity Schedule
quantity = int(input("Enter quantity of widgets: "))

if quantity > 10000:
    price = 10.00
elif 5000 <= quantity <= 10000:
    price = 20.00
else:
    price = 30.00

extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax

print(f"\n{"Description":<18} {"Value":>12}")
print("-" * 31)
print(f"{"Extended Price:":<18} ${extended_price:>11,.2f}")
print(f"{"Tax (7%):":<18} ${tax:>11,.2f}")
print(f"{"Total:":<18} ${total:>11,.2f}")