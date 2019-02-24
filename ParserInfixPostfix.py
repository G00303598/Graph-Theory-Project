#This program converts an infix expression to postfix expression
#Operators: ., |, *
#Include more operators eventually

def checkOperator(symbol):
    if symbol == '.' or symbol == '|' or symbol == '*':
        return 1
    else:
        return 0

def convertInfixToPostFix(infix_Expression):
    #Define the stack to pop and push from
    stack = []
    postFix_Expression = ''

    #Pushing ( to front of stack and appending ) to end to form regular expression
    stack.insert(0, '(')
    stack.append(')')

    #initialise before loop
    i = 0
    item = infix_Expression[i]

    #read in infix expression until empty
    for i in infix_Expression:
        print(item) #Testing purposes

        # if operand encountered, push to stack
        if item == checkOperator(item):
            postFix_Expression.join(item)
            print(postFix_Expression)

        # if left parenthesis encountered, push to stack
        elif item == '(':
            stack.insert(i, item)
            print(stack)

        elif item.isalpha() or item.isdigit():
            postFix_Expression.join(item)
            print(stack)






convertInfixToPostFix("a.(b.b)*.a")

