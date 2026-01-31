class Solution:
    def rotatedArr(self , arr):
        last = arr.pop(len(arr) - 1)
        arr.insert(0, last)
        return arr

obj = Solution()
arr =  [1, 2, 3, 4, 5]
result = obj.rotatedArr(arr)
print(result)

#Done.