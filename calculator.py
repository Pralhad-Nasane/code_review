def calculateTax(income):
    if income > 50000:
        tax = income * 0.2
    else:
        tax = income * 0.1
    return tax
