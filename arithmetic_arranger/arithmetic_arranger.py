"""
This problem should follow certain rule
1. only less or equal to 5 operation are allowed, otherwise Error: Too many
problems.
2. only allowed to use + or -
3. number must only contain digits
4. number must cant be more than 4 digits
"""

def arithmetic_arranger(ls, state) -> list:
    # check length of list
    if len(ls) > 5:
        return "Error: Too many problems."
    
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    # check type of operations
    for prob in ls:
        num1, operation, num2 = prob.split(' ')
        lineMax = max(len(num1), len(num2)) + 2

        if operation not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # check for non-digits in number
        try:
            int(num1)
            int(num2)
        except ValueError:
            return "Error: Numbers must only contain digits."
            

        # for line 1
        line1.append((lineMax - len(num1))*' ' + num1)
        # for line 2
        line2.append(operation + (lineMax - len(num2) - 1)*' ' + num2)
        # for line 3
        line3.append(lineMax*'-')
        # for line 4
        if operation == '+':
            r = int(num1) + int(num2)
        else:
            r = int(num1) - int(num2)
        line4.append((lineMax - len(str(r)))*' ' + str(r))

        
    result = [ 
        '\t'.join(line1), 
        '\t'.join(line2), 
        '\t'.join(line3), 
        '\t'.join(line4) 
        ]
    if state == True:
        return '\n'.join(result)
