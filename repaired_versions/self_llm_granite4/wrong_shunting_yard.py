def shunting_yard(tokens):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    rpntokens = []
    opstack = []
    for token in tokens:
        if isinstance(token, int):
            rpntokens.append(token)
        else:
            # Pop operators with greater or equal precedence before pushing the current one
            while opstack and precedence[token] <= precedence[opstack[-1]]:
                rpntokens.append(opstack.pop())
            opstack.append(token)  # push the current operator onto the stack

    # Pop any remaining operators from the stack
    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens