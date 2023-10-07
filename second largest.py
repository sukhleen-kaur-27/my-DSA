def getSecondOrderElements(n: int,  arr: [int]) -> [int]:
    # Write your code here.
    secondMax = 10^9
    firstMax = 10^9
    secondMin = 10^9
    firstMin = 10^9
    for i in range(0, len(arr)):
        if(secondMax<arr[i]):
            if(firstMax<arr[i]):
                secondMax = firstMax
                firstMax = arr[i]
            else:
                secondMax = arr[i]
        if (firstMin>arr[i]): 
            secondMin = firstMin
            firstMin = arr[i]
        elif (secondMin>arr[i]):
            secondMin = arr[i]
    return [secondMax, secondMin]
