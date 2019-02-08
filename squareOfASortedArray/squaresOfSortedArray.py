# https://leetcode.com/problems/squares-of-a-sorted-array/
# 132 / 132 test cases passed.
# Status: Accepted
# Runtime: 144 ms, faster than 91.17% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 12.2 MB, less than 100.00% of Python3 online submissions for Squares of a Sorted Array.

# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

## Note:
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.

# A = [-4,-1,0,3,10]
A = [-7,-3,2,3,11]
arr = []
for a in A:
    arr.append(a*a)
print arr
