#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:20:40 2026

@author: alissadinsmore
"""

# Problem 3: Part Number and Unit Cost
part_number = input("Enter part number: ")
quantity = int(input("Enter quantity: "))

if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00

total_cost = quantity * unit_cost

print(f"\n{"Description":<18} {"Value":>12}")
print("-" * 31)
print(f"{"Part Number:":<18} {part_number:>12}")
print(f"{"Cost Per Unit:":<18} ${unit_cost:>11,.2f}")
print(f"{"Total Cost:":<18} ${total_cost:>11,.2f}")