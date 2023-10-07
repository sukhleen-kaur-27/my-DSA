def linearSearch(n: int, k: int, arr: [int]) -> int:
    # Write your code here.
    for i in range(n):
        if arr[i]==k:
            return i
    return -1
