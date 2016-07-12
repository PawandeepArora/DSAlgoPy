from sample.package.DataStructures.Deque import Deque


def pallindrome(inputString):
    deque = Deque()

    for c in inputString:
        deque.addFront(c)


    continueFlag = True
    while deque.size()>1 and continueFlag:
        if deque.removeFront() == deque.removeRear():
            continueFlag = True
        else:
            continueFlag = False

    if continueFlag:
        print("Pallindrome")
    else:
        print("Not a pallindrome")


if __name__=="__main__":
    pallindrome("Pawandeep")
    pallindrome("arora")

