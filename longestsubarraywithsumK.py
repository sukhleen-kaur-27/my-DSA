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