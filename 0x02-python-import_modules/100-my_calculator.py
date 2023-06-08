#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    argc = len(args)

    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    
    a = arga[1]
    op = args[2]
    b = args[3]
    result = 0
     if op == '+':
         result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op = '/':
        result = div(a, b)
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    print(f"{a:d} {op} {b:d} = {result:d}")
