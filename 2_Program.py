class Solution:
    def getMinMax(self, arr):
        i = 0
        Max = arr[0]
        Min = arr[0]
        while i < len(arr):
            if(arr[i] > Max):
                Max = arr[i]
                if (arr[i] < Min):
                    Min = arr[i]
            i += 1        
        return [Min, Max]
    
obj = Solution()
arr = [1 , 3, 6, 4, 8, 7, 5]
result = obj.getMinMax(arr)
print(result); 