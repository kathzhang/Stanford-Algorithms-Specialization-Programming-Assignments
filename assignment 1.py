#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:39:07 2020

@author: apple
"""

#Karatsuba Multiplication: takes string as inputs
def ks_multi(x ,y):
    m=int(len(str(x)))
    n=int(len(str(y)))
    if(m/2<1) and (n/2<1):
        result=int(float(x))*int(float(y))
        return result
    else:
        a=x[:int((m/2))]
        b=x[int((m/2)):]
        c=y[:int((n/2))]
        d=y[int((n/2)):]
        result=int(10**m*ks_multi(a,c)+10**(int(float(m/2)))*(ks_multi(a,d)+ks_multi(b,c))+ks_multi(b,d))
        return result

ks_multi('35','87');


ks_multi('3141592653589793238462643383279502884197169399375105820974944592','2718281828459045235360287471352662497757247093699959574966967627');

