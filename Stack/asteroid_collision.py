class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            while stack and stack[-1]>0 and asteroids[i]<0:
                if (stack[-1]+asteroids[i])<0:
                    stack.pop()
                elif (stack[-1]+asteroids[i])==0:
                    stack.pop()
                    asteroids[i]=0
                else: 
                    asteroids[i]=0
            if asteroids[i]!=0 :
                stack.append(asteroids[i])
        return stack