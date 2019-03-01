# This program converts an infix expression to postfix expression
# Operators: ., |, *
# Alphabet: a,b,c
# Include more operators + expand alphabet eventually
# Algorithm reference: https://brilliant.org/wiki/shunting-yard-algorithm/

stack = []  # Used to store operations: https://dbader.org/blog/stacks-in-python
output = []  # used to store output: https://dbader.org/blog/queues-in-python
token = []  # used to store tokens being read in: https://dbader.org/blog/stacks-in-python

SYMBOLS = ['*', '-', '+']  # define operators to be included


def convert_infix_to_postfix(infix_expression):
    # while there are tokens to be read
    for element in infix_expression:
        # read a token
        token = element
        new_precedence = check_precedence(token)
        # print(token)  # used to verify successful iterations

        # if token is part of alphabet
        if token.isalpha() or token.isdigit():
            # add to queue
            output.append(token)
            # print(output)

        # I ignore the brackets --> ( )   as I thought it was a redundant step
        # If token is an accepted operator:
        if token in SYMBOLS:
            # Loop through the stack
            for i in stack:
                token_to_check = i  # sets the token to check as the token at i on the stack
                previous_precedence = check_precedence(token_to_check)  # find the precedence of the token on the stack

                # if there's an operator on the stack with a greater precedence than what's being read in
                if previous_precedence > new_precedence:
                    output.append(stack.pop())

            # Add token to the stack
            stack.append(token)

    # Put remainder of stack onto output
    # count number of elements left in list
    stack_count = len(stack)
    for i in range(stack_count):
        output.append(stack.pop())

    return output


def check_precedence(input_token):
    if input_token is '*':
        return 2
    if input_token is '+':
        return 1
    if input_token is '-':
        return 0


# convert_infix_to_postfix("0.(1.1)*.0")
convert_infix_to_postfix("(a+b) - c * 5")
# convert_infix_to_postfix(".|.*")  # using to test order of precedence
print(output)
