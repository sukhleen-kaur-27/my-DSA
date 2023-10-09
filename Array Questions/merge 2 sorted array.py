def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    temp = []
    for i in range(len(a)):
        if a[i] not in temp:
            temp.append(a[i])
    for i in range(len(b)):
        if b[i] not in temp:
            temp.append(b[i])
    return sorted(temp)