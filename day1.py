# https://adventofcode.com/2024/day/1


def main(useSampleInput = False):

    leftList = []
    rightList = []
    if(useSampleInput):
        # Sample input
        leftList = [3,4,2,1,3,3]
        rightList = [4,3,5,3,9,3]
    else:
        path = "C:\\workspaces\\advent-of-code-2024\\day1input.txt"
        with open(path) as file:
            lines = file.readlines()
            print(len(lines))
            for line in lines:
                splitLine = line.split("   ")
                leftList.append(int(splitLine[0]))
                rightList.append(int(splitLine[1]))

    

    if len(leftList) != len(rightList):
        print("Error: Array lengths must match")
        return 1
    
    if len(leftList) == 0 or len(rightList) == 0:
        print("Error: Arrays must contain values")
        return 1
    
    totalDistance = calculateDistance(leftList, rightList)
    
    print("Total Distance: ", totalDistance)
    print("---")
    similarityScore = calculateSimilarityScore(leftList, rightList)
    print("Similarity Score: ", similarityScore)



def calculateDistance(left, right):
    # Copy the lists and sort them, since pass by ref is a thing here
    l = left[:]
    r = right[:]

    l.sort()
    r.sort()

    totalDistance = 0

    for i in range(len(l)):
        totalDistance += abs(l[i] - r[i])

    return totalDistance

def calculateSimilarityScore(left, right):
    rightMap = dict()

    # for every element, record the number of occurrences in a dict
    for elem in right:
        if elem in rightMap:
            rightMap[elem] += 1
        else:
            rightMap[elem] = 1

    print(rightMap)
    
    similarityScore = 0
    #scoreSteps = []
    for item in left:
        if item not in rightMap:
            #scoreSteps.append(item * 0)
            similarityScore += item * 0
        elif item in rightMap:
            #scoreSteps.append(item * rightMap[item])
            similarityScore += item * rightMap[item]
        
    return similarityScore

main(False)





