#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:30:48 2026

@author: alissadinsmore
"""

# Problem 5: Concert Tickets
tickets = int(input("Enter number of concert tickets: "))

if tickets >= 25:
    price_per_ticket = 50.00
elif 10 <= tickets <= 24:
    price_per_ticket = 60.00
elif 5 <= tickets <= 9:
    price_per_ticket = 70.00
else:
    price_per_ticket = 75.00

total_cost = tickets * price_per_ticket

print(f"\n{"Description":<22} {"Value":>12}")
print("-" * 35)
print(f"{"Number of Tickets:":<22} {tickets:>12,}")
print(f"{"Price Per Ticket:":<22} ${price_per_ticket:>11,.2f}")
print(f"{"Total Cost:":<22} ${total_cost:>11,.2f}")