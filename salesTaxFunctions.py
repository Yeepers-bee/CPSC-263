SALES_TAX_RATE: float = .06

def sales_tax(total):
    tax = total * SALES_TAX_RATE
    round(tax, 2)
    return tax



def total_after_tax(total, tax):
    tax_total = total + tax
    round(tax_total, 2)
    return tax_total
    
