import re

class MulResult:
    def __init__(self):
        self.isMul = False
        self.mulValue = []

    def getMulString(self):
        return "".join(map(str, self.mulValue))

def main(useSampleInput = False):

    data = ""
    if(useSampleInput):
        data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    else:
        path = "C:\\workspaces\\advent-of-code-2024\\day3input.txt"
        with open(path) as file:
            data =  file.read()

    muls = getMuls(data)
    print(muls)
    total = calculateMulValue(muls)
    print("Total from multiplication result: ", total)

    switchingMuls = getMulsWithSwitching(data)
    print(switchingMuls)
    switchingTotal = calculateMulValue(switchingMuls)
    print("Total from multiplation result with Switching: ", switchingTotal)
    


def getMuls(data):
    mulbuffer = []
    dataArr = list(data)
    for i in range(len(dataArr)):
        if dataArr[i] == 'm':
            # Using this like a C# out var
            # print("Found m at ", i)
            result = findMul(dataArr, i)
            if result.isMul:
                mulbuffer.append(result.getMulString())

    return mulbuffer


def getMulsWithSwitching(data):
    isMullingEnabled = True
    mulbuffer = []
    dataArr = list(data)
    for i in range(len(dataArr)):
        if dataArr[i] == 'd':
            isMullingEnabled = calculateMulState(dataArr, i, isMullingEnabled)

        if dataArr[i] == 'm':
            # Using this like a C# out var
            # print("Found m at ", i)
            result = findMul(dataArr, i)
            if result.isMul and isMullingEnabled:
                mulbuffer.append(result.getMulString())

    return mulbuffer


def calculateMulState(dataArr, dIndex, currentState):
    
    dataLength = len(dataArr)

    # If we haven't matched either do() or don't(), return the current mulState
    if dataArr[dIndex] != 'd':
        return currentState
    
    if dIndex + 1 > dataLength or dataArr[dIndex + 1] != 'o':
        return currentState
    
    isDo = False
    isDont = False

    if dIndex + 2 > dataLength:
        return currentState
    
    if dataArr[dIndex + 2] == '(':
        isDo = True
    elif dataArr[dIndex + 2] == 'n':
        isDont = True 

    if not isDo and not isDont:
        return currentState
    
    if isDo:
        if dIndex + 3 > dataLength or dataArr[dIndex + 3] != ')':
            return currentState
        
        # We have passed all conditions for do(), explicitly turn on mulling
        return True
    elif isDont:
        if dIndex + 3 > dataLength or dataArr[dIndex + 3] != '\'':
            return currentState
        if dIndex + 4 > dataLength or dataArr[dIndex + 4] != 't':
            return currentState
        if dIndex + 5 > dataLength or dataArr[dIndex + 5] != '(':
            return currentState
        if dIndex + 6 > dataLength or dataArr[dIndex + 6] != ')':
            return currentState
        
        # We have passed all condiitons for don't(), explicitly turn off mulling
        return False
        

  




def findMul(dataArr, mIndex):

    falseResult = MulResult()
    falseResult.isMul = False
    # Once we hit an M we start building:
    # first char: m
    # next char:  u
    # next char:  l
    # next char:  (
    stepper = 0
    dataLength = len(dataArr)

    if dataArr[mIndex] != 'm':
        return falseResult
    
    if mIndex + 1 > dataLength or dataArr[mIndex+1] != 'u':
        return falseResult
    
    if mIndex + 2 > dataLength or dataArr[mIndex+2] != 'l':
        return falseResult
    
    if mIndex + 3 > dataLength or dataArr[mIndex+3] != '(':
        return falseResult
    
    # next char must be 0-9
    if mIndex + 4 > dataLength or not dataArr[mIndex+4].isnumeric():
        return falseResult

    stepper = 5

    # next char must be 0-9 or ,
            # repeat until ,
    while(mIndex + stepper < dataLength):
        
        isDigitOrComma = dataArr[mIndex + stepper].isnumeric() or dataArr[mIndex + stepper] == ','
        
        if not isDigitOrComma:
            return falseResult  
        if dataArr[mIndex + stepper] == ',':
            break
        stepper += 1

    stepper += 1

    # Safety first!
    if (mIndex + stepper >= dataLength):
        return falseResult
    
    
    # next char must be 0-9 or )
    #   Repeat until ) hit
    while(mIndex + stepper < dataLength):
        isDigitOrCloseBracket = dataArr[mIndex + stepper].isnumeric() or dataArr[mIndex + stepper] == ')'
        
        if not isDigitOrCloseBracket:
            return falseResult  
        if dataArr[mIndex + stepper] == ')':
            break

        stepper += 1

    stepper += 1

    # Now that we have closed everything, let's build our string from start to finish
    result = MulResult()
    result.isMul = True
    result.mulValue = dataArr[mIndex:mIndex+stepper]
    return result

def calculateMulValue(mulValues):
    total = 0
    pattern = r"\((\d+),(\d+)\)"

    for mul in mulValues:
        match = re.search(pattern, mul)

        if match:
            total = total + (  int(match.group(1)) * int(match.group(2))     )
    
    return total


main(False)