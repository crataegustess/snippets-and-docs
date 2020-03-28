def convert_to_dec(roman: str):
    # best to use regex to solve
    if len(roman) == 1:
        if roman == 'V':
            return 5
        elif roman == 'X':
            return 10
        elif roman == 'I':
            return 1
    return 0

littlest_cyphers = {'3':'III','2':'II','1':'I'}

def check_modulo(previous_remainder:int, divisor:int, symbol:str):
    result = ''
    if previous_remainder < divisor:
        return (previous_remainder,'')
    if previous_remainder < 4:
        return (0,littlest_cyphers[str(previous_remainder)])
    mod = previous_remainder % divisor
    num = (previous_remainder - mod) / divisor
    while num > 0:
        result += symbol
        num -= 1

    return (mod,result)

cyphers = [(1000,'M'),(900,'CM'),(600,'DC'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(60,'LX'),(50, 'L'),(40, 'XL'),(10, 'X'),(9,'IX'),(6,'VI'), (5,'V'),(4,'IV'),(1,'I')]

def convert_to_roman(num: int):
    # best to use modulo to solve
    result = ''
    for (divisor,symbol) in cyphers:
        (new_remainder,additional_symbols) = check_modulo(num,divisor,symbol)
        result += additional_symbols
        num = new_remainder
        if new_remainder == 0:
            return result

    return "unable to compute roman representation"

import timeit
print(timeit.timeit(stmt='convert_to_roman(1876)', number=10, globals=globals()))
