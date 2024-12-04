# #
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9


class ReportResult:

    def __init__(self):
        self.failedIndexes = []
    
    def passed(self):
        return len(self.failedIndexes) == 0
    
    def addIndex(self, i):
        if i not in self.failedIndexes:
            self.failedIndexes.append(i)



def main(useSampleInput = False):

    reports = []
    if(useSampleInput):
        # Sample input
        reports.append([7,6,4,2,1])
        reports.append([1,2,7,8,9])
        reports.append([9,7,6,2,1])
        reports.append([1,3,2,4,5])
        reports.append([8,6,4,4,1])
        reports.append([1,3,6,7,9])
    else:
        path = "C:\\workspaces\\advent-of-code-2024\\day2input.txt"
        with open(path) as file:
            lines = file.readlines()
            print(len(lines))
            for line in lines:
                splitLine = line.split(" ")
                lineArr = []
                for i in splitLine:
                    lineArr.append(int(i))
                reports.append(lineArr)

    
    # safeCount = 0
    
    # for report in reports:
    #     result = getSafetyReport(report)
    #     if result.passed():
    #         safeCount += 1
    
    safeCountExtended = 0
    for report in reports:
        if isSafeExtended(report):
            safeCountExtended += 1

    # print("Safe Reports: ", safeCount)
    print("Safe Reports with Drops:", safeCountExtended)



def getSafetyReport(report):
    # Safety Criteria:
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.

    # 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    # 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    # 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    # 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    # 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    # 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

    smokeTestResultFailure = ReportResult()
    smokeTestResultFailure.addIndex(0)
    smokeTestResultFailure.addIndex(1)
    print("Eval: ", report)
    
    if len(report) == 0 or len(report) == 1:
        print("Unsafe list length")
        return smokeTestResultFailure
    
    if report[0] == report[1]:
        print("Unsafe delta at start")
        return smokeTestResultFailure
    
    isAscending = isListAscending(report)

    result = ReportResult()
    for i in range(len(report)):
        if i == len(report)-1:
            break
        
        delta = 0
        # Check sequencing for ascention vs descention and set delta
        if isAscending:
            if not report[i] < report[i+1]:
                result.addIndex(i+1)
                print("Expected Ascent, detected Descent", report[i]," ", report[i+1])
                continue
            
            delta = report[i] - report[i+1]
            if delta == 0 or delta < -3:
                print("Bad Delta on Ascent ", report[i], " ", report[i+1])
                result.addIndex(i+1)

        else:
            if not report[i] > report[i+1]:
                result.addIndex(i+1)
                print("Expected Descent, detected Ascent ", report[i]," ", report[i+1])
                continue

            delta = report[i] - report[i+1]
            if delta == 0 or delta > 3:
                print("Bad Delta on Descent ", report[i], " ", report[i+1])
                result.addIndex(i+1)


    

    print("Passed? ", result.passed())
    print(result.failedIndexes)
    print(len(result.failedIndexes))
    print("---")
    return result


def isSafeExtended(report):
    initialResult = getSafetyReport(report)
    if initialResult.passed():
        return True


    if len(initialResult.failedIndexes) > 0:
        # Just brute force removing each item until something works
        for i in range(len(report)):
            reportCopy = report[:]
            print("try again")
            del reportCopy[i]

            updatedResult = getSafetyReport(reportCopy)
            if updatedResult.passed():
                return True

    return False


def isListAscending(report):
    ascentionMap = { "a":0, "d":0 }
    for i in range(len(report)):
        if i == len(report)-1:
            break
        
        if report[i] > report[i+1]:
            ascentionMap["d"] += 1
        elif report[i] < report[i+1]:
            ascentionMap["a"] += 1

    # Count the occurrences of ascention vs descention to see if list is ascending or descending
    return ascentionMap["a"] >= ascentionMap["d"]
    
    
main(False)