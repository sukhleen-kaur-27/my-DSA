def threeSum(self, arr: List[int]) -> List[List[int]]:
        n=len(arr)
        temp = []
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if (arr[i]+arr[j]+arr[k]==0) and i!=j and j!=k and k!=i:
                        new_val = [arr[i], arr[j], arr[k]]
                        new_val.sort()
                        if new_val not in temp:
                            temp.append(new_val)
        return temp