#Tax calculator
#Net Charge Income =  Total Income -Deductions(MPF) –Allowances(13200*n)
#Standard rate of income = Total Income -Deductions(MPF) * 15%

#MPF = if income>= 7100 or income<=30000, deduction = income*5% *12 months (each month not more than 1500)
# if income > 30000, deduction = 1500*12
#Deduction maximum = 18000

import numpy as np
import sys

def tax_calculator(income,who = 'YOU'):
    MAX_1 = 50000
    MAX_2 = 100000
    MAX_3 = 150000
    MAX_4 = 200000

    RATE_1 = 0.020
    RATE_2 = 0.060
    RATE_3 = 0.100
    RATE_4 = 0.140
    RATE_5 = 0.170
  
    income = int(income)
    if income < 7100 * 12 :
        deduction = 0
    elif 29999 * 12 > income > 7099 * 12:
        deduction = income * 0.05
    else:
        deduction = 1500 * 12
        
    #allowance
    allowance = 132000

    #net chargeable income
    net = (income - deduction - allowance)
    if net <0:
        net = 0

    if net < MAX_1:
        tax = RATE_1 * (net)
    elif net < MAX_2:
        tax = RATE_1 * MAX_1 + RATE_2 * (net - MAX_1)
    elif net < MAX_3:
        tax = RATE_1 * MAX_1 + MAX_2 * (MAX_2 - MAX_1) + \
                RATE_3 * (net - MAX_2)
    elif net < MAX_4:
        tax = RATE_1 * MAX_1 + RATE_2 * (MAX_2 - MAX_1) + \
        RATE_3 * (MAX_3 - MAX_2) + RATE_4 * (net - MAX_3)
    else:
        tax = RATE_1 * MAX_1 + RATE_2 * (MAX_2 - MAX_1) + \
                RATE_3 * (MAX_3 - MAX_2) + RATE_4 * (MAX_4 - MAX_3) + \
                RATE_5 * (net - MAX_4)
    #
    #Tax calculation with standard rate
    #
    sdtax = (income - deduction) * 0.15
    #Display the result
    print("Result:")
    print(" ")
    print("Income: $" + format(income,",.2f"))
    print(" ")
    print("Deduction(MPF) :$" + format(deduction, ",.2f"))
    print(" ")
    print("Allowance :$" + format(allowance, ",.2f"))
    print(" ")
    print("Net chargeable income $" + format(net, ",.2f"))
    print(" ")
    if tax < sdtax:
        print(f"TAX PAYABLE BY {who} :$" + format(tax, ",.2f"))
    else:
        print(f"TAX PAYABLE BY {who} (Standard rate) :$" + format(sdtax, ",.2f"))
    print(" ")
    print(" ")

    tax_payable = np.array([tax,sdtax]).min()
    return income, tax_payable, deduction

  
#
#Joint assessment
#
def joint_assesment(income1,income2,deduction1,deduction2):
    MAX_1 = 50000
    MAX_2 = 100000
    MAX_3 = 150000
    MAX_4 = 200000

    RATE_1 = 0.020
    RATE_2 = 0.060
    RATE_3 = 0.100
    RATE_4 = 0.140
    RATE_5 = 0.170
    
    allowance = 132000*2
    
    net3 = income1+income2-deduction1-deduction2-allowance

    if net3 < MAX_1:
        joint_tax = RATE_1 * (net3)
    elif net3 < MAX_2:
        joint_tax = RATE_1 * MAX_1 + RATE_2 * (net3 - MAX_1)
    elif net3 < MAX_3:
        joint_tax = RATE_1 * MAX_1 + MAX_2 * (MAX_2 - MAX_1) + \
                RATE_3 * (net3 - MAX_2)
    elif net3 < MAX_4:
        joint_tax = RATE_1 * MAX_1 + RATE_2 * (MAX_2 - MAX_1) + \
        RATE_3 * (MAX_3 - MAX_2) + RATE_4 * (net3 - MAX_3)
    else:
        joint_tax = RATE_1 * MAX_1 + RATE_2 * (MAX_2 - MAX_1) + \
                RATE_3 * (MAX_3 - MAX_2) + RATE_4 * (MAX_4 - MAX_3) + \
                RATE_5 * (net3 - MAX_4)
    
    print("Result:")
    print(" ")
    print(" ")

    print("JOINT ASSESSMENT")
    print(" ")
    print(" ")
    print("Total Deductions(MPF) :$" + format(deduction1 + deduction2, ",.2f"))
    print(" ")
    print("Total Allowances :$" + format(allowance, ",.2f"))
    print(" ")
    print("Total Net chargeable income :$" + format(net3, ",.2f"))
    print(" ")
    print("Total payable tax of this family under JOINT ASSESSMENT  :$" + format(joint_tax, ",.2f"))
    print(" ")
    print(" ")
    return joint_tax


income1 = input(f"Yearly Income of you:$")
if str(income1).lower() == 'y':
    sys.exit()
income2 = input(f"Yearly Income of your spouse (0 for no spouse) :$")
if str(income2).lower() == 'y':
    sys.exit()

try:
    assert int(income1) >= 0 , "ERROR: Input must be a positive number, please try again"
    assert int(income2) >= 0 , "ERROR: Input must be a positive number, please try again"
    income1, tax_payable1, deduction1 = tax_calculator(income1)
    income2, tax_payable2, deduction2 = tax_calculator(income2,'your spouse')
    joint_tax = joint_assesment(income1,income2,deduction1,deduction2)

    septax= tax_payable1+tax_payable2
    print("Total payable tax of this family under SEPERATE ASSESSMENT $" + format(septax, ",.2f"))
    print(" ")
    print(" ")
    #
    #Recommandation
    #
    print("Recommendation:")
    if septax > joint_tax:
        print("JOINT ASSESSMENT is recommended, ",
            "which saved you $" + format(septax - joint_tax, ",.2f"))
    else:
        print("SEPERATE ASSESSMENT is recommended, ",
            "which saved you $" + format(joint_tax - septax, ",.2f"))
except ValueError:
    print("ERROR: Input must be a number, please try again")

