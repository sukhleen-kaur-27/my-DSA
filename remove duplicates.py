def removeDuplicates(arr,n):
    # Write your code here.
    index = 0
    pos = 0
    for i in range(1,n):
        if(arr[pos]!=arr[i]):
            pos = i
            index+=1
            
    return index+1