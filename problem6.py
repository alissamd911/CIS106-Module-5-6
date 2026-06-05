#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:32:29 2026

@author: alissadinsmore
"""

# Problem 6: Employee Bonus (Corrected Print Block)
last_name = input("Enter employee last name: ")
salary = float(input("Enter salary: "))
job_level = int(input("Enter job level: "))

if job_level >= 10:
    bonus_rate = 0.25
elif 5 <= job_level <= 9:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

bonus = salary * bonus_rate

# The fix is right here: "Employee:" has a colon now!
print(f"\n{"Description":<18} {"Value":>14}")
print("-" * 34)
print(f"{"Employee:":<18} {last_name:>14}")
print(f"{"Bonus Amount:":<18} ${bonus:>13,.2f}")