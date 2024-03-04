import sys
from __future__ import annotations
balance =0

def getMenuOption():
    global option
    print('Please select an option:\n1. Deposit\n2.Withdraw\n3.Balance\n4.End')
    option = int(input())
    return option


def Deposit():
    global balance
    amount = input('Please select amount to deposit:')
    balance += int(amount)
    print('Amount deposited is ' + amount)
    return

def Withdraw():
    global balance
    amount = input('Please select amount to withdraw:')
    balance -= int(amount)
    print('Amount withdrawn is ' + amount)
    return

def Balance():
    global balance
    print('Your current balance is: '+str(balance)+'.')
    return

def End():
    sys.exit()
    
    


