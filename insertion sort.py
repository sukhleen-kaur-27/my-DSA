from typing import List

def insertionSort(a: List[int], n: int) -> None:
   # write your code here
   for i in range(n):
      for j in range(i,0,-1):
         if(a[j]<a[j-1]):
            (a[j], a[j-1]) = (a[j-1], a[j])
         else:
            break