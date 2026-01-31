class Solution: 
    def largestElement(self, arr):
            i = 0
            Max = arr[i]
            while i < len(arr):
                if(arr[i] > Max):
                    Max = arr[i]
                i += 1

            return Max
    
obj = Solution()
arr = [1, 8, 7, 56, 90]
result = obj.largestElement(arr)
print(result)