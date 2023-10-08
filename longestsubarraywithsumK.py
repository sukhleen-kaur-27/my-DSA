def longestSubarrayWithSumK(arr: [int], k: int) -> int:
    # Write your code here
    maxval = 0
    for i in range(len(arr)):
        sum=0
        for j in range(i, len(arr)):
            sum += arr[j]
            if(sum==k):
                maxval = max(maxval, j-i+1)
    return maxval

def longestSubarrayWithSumK(arr: [int], k: int) -> int:
    left, right = 0, 0
    n = len(arr)
    sum = arr[0]
    max_val = 0
    while(right<n):
        if (sum>k and left<=right): 
            while(sum>k):
                sum -= arr[left]
                left+=1
        if (sum==k):
            max_val = max(max_val, (right-left+1))
        right+=1
        if(right<n):
            sum += arr[right]
    return max_val