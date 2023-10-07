import math
def majorityElement(arr: [int]) -> int:
    # Write your code here
    # for i in range(len(arr)):
    #     count = 0
    #     for j in range(len(arr)):
    #         if(arr[i]==arr[j]):
    #             count+=1
    #     if(count>(len(arr)/2)):
    #         return arr[i]
    # return -1
    arr.sort(reverse = False)
    count = 1
    if (len(arr)==1):
        return arr[0]
    for i in range(len(arr)-1):
        if(arr[i]==arr[i+1]):
            count+=1
        else:
            count=1
        if(count>=math.ceil(len(arr)/2)):
            return arr[i]
    return -1