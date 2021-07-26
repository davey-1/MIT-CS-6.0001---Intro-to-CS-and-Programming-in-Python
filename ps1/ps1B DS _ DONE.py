#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:27:04 2020

MIT CS6.0001 F16 

Problem Set 1

@author: davidsheu
"""


"""Part B"""


"""assume down payment = 25%"""
portion_down_payment = 0.25


"""assume annual return on investment is 4%, compounded monthly"""
r = 0.04 



current_savings = int(input("Enter your current savings: "))

annual_salary = int(input("Enter your annual salary: "))

portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

total_cost = int(input("Enter your the cost of your dream home: "))

semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

""" Add compounding equation to current monthly savings """

num_months = 0

while current_savings < portion_down_payment*total_cost:
    current_savings = int(current_savings + annual_salary*portion_saved/12 + current_savings*r/12)
    num_months = num_months + 1
    if num_months % 6 == 0:
        annual_salary = annual_salary*(1+semi_annual_raise)
        
print("Number of monnths:", num_months)

"""end Part B"""