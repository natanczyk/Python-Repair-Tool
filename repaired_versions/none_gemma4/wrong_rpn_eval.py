def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }[symbol](a, b)

    stack = []

    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        else:
            # In RPN, the first operand popped is the right operand, 
            # and the second operand popped is the left operand.
            b = stack.pop()
            a = stack.pop()
            stack.append(
                op(token, a, b)
            )

    return stack.pop()