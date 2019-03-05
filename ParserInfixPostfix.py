# This program converts an infix expression to postfix expression
# Author: Morgan Reilly - G00303598

# Algorithm references:
# https://brilliant.org/wiki/shunting-yard-algorithm/
# https://web.microsoftstream.com/video/a29536d4-e975-4172-a470-40b4fe28866e

stack = []  # Shunting store: https://dbader.org/blog/stacks-in-python
output = []  # used to store output: https://dbader.org/blog/queues-in-python
SYMBOLS = ['*', '-', '+', '^', '|', '.']  # define operators to be included


def convert_infix_to_postfix(infix_expression):
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

                # while stack has a operator of greater precedence than input
                while stack and token_precedence <= stack_precedence:
                    to_output = stack.pop()  # stores token to send to output
                    output.append(to_output)

                # push lesser operator to stack
                stack.append(token)

        # if right bracket encountered
        if token == ')':
            while stack[-1] != '(':
                to_output = stack.pop()
                output.append(to_output)
            stack.pop()  # ( found, pop from stack

    # clear remainder on stack
    while stack:
        to_output = stack.pop()
        output.append(to_output)

    # print(output)  # prints as list
    print("POSTFIX: ", ''.join(output))  # prints as string
# END


def check_precedence(input_token):
    if input_token is '^':
        return 3
    if input_token is '*':
        return 2
    if input_token is '+' or input_token is '-':
        return 1
    if input_token is ')' or input_token is '(':
        return -1


# Tests from: http://www.oxfordmathcenter.com/drupal7/node/628
# convert_infix_to_postfix("A*B+C")  # Test 1
# convert_infix_to_postfix("A+B*C")  # Test 2
# convert_infix_to_postfix("A*(B+C)")  # Test 3
# convert_infix_to_postfix("A-B+C")  # Test 4
# convert_infix_to_postfix("A*B^C+D")  # Test 5
convert_infix_to_postfix("A*(B+C*D)+E")  # Test 6
