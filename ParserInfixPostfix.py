# This program converts an infix expression to postfix expression
# Operators: ., |, *
# Alphabet: a,b,c
# Include more operators + expand alphabet eventually
# Algorithm reference: https://brilliant.org/wiki/shunting-yard-algorithm/

stack = []  # Used to store operations: https://dbader.org/blog/stacks-in-python
output = []  # used to store output: https://dbader.org/blog/queues-in-python
token = []  # used to store tokens being read in: https://dbader.org/blog/stacks-in-python

SYMBOLS = ['*', '-', '+', '^']  # define operators to be included


def convert_infix_to_postfix(infix_expression):
    # while there are tokens to be read
    for element in infix_expression:
        print("Operator Stack: ", stack)
        # read a token
        token = element
        new_precedence = check_precedence(token)
        # print(token)  # used to verify successful iterations

        # if token is part of alphabet
        if token.isalpha() or token.isdigit():
            # add to queue
            output.append(token)

        # If token is an accepted operator:
        if token in SYMBOLS:
            # Loop through the stack
            for i in stack:
                token_to_check = i  # sets the token to check as the token at i on the stack
                previous_precedence = check_precedence(token_to_check)  # find the precedence of the token on the stack

                # if there's an operator on the stack with a greater precedence than what's being read in
                if previous_precedence >= new_precedence:
                    to_output = stack.pop()  # store pop from stack
                    # had to do it this way as brackets were falling through to here and
                    # being added to output queue
                    if to_output is '(':
                        continue
                    if to_output in SYMBOLS:
                        output.append(to_output)  # add to output stack
            # Add token to the stack
            stack.append(token)

        if token is '(':
            stack.append(token)

        if token is ')':
            for i in stack:
                token_to_check = i
                if token_to_check is '(':
                    stack.pop()

    # Put remainder of stack onto output
    # count number of elements left in list
    stack_count = len(stack)
    for i in range(stack_count):
        output.append(stack.pop())

    print(output)


def check_precedence(input_token):
    if input_token is '^':
        return 3
    if input_token is '*':
        return 2
    if input_token is '+' or input_token is '-':
        return 1


# TESTS FROM: http://www.oxfordmathcenter.com/drupal7/node/628
# convert_infix_to_postfix("A * B + C")  # Test 1 - Pass
# convert_infix_to_postfix("A + B * C ")  # Test 2 - Pass
# convert_infix_to_postfix("A * (B + C)")  # Test 3 - Pass
# convert_infix_to_postfix("A - B + C")  # Test 4 - Pass
# convert_infix_to_postfix("A * B ^ C + D ")  # Test 5 -- Fail, * after + for some reason
convert_infix_to_postfix("A * (B + C * D) + E")  # Test 6

