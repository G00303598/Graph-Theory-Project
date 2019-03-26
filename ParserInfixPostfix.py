# This program converts an infix expression to postfix expression
# Author: Morgan Reilly - G00303598

# Algorithm references:
# https://brilliant.org/wiki/shunting-yard-algorithm/
# https://web.microsoftstream.com/video/a29536d4-e975-4172-a470-40b4fe28866e


def convert_infix_to_postfix(infix_expression):
    stack = []  # Shunting store: https://dbader.org/blog/stacks-in-python
    output = []  # used to store output: https://dbader.org/blog/queues-in-python
    symbols = {'^': 40, '?': 30, '*': 30, '+': 20, '-': 20, '.': 20, '|': 10}  # define operators to be included in dictionary

    print("INFIX: ", infix_expression)

    # loop through input
    for i, token in enumerate(infix_expression):
        # right bracket encountered
        if token is '(':
            stack.append(token)  # add token to stack
        # left bracket encountered
        elif token is ')':
            # until left bracket append output with top of stack
            # then pop from stack
            while stack[-1] is not '(':
                output.append(stack[-1])
                del stack[-1]  # del stack[-1] is equivalent to stack.pop()
            # left bracket encountered, pop from stack
            del stack[-1]
        # operator encountered
        elif token in symbols:
            # while stack has a operator of greater precedence than input
            while stack and symbols.get(token, 0) <= symbols.get(stack[-1], 0):
                output.append(stack[-1])
                del stack[-1]
            # push lesser operator to stack
            stack.append(token)
        # token is alphanumeric
        else:
            output.append(token)
    # clear remainder on stack
    while stack:
        output.append(stack[-1])
        del stack[-1]

    # print(output)  # prints as list
    # print("POSTFIX: ", ''.join(output))  # prints as string
    postfix_expression = ''.join(output)
    return postfix_expression  # returns as string


# Tests from: http://www.oxfordmathcenter.com/drupal7/node/628
# convert_infix_to_postfix("A*B+C")  # Test 1 -- A B * C +
# convert_infix_to_postfix("A+B*C")  # Test 2 -- A B C * +
# convert_infix_to_postfix("A*(B+C)")  # Test 3 -- A B C + *
# convert_infix_to_postfix("A-B+C")  # Test 4 -- A B - C +
# convert_infix_to_postfix("A*B^C+D")  # Test 5 -- A B C ^ * D +
# convert_infix_to_postfix("A*(B+C*D)+E")  # Test 6 -- A B C D * + * E +
# print("POSTFIX: ", convert_infix_to_postfix("(0|(1(01*(00)*0)*1)*)*"))
print("Postfix: ", convert_infix_to_postfix("a+b"))