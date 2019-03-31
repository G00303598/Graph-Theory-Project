# This program matches regular expressions through the use of
# a converter which parses an expression in infix notation to postfix by using
# an algorithm known as the Shunting Yard Algorithm,
# which then constructs NFAs with the postfix expression through the use
# of an algorithm called Thompson's Construction

# Author: Morgan Reilly

# References for Shunting Yard algorithm:
# https://brilliant.org/wiki/shunting-yard-algorithm/
# https://web.microsoftstream.com/video/a29536d4-e975-4172-a470-40b4fe28866e
# https://www.boost.org/doc/libs/1_56_0/libs/regex/doc/html/boost_regex/syntax/basic_extended.html#boost_regex.syntax.basic_extended.operator_precedence
# https://regex101.com/

# References for NFA construction:
# https://swtch.com/~rsc/regexp/regexp1.html
# https://web.microsoftstream.com/video/5e2a482a-b1c9-48a3-b183-19eb8362abc9

# References for string matching:
# https://web.microsoftstream.com/video/6b4ba6a4-01b7-4bde-8f85-b4b96abc902a
# https://web.microsoftstream.com/video/1b3e7f4f-69e0-4316-853f-c63b14f9c36a


# function to convert infix to postfix
def convert_infix_to_postfix(infix_expression):
    stack = []  # Shunting store: https://dbader.org/blog/stacks-in-python
    output = []  # used to store output: https://dbader.org/blog/queues-in-python

    # define operators to be included in dictionary
    symbols = {'^': 40, '?': 30, '*': 30, '+': 20, '-': 20, '.': 20, '|': 10}

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
            while stack and symbols[token] <= symbols.get(stack[-1], 0):
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
    print("POSTFIX: ", ''.join(output))  # prints as string
    postfix_expression = ''.join(output)
    return postfix_expression  # returns as string


class State:
    # variables
    label = None
    edge1 = None
    edge2 = None


class Nfa:
    # variables
    initial_state = None
    accept_state = None

    # constructor
    def __init__(self, initial_state, accept_state):
        # self. is equivalent to this.
        self.initial_state = initial_state
        self.accept_state = accept_state


# function to take postfix expression and add to nfa stack
def regex_compiler(postfix_expression):
    nfa_stack = []

    for i, token in enumerate(postfix_expression):
        if token is '.':
            """CONCATENATION"""
            # popping in LIFO order
            nfa_1, nfa_0 = nfa_stack.pop(), nfa_stack.pop()

            # merge NFAs together
            nfa_0.accept_state.edge1 = nfa_1.initial_state

            # push nfa back onto stack
            new_nfa = Nfa(nfa_0.initial_state, nfa_1.accept_state)
            nfa_stack.append(new_nfa)

        elif token is '|':
            """ALTERNATION"""
            # Pop 2 nfa from stack in LIFO order
            nfa_1, nfa_0 = nfa_stack.pop(), nfa_stack.pop()

            # create new initial state and accept state
            initial_state, accept_state = State(), State()

            # connect to initial state from 2 NFAs popped from stack
            initial_state.edge1, initial_state.edge2 = nfa_0.initial_state, nfa_1.initial_state

            # join nfa0 accept state to accept state and join nfa1 accept state to accept state
            nfa_0.accept_state.edge1, nfa_1.accept_state.edge1 = accept_state, accept_state

            # Push NFA to stack
            new_nfa = Nfa(initial_state, accept_state)
            nfa_stack.append(new_nfa)

        elif token is '*':
            """ZERO OR MORE"""
            # pop NFA from stack
            nfa_0 = nfa_stack.pop()

            # create initial + accept state
            initial_state, accept_state = State(), State()

            # join initial state to nfa and join initial state to accept state
            initial_state.edge1, initial_state.edge2 = nfa_0.initial_state, accept_state

            # join nfa accept state to nfa initial state and join nfa accept state to accept state
            nfa_0.accept_state.edge1, nfa_0.accept_state.edge2 = nfa_0.initial_state, accept_state

            # push new NFA to stack
            new_nfa = Nfa(initial_state, accept_state)
            nfa_stack.append(new_nfa)

        elif token is '?':
            """ZERO OR ONE"""
            # pop NFA from stack
            nfa_0 = nfa_stack.pop()

            # create initial + accept state
            initial_state, accept_state = State(), State()

            # join new initial state to nfa initial state and join initial state to accept state
            initial_state.edge1, initial_state.edge2 = nfa_0.initial_state, accept_state

            # join nfa accept state to accept state
            nfa_0.accept_state.edge1 = accept_state

            # push new NFA to stack
            new_nfa = Nfa(initial_state, accept_state)
            nfa_stack.append(new_nfa)

        elif token is '+':
            """ONE OR MORE"""
            # pop NFA from stack
            nfa_0 = nfa_stack.pop()

            # create initial + accept state
            initial_state, accept_state = State(), State()

            # join initial state to nfa initial state
            initial_state.edge1 = nfa_0.initial_state

            # join nfa accept state to initial state and join nfa accept state to accept state
            nfa_0.accept_state.edge1, nfa_0.accept_state.edge2 = nfa_0.initial_state, accept_state

            # push new NFA to stack
            new_nfa = Nfa(initial_state, accept_state)
            nfa_stack.append(new_nfa)

        # if not regular character
        else:
            # creating new instance of State
            accept_state, initial_state = State(), State()

            # join initial state to accept state using arrow labeled token
            # initial state is character being read, edge one points to accept state
            initial_state.label, initial_state.edge1 = token, accept_state

            # push to stack - using constructor w/ 2 args
            new_nfa = Nfa(initial_state, accept_state)
            nfa_stack.append(new_nfa)

    # stack should only have single NFA on stack
    final_nfa = nfa_stack.pop()
    return final_nfa


