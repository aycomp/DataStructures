operatorList = ['-', '+', '/', '*']

def peek(stack):
    return stack[-1] if stack else None

def HasHigherPrecedence(stackTop, exp):
    if operatorList.index(stackTop) == 0 and operatorList.index(exp)== 1:
        return True
    if operatorList.index(stackTop) == 2 and operatorList.index(exp)== 3:
        return True
    elif operatorList.index(stackTop) >= operatorList.index(exp):
        return True
    else:
        return False

def IsOpeningParenthesis(stackTop):
    if(stackTop == '('):
        return True
    else:
        return False

def IsClosingParenthesis(stackTop):
    if(stackTop == ')'):
        return True
    else:
        return False

def InfixToPostfix(exp):
    tmpStack = []
    postfix = []
    for item in exp:
        # check if item is an operator, elif item is a parenthesis, else it is an operand
        if item in operatorList:
            while tmpStack and IsOpeningParenthesis(peek(tmpStack)) == False and IsClosingParenthesis(peek(tmpStack)) == False \
                    and HasHigherPrecedence(peek(tmpStack), item):
                postfix.append(tmpStack.pop())
            tmpStack.append(item)
        elif item == '(':
            tmpStack.append(item)
        elif item == ')':
            while tmpStack and IsOpeningParenthesis(peek(tmpStack)) == False:
                postfix.append(tmpStack.pop())
            tmpStack.pop()
        else:
            postfix.append(item)

    while tmpStack:
        postfix.append(tmpStack.pop())
    return postfix

def DoCalculation(operand, op1, op2):
    if(operand == '-'):
        return float(op1) - float(op2)
    elif(operand == '+'):
        return float(op1) + float(op2)
    elif(operand == '/'):
        return float(op1) / float(op2)
    elif(operand == '*'):
        return float(op1) * float(op2)

def EvaluatePostfix(exp):
    outputStack = []
    for item in exp:
        if item in operatorList:
            op2 = outputStack.pop()
            op1 = outputStack.pop()
            result = DoCalculation(item, op1, op2)
            outputStack.append(result)
        else:
            outputStack.append(item)
    return outputStack.pop()

if __name__ == '__main__':
    result = ''
    with open('bonus_input.txt') as f:
        content = f.readlines()
        for x in content:
            a = InfixToPostfix(str(x).split())
            # print(str(EvaluatePostfix(a)))
            result += str(EvaluatePostfix(a)) + '\n'

    print(result)
    with open('bonus_output.txt', 'w+') as outputFile:
        outputFile.write(result)