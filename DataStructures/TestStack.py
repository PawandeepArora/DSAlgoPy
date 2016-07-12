from sample.package.DataStructures.Stack import Stack


def testStack():

    s = Stack()
    print(s.isEmpty())

    s.push(1)
    s.push('Dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())

def reverseStringUsingStack(str):
    s = Stack()

    for c in str:
        s.push(c)

    revStr = ""
    while(s.isEmpty() == False):
        revStr = revStr + s.pop()

    print(revStr)

# To check the paranthesis
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1

    if balanced and s.isEmpty():
        print("parantheses stack is balanced")
    else:
        print("parantheses stack is not balanced")

# decimal to binary number using Stack
def divideBy2(decimalNum):
    remstack = Stack()

    while decimalNum > 0:
        rem = decimalNum % 2
        remstack.push(rem)
        decimalNum = decimalNum // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    print("The binary equivalent is: %s"% binString)


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
    print(newString)

if __name__=="__main__":
    #testStack()
    #reverseStringUsingStack("Pawandeep")
    #parChecker("((()))")
    #parChecker("((()")
    #divideBy2(233)
    baseConverter(2545,16)
