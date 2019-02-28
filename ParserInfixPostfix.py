# This program converts an infix expression to postfix expression
# Operators: ., |, *
# Include more operators eventually
# Algorithm reference: https://brilliant.org/wiki/shunting-yard-algorithm/

stack = []  # Used to store operations: https://dbader.org/blog/stacks-in-python
output = []  # used to store output: https://dbader.org/blog/queues-in-python
token = []  # used to store tokens being read in: https://dbader.org/blog/stacks-in-python

SYMBOLS = ['.', '|', '*']


def convert_infix_to_postfix(infix_expression):
    # while there are tokens to be read
    for i, e in enumerate(infix_expression):
        # read a token
        token = e
        # print(token)  # used to verify successful iterations

        # if token is 0 or 1.. will modify later to include better alphabet
        if token is 'a' or token is 'b' or token is 'c':
            # add to queue
            output.append(token)
            # print(output)

        # if token is operator
        elif token in SYMBOLS:
            stack.append(token)
            precedence = check_precedence(token)

            # check precedence
            if precedence == 2:
                output.append(stack.pop())
            elif precedence == 1 or precedence == 0:
                continue

        precedence = check_precedence(token)
        # check precedence
        if precedence == 1:
            output.append(stack.pop())

    output.append(stack.pop())
    return output


def check_precedence(input_token):
    if input_token is '*':
        return 2
    if input_token is '.':
        return 1
    if input_token is '|':
        return 0


convert_infix_to_postfix("a.(b.b)|a")
#convert_infix_to_postfix("(a|b).c")
print(output)