def match_infix_to_string(infix_expression, string_in):
    """ Function to match an infix expression to a string """
    # shunt and compile regular expression
    postfix_expression = convert_infix_to_postfix(infix_expression)
    nfa = regex_compiler(postfix_expression)

    # current set of states and next set of states
    current_state, next_state = set(), set()

    # Add initial state to current set
    current_state |= follow_edge_state(nfa.initial_state)

    # loop through each token in string, where i is counter, token is character being read
    for i, token in enumerate(string_in):
        # loop through current set of states, where j is counter, char is character being read
        for j, char in enumerate(current_state):
            # check if state is labelled s
            if char.label is token:
                # add edge1 to next set
                next_state |= follow_edge_state(char.edge1)
        # set current state to next
        current_state = next_state
        next_state = set()

    # check if accept state is in set of current sates
    return nfa.accept_state in current_state


def follow_edge_state(state_to_follow):
    """ Helper function: returns the set of states reached from state following edge arrows"""

    # create a new set with state as its only member
    states = set()
    states.add(state_to_follow)

    # check if state has arrows labelled e from it
    if state_to_follow.label is None:
        # check if edge 1 is a state
        if state_to_follow.edge1 is not None:
            # if there's an edge1, follow
            # using function recursively and shorthand or equals operator --> |=
            states |= follow_edge_state(state_to_follow.edge1)
        # check if edge 2 is a state
        if state_to_follow.edge2 is not None:
            # if there's an edge2, follow
            states |= follow_edge_state(state_to_follow.edge2)
    return states


# Tests 1 - From video: https://web.microsoftstream.com/video/6b4ba6a4-01b7-4bde-8f85-b4b96abc902a
infix_list = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
string_list = ["", "ab", "abc", "abbc", "abcc", "abad", "abbbc"]

# Tests 2 - Testing operators: + ? -- Verifying correct functionality with basic tests
# infix_list = ["(a.b)+", "(a.b)?"]
# string_list = ["", "a", "ab", "aaa", "abab", "ababab"]

# Test set 3 -- Recursion issue -- FIX HELPER!
# infix_list = ["(0|(1(01*(00)*0)*1)*)*"]
# string_list = ["", "0", "00", "11", "000", "011", "110", "0000", "0011", "0110", "1001", "1100", "1111", "00000"]

# User input
infix_expression_input = input("Enter infix expression\n >")
string_input = input("Enter string to compare\n >")

# Runner -- for use with lists
# for i, infix in enumerate(infix_list):
#    for j, string in enumerate(string_list):
#        print("INPUT: ", string_input, "\nRESULT: ", match_infix_to_string(infix_expression_input, string_input))


# Runner -- For use with user input
print("INPUT: ", string_input, "\nRESULT: ", match_infix_to_string(infix_expression_input, string_input))
