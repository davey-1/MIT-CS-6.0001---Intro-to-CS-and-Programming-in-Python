#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:27:04 2020

MIT CS6.0001 F16 

Problem Set 1

@author: davidsheu
"""


"""Part C"""

"""Situation: given the below assumptions/initializations,

calculate the savings rate needed (as a decimal) to afford the down payment"""


"""assume semi-annual raise is 7%, *after* each 6th month"""
semi_annual_raise = 0.07


"""assume annual return on investment is 4%, compounded monthly"""
r = 0.04 

"""assume down payment = 25%"""
portion_down_payment = 0.25

"""assume cost of house to save for is $1M"""
total_cost = 1000000

down_payment = portion_down_payment*total_cost

""" Optional input (add current savings) , set to 0 instead
current_savings = int(input("Enter your current savings: "))
"""
current_savings = 0

"""set number of months intended to save for down payment to 36"""
num_months_total = 36

"""more initializations for bisectional search"""
"""the guess is on savings rate aka portion_saved"""
num_guesses = 0
epsilon = 100
low = 0

"""100 percent to 2 decimal places, cast back into float later"""
high = 10000

"""first guess for portion_saved"""
guess = int((high-low)/2)


annual_salary = int(input("Enter your annual salary: "))

ann_sal_placeholder = annual_salary


while abs(current_savings - down_payment) > epsilon:

    annual_salary = ann_sal_placeholder
    current_savings = 0

    """line below states guess number"""
    """print("guess #",num_guesses,"=",str(float((guess/10000)*100))+"%")"""
    
    """calculates total savings over 36 months"""
    for num_months in range(1,num_months_total+1):
        current_savings = int(current_savings + annual_salary*guess/10000/12 + current_savings*r/12)
        if num_months % 6 == 0:
            annual_salary = annual_salary*(1+semi_annual_raise)
            
            """line below checks current savings given the estimated savings rate ('guess') """
            """print("guess #",num_guesses,"savings after",num_months+1,"months =",current_savings) """

    num_guesses = num_guesses + 1


    """Success case!!!"""    
    if abs(current_savings - down_payment) <= epsilon:
        print("Best savings rate:", str(float((guess/10000)*100))+"%")

        print("Steps in bisection search:", num_guesses)

        break
    
    """Bisectional Search"""
    if current_savings > down_payment:   
        high = guess
    else:
        low = guess

    guess = int((high + low)/2)

    """salary insufficient to save up for down payment within three years...rough guess"""        
    if guess > 9990:
        print("It is not possible to pay the down payment in three years.")
        break
    
    if num_guesses == 20:
        print("Number of guesses has exceeded 20.")
        break
        



"""end Part C"""