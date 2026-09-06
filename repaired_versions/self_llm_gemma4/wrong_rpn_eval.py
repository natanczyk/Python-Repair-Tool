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
            # In RPN, the first item popped is the right operand, 
            # and the second item popped is the left operand.
            right = stack.pop()
            left = stack.pop()
            stack.append(
                op(token, left, right)
            )

    return stack.pop()