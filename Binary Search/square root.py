def floorSqrt(n):
   # write your code logic here .
   low = 0
   high = n
   ans = -1
   while(low<=high):
      mid = (low+high)//2
      val = mid*mid
      if(val<=n):
         low = mid+1
         ans = mid
      else:
         high = mid-1
   return ans
      
n= int(input())
print(floorSqrt(n))