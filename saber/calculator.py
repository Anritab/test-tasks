def is_operator(token):
    return token in ['+', '-', '*', '/']

#последовательность операций
def precedence(operator):
    if operator in ['+', '-']:
        return 1
    elif operator in ['*', '/']:
        return 2
    return 0

#перевод в обратную польскую запись
def infix_to_rpn(expression):
    output = []
    stack = []

    for token in expression:
        if token.isdigit():
            output.append(token)
        elif is_operator(token):
            while stack and is_operator(stack[-1]) and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return output

#подсчет обратной польской записи
def evaluate_rpn(expression):
    stack = []

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        elif is_operator(token):
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            elif token == '/':
                stack.append(num1 / num2)

    return stack[0]

#вызов всех функций
input_expression = input()
expression_without_spaces = ''.join(input_expression.split())
rpn_expression = infix_to_rpn(expression_without_spaces)
result = evaluate_rpn(rpn_expression)

print(result)
