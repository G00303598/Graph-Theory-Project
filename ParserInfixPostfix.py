# This program converts an infix expression to postfix expression
# Operators: ., |, *
# Include more operators eventually
# Algorithm reference: https://brilliant.org/wiki/shunting-yard-algorithm/

from collections import deque
stack = []  # Used to store operations: https://dbader.org/blog/stacks-in-python
output = deque()  # used to store output: https://dbader.org/blog/queues-in-python
token = []  # used to store tokens being read in: https://dbader.org/blog/stacks-in-python

SYMBOLS = ['.', '|', '*']


def convert_infix_to_postfix(infix_expression):
    # while there are tokens to be read
    for i, e in enumerate(infix_expression):
        token = e
        # print(token)  # used to verify successful iterations

        # if token is 0 or 1.. will modify later to include better alphabet
        if token is '0' or token is '1':
            # add to queue
            output.append(token)
            # print(output)

        # if token is operator
        #
        if token in SYMBOLS:
            # check precedence
            for i in stack:
                if token:
                    output.append(stack.pop())
            stack.append(token)

    print(stack)
    print(output)

    for i in stack:
        output.append(stack.pop())
    print(output)


def check_precedence(input_token):
    if input_token is '*':
        return 2
    if input_token is '.':
        return 1
    if input_token is '|':
        return 0


convert_infix_to_postfix("0.(1.1)*.0")
