def splitter(expr):
    if '+' in expr:
        worklist = expr.split('+')
        worklist[0] = int(worklist[0])
        worklist[1] = int(worklist[1])
        worklist.append('+')
        return worklist
    elif '-' in expr:
        worklist = expr.split('-')
        worklist[0] = int(worklist[0])
        worklist[1] = int(worklist[1])
        worklist.append('-')
        return worklist    
    elif '*' in expr:
        worklist = expr.split('*')
        worklist[0] = int(worklist[0])
        worklist[1] = int(worklist[1])
        worklist.append('*')
        return worklist
    elif '/' in expr:
        worklist = expr.split('/')
        worklist[0] = int(worklist[0])
        worklist[1] = int(worklist[1])
        worklist.append('/')
        return worklist

def math(num_list):
    if num_list[2] == '+':
        result = num_list[0] + num_list[1]
        return result
    elif num_list[2] == '-':
        result = num_list[0] - num_list[1]
        return result
    elif num_list[2] == '*':
        result = num_list[0] * num_list[1]
        return result
    elif num_list[2] == '/':
        result = int(num_list[0] / num_list[1])
        return result
    else:
        print('wrong operator!')
