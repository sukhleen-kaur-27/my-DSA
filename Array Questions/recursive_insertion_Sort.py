from typing import List

def insertionSort(a: List[int], n: int, j: int) -> None:
   # write your code here
   # for i in range(n):
   #    for j in range(i,0,-1):
   #       if(a[j]<a[j-1]):
   #          (a[j], a[j-1]) = (a[j-1], a[j])
   #       else:
   #          break
   if n==i:
      return
   for i in range(j,0,-1):
      if (a[i]<a[i-1]):
         (a[i], a[i-1]) = (a[i-1], a[i])
      else:
         break
   insertionSort(a, n, i+1)