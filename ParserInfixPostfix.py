# This program converts an infix expression to postfix expression
# Author: Morgan Reilly - G00303598

# Algorithm references:
# https://brilliant.org/wiki/shunting-yard-algorithm/
# https://web.microsoftstream.com/video/a29536d4-e975-4172-a470-40b4fe28866e

stack = []  # Shunting store: https://dbader.org/blog/stacks-in-python
output = []  # used to store output: https://dbader.org/blog/queues-in-python
SYMBOLS = ['*', '-', '+', '^', '|', '.']  # define operators to be included


def v3_convert_infix_to_postfix(infix_expression):
    print("INFIX: ", infix_expression)
    # loop through input
    for i, token in enumerate(infix_expression):
        print(i, " >   Input: ", token, "   Stack: ", stack,"   Output: ", output)

        if token is '(':
            stack.append(token)

        if token.isalpha() or token.isdigit():
            output.append(token)

        if token in SYMBOLS:
            if len(stack) is 0:
                # means nothing on stack
                stack.append(token)
            else:
                # compare both tokens to determine precedence
                token_precedence = check_precedence(token)  # gets precedence value of input
                stack_precedence = check_precedence(stack[-1])  # gets precedence value of top of stack

                if token_precedence >= stack_precedence:
                    if token is '(':
                        stack.pop()
                    else:
                        stack.append(token)

                elif token_precedence <= stack_precedence:
                    if token is '(':
                        stack.pop()
                    else:
                        to_output = stack.pop()  # stores token to send to output
                        output.append(to_output)
                        stack.append(token)

        # if right bracket encountered
        if token is ')':
            # pop all from stack to output
            for i, el in enumerate(stack):
                to_output = stack.pop()
                output.append(to_output)
                if el is '(':
                    stack.pop()
    print(stack)
    # clear remainder on stack
    while stack:
        to_output = stack.pop()
        output.append(to_output)

    print(output)
    # print("POSTFIX: ", ''.join(output))  # prints as string
# END V3


def v2_convert_infix_to_postfix(infix_expression):
    # loop through input
    for token in infix_expression:
        stack_count = len(stack)

        # print("INPUT: ", token)
        # print("STACK: ", stack)
        # print("OUTPUT: ", output)
        # print("STACK_COUNT: ", stack_count)

        if token.isalpha() or token.isdigit():
            output.append(token)

        if token is '(':
            stack.append(token)

        if token in SYMBOLS:
            stack.append(token)
            if stack_count > 0:
                input_precedence = check_precedence(token)
                stack_item = stack
                stack_precedence = check_precedence(stack_item)

                if stack_item in SYMBOLS:
                    if input_precedence <= stack_precedence:
                        output.append(stack_item)

                    if input_precedence >= stack_precedence:
                        stack.append(token)

        if token is ')':
            # While stack is not (
            for i in stack:
                if i is '(':
                    stack.pop()
                else:
                    output.append(stack.pop())

    stack_count = len(stack)
    # Clear stack + append to output
    for i in range(stack_count):
        stack_item = stack.pop()
        if i is '(':
            # ( encountered
            continue
        else:
            output.append(stack_item)

    print(stack)
    print(output)


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
                stack_item = stack.pop()
                if i is '(':
                    continue
                else:
                    output.append(stack_item)

    # Put remainder of stack onto output
    # count number of elements left in list
    stack_count = len(stack)
    for i in range(stack_count):
        output.append(stack.pop())

    print(stack)
    print(output)


def check_precedence(input_token):
    if input_token is '^':
        return 3
    if input_token is '*':
        return 2
    if input_token is '+' or input_token is '-':
        return 1
    if input_token is ')' or input_token is '(':
        return -1


# TESTS FROM: http://www.oxfordmathcenter.com/drupal7/node/628
# convert_infix_to_postfix("A * B + C")  # Test 1 - Pass
# convert_infix_to_postfix("A + B * C ")  # Test 2 - Pass
# convert_infix_to_postfix("A * (B + C)")  # Test 3 - Pass
# convert_infix_to_postfix("A - B + C")  # Test 4 - Pass
# convert_infix_to_postfix("A * B ^ C + D ")  # Test 5 - Fail
# convert_infix_to_postfix("A * (B + C * D) + E")  # Test 6 - Fail

# VERSION 2 TESTS -- Version was set up for V3, but mostly a fail.
# v2_convert_infix_to_postfix("A * B + C")  # Test 1
# v2_convert_infix_to_postfix("A + B * C ")  # Test 2
# v2_convert_infix_to_postfix("A * (B + C)")  # Test 3
# v2_convert_infix_to_postfix("A * (B + C * D) + E")

# Version 3 Tests -- Working/Submittable version
#v3_convert_infix_to_postfix("A * B + C")  # Test 1 - Pass
#v3_convert_infix_to_postfix("A + B * C ")  # Test 2 - Pass
# v3_convert_infix_to_postfix("A*(B+C)")  # Test 3 - Pass
#v3_convert_infix_to_postfix("A - B + C")  # Test 4 - Pass
v3_convert_infix_to_postfix("A * B ^ C + D ")  # Test 5 - Fail
#v3_convert_infix_to_postfix("A * (B + C * D) + E")  # Test 6 - Fail
