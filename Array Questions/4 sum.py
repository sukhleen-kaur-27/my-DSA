def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        n=len(arr)
        temp = []
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for r in range(k+1,n):
                        if (arr[i]+arr[j]+arr[k]+arr[r]==target):
                            new_val = [arr[i], arr[j], arr[k], arr[r]]
                            new_val.sort()
                            if new_val not in temp:
                                temp.append(new_val)
        return temp