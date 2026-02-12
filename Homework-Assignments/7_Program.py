# Given a sorted array of distinct integers and a target value, return the index if the
# target is found. If not, return the index where it would be if it were inserted in
# order.
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

class Solution:
    def findTarget(self, arr, target):
        mid_idx = int(len(arr)/2)
        print(mid_idx)
        i = 0
        if(target <= arr[mid_idx]):
            while i <= mid_idx:
                if(arr[i] == target):
                    return i
            i += 1
        elif (target >= arr[mid_idx]):
            print("inside second half")
            i = mid_idx
            while i <= len(arr):
                if(arr[i] == target):
                    return i
            i += 1

    
obj = Solution()
arr = [1,3,5,6]
target = 5
result = obj.findTarget(arr, target)
print(result)

#Not done.