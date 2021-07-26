#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:16:41 2020

@author: davidsheu
"""

'''
find the minimum fixed monthly payment needed to pay\
off a credit card balance in 12 months using bisection\
search
'''
balance = 320000    #should return 29157.09
subbalance = 320000
annualInterestRate = 0.2
monInterestRate = annualInterestRate/12.0
subbalance = balance        #proxy variable for balance
epsilon = .12           #margin of error allowed
lowerbound = balance/12
upperbound = (balance * (1 + monInterestRate)**12) / 12

#upperbound = (balance * (1 + monInterestRate)**12) / 12
minfixedpay = (lowerbound + upperbound)/2
i = 0 #i = number of iterations

while abs(subbalance) > epsilon:
    i += 1
    print('iteration:',i, 'minfixedpay =', minfixedpay)
     
    for i in range(12):
        unpaidbalance = subbalance - minfixedpay
        interest = unpaidbalance*(annualInterestRate/12.0)
        subbalance = unpaidbalance + interest 
        print('month:',i,"subbalance =",subbalance)
        #at the end of 12 months, subbalance ideally is < epsilon
        #i.e. the loan is paid off.  not too much or too little.
    
    if abs(subbalance) <= epsilon:
        print(minfixedpay)
        break
    
    else:
        if subbalance < 0:
            upperbound = minfixedpay
        else:
            lowerbound = minfixedpay
            
    subbalance = balance #resets balance
            
    minfixedpay = (lowerbound + upperbound)/2   #reevaluates our guess