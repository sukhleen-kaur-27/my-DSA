def read(n: int, book: [int], target: int) -> str:
    # Write your code here.
    book = sorted(book)
    left = 0
    right = n-1
    sum = 0
    while(left<=right):
        sum = book[left]+book[right]
        if sum == target:
            return "YES"
        elif sum>target:
            sum = 0
            right-=1
        else :
            sum = 0
            left +=1
    return "NO"