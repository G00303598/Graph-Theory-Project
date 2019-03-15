# This program is intended to construct a series of small NFAs
# using Thompson's construction
# Author: Morgan Reilly - G00303598

# References:
# https://swtch.com/~rsc/regexp/regexp1.html
# https://web.microsoftstream.com/video/5e2a482a-b1c9-48a3-b183-19eb8362abc9


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
        # TODO: Include other special characters.. ie. ?, +
        # Concatenation
        if token is '.':
            # popping in LIFO order
            nfa_1, nfa_0 = nfa_stack.pop(), nfa_stack.pop()

            # merge NFAs together
            nfa_0.accept_state.edge1 = nfa_1.initial_state

            # push nfa back onto stack
            new_nfa = Nfa(nfa_0.initial_state, nfa_1.accept_state)
            nfa_stack.append(new_nfa)

        # Alteration
        elif token is '|':
            # Pop 2 nfa from stack in LIFO order
            nfa_1, nfa_0 = nfa_stack.pop(), nfa_stack.pop()

            # create new initial state.
            # connect to initial state from 2 NFAs popped from stack
            initial_state, accept_state = State(), State()
            initial_state.edge1, initial_state.edge2 = nfa_0.initial_state, nfa_1.initial_state

            # creating accept state connecting accept states from popped NFAs
            nfa_0.accept_state.edge1, nfa_1.accept_state.edge1 = accept_state, accept_state

            # Push NFA to stack
            new_nfa = Nfa(initial_state, accept_state)
            nfa_stack.append(new_nfa)

        # Zero or more
        elif token is '*':
            # pop NFA from stack
            nfa_0 = nfa_stack.pop()

            # create initial + accept state
            initial_state, accept_state = State(), State()

            # join new initial to old NFA0 initial state and new accept state
            initial_state.edge1, initial_state.edge2 = nfa_0.initial_state, accept_state

            # join old accept to new accept and NFA0 initial state
            nfa_0.accept_state.edge1, nfa_0.accept_state.edge2 = nfa_0.initial_state, accept_state

            # push new NFA to stack
            new_nfa = Nfa(initial_state, accept_state)
            nfa_stack.append(new_nfa)

        # Zero or one
        elif token is '?':
            # TODO: NO IDEA IF THIS WORKS
            # pop NFA from stack
            nfa_0 = nfa_stack.pop()

            # create initial state + accept state
            initial_state, accept_state = State(), State()

            # join old accept state to new accept state and NFA0 initial state
            nfa_0.accept_state.edge1, nfa_0.accept_state.edge2 = nfa_0.initial_state, accept_state

            # push new NFA to stack
            new_nfa = Nfa(initial_state, accept_state)
            nfa_stack.append(new_nfa)

        # One or more
        elif token is '+':
            # TODO: NO IDEA IF THIS WORKS
            # popping in LIFO order
            nfa_0 = nfa_stack.pop()

            # create initial state + accept state
            initial_state, accept_state = State(), State()

            # join accept to NFA0 initial state
            accept_state = nfa_0.accept_state.edge1

            # join initial state of NFA to accept state
            initial_state.edge1 = accept_state

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


# print(regex_compiler("010100*0*1**|*"))
print(regex_compiler("ab+"))
