def moveZeros(n: int,  arr: [int]) -> [int]:
    # Write your code here.
    # temp = []
    # for i in range(len(arr)):
    #     if arr[i]!=0:
    #         temp.append(arr[i])
    # for i in range(len(temp)):
    #     arr[i] = temp[i]
    # for i in range(len(temp), len(arr)):
    #     arr[i] = 0
    # return arr

    index = 0
    for i in range(len(arr)):
        if (arr[i]!=0):
            arr[index] = arr[i]
            index+=1
    for i in range(index, len(arr)):
        arr[i] = 0
    return arr
