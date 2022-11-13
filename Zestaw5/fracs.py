import math

def add_frac(frac1, frac2):
    divisor = math.lcm(frac1[1], frac2[1])
    frac_sum = [int(frac1[0]*divisor/frac1[1] + frac2[0]*divisor/frac2[1]), int(divisor)]
    return frac_sum

def sub_frac(frac1, frac2):
    divisor = math.lcm(frac1[1], frac2[1])
    frac_difference = [int(frac1[0] * divisor / frac1[1] - frac2[0] * divisor / frac2[1]), int(divisor)]
    return frac_difference

def mul_frac(frac1, frac2):
    dividend = frac1[0] * frac2[0]
    divisor = frac1[1] * frac2[1]
    greatest_common_divisor = math.gcd(dividend, divisor)
    frac_product = [int(dividend/greatest_common_divisor), int(divisor/greatest_common_divisor)]
    return frac_product

def div_frac(frac1, frac2):
    dividend = frac1[0] * frac2[1]
    divisor = frac1[1] * frac2[0]
    greatest_common_divisor = math.gcd(dividend, divisor)
    frac_quotient = [int(dividend/greatest_common_divisor), int(divisor/greatest_common_divisor)]
    return frac_quotient

def is_positive(frac):
    if (frac[0] < 0 and frac[1] < 0) or (frac[0] >= 0 and frac[1] >= 0):
        return True
    else:
        return False

def is_zero(frac):
    if frac[0] == 0 or frac[1] == 0:
        return True
    else:
        return False

def cmp_frac(frac1, frac2):
    divisor = math.lcm(frac1[1], frac2[1])
    frac1_numerator = frac1[0] * divisor / frac1[1]
    frac2_numerator = frac2[0] * divisor / frac2[1]
    if frac1_numerator == frac2_numerator:
        return 0
    elif frac1_numerator < frac2_numerator:
        return -1
    elif frac1_numerator > frac2_numerator:
        return 1

def frac2float(frac):
    return frac[0]/frac[1]