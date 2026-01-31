class Solution:
    def kthElement(self , arr, k):
        arr.sort()
        return arr[k - 1]
    

obj = Solution()
result = obj.kthElement([1, 6, 7, 4], 3)
print(result)