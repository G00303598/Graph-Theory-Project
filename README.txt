# G00303598 - Graph Theory Project
--------------------------------

This program matches regular expressions through the use of a converter which parses an expression in infix notation to post-fix by using an algorithm known as the Shunting Yard Algorithm, which then constructs NFAs with the postfix expression through the use of an algorithm called Thompson's Construction.

## NFA Construction
--------------------------------

This program is intended to construct a series of small NFAs using Thompson's construction. It does so by having a data type for storing the NFAs, I have used a list acting as a stack. The program iterates through an inifx expression, checking each character. If the character is not an operator an NFA is created and is pushed to the NFA stack. If the character is an operator an NFA is created depending on what sort of character it is. The characters in this program are as follows:

'.' --> Concatenation. Pops two NFAs from stack, joins them, and pushes them back onto the NFA stack.
'|' --> Alternation. Pops two NFAs from stack, creates two paths pointing to the accept state, and pushes the NFA back onto the stack.
'*' --> Zero or More. Pops a single NFA from the stack. This operator allows either an empty string or many of the same character.
'?' --> Zero or One. Pops a single NFA from the stack. This operator allows either an empty string or one of the character(s) being read.
'+' --> One or More. Pops a single NFA from the stack. This operator allows one or many of the characters being read, requiring at least one to continue to an accept state.
At the end of this program it should return a single NFA which has been popped from the NFA stack.

## Parser: Infix to Postfix
--------------------------------

This part of the program converts an infix expression to post-fix expression using an algorithm called Thompson's Construction. The algorithm iterates through the in-fix input, checking if the character being read is either an operator, an operand or brackets, and uses 3 data types (in this case I've used lists acting as stacks) to work through. If it's an operand, the character being read is pushed to the stack. If it's an operator you need to check it's precedence and push to the output stack accordingly. If it's a ( bracket being read, push it to the stack. If it's a ) bracket, you pop from the stack and push the characters to the output stack until a ( bracket has been met, at which point you pop the ( from the stack. When all characters have been read clear the stack by popping all remaining on it and pushing them to the output stack.

## Regex
--------------------------------
This program is a combination of the Parser program and the NFA construction program along with a matching function in order to make a working run-able Regex. It initially converts the infix to postfix and compiles the necessary NFAs from the postfix expression. It then Keeps track of the current set of states and the next set of states (Using sets as a way of storing this information). The program adds the initial state to the current state and then iterates through a string to compare with. The program uses a recursive helper function to keep track of the states being followed. On completion the program should display a true or false message along with the infix expression and the string it was compared to.
