# Solved by Prateek Rokadiya - 06-02-2019
# Success
# Details
# 29 / 29 test cases passed.
# Status: Accepted
# Runtime: 892 ms, faster than 30.81% of Python3 online submissions for Two Sum.
# Memory Usage: 7.2 MB, less than 81.55% of Python3 online submissions for Two Sum.

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#         31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
#         59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
#         87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
nums1 = [2, 7, 11, 15]
target1 = 9
#
# nums = [3, 2, 4, 15]
# target = 6

    # Input
    # [3,3]
    # 6
    # Output
    # []
    # Expected
    # [0,1]
    #
    #
nums2 = [3, 3]
target2 = 6

    #
    # Input
    # [3,2,4]
    # 6
    # Output
    # [0]
    # Expected
    # [1,2]
    #
nums3 = [3, 2, 4]
target3 = 6

    # Input
    # [217,231,523,52,547,243,648,509,415,149,689,710,265,187,370,56,977,182,400,329,471,805,955,989,255,766,38,566,79,843,295,229,988,108,781,619,704,542,335,307,359,907,727,959,161,699,123,650,147,459,657,188,304,268,405,685,620,721,351,570,899,60,388,771,24,659,425,440,508,373,32,645,409,272,356,175,533,740,370,152,34,510,745,251,227,494,258,527,817,773,178,194,860,387,627,851,449,736,15,212,529,950,316,28,65,484,968,63,4,643,795,669,203,677,139,636,289,555,430,849,150,493,301,377,240,873,965,441,230,349,447,470]
    # 718
    # Output
    # [27,40,79]
    # Expected
    # [27,79]

nums4 = [217,231,523,52,547,243,648,509,415,149,689,710,265,187,370,56,977,182,400,329,471,805,955,989,255,766,38,566,79,843,295,229,988,108,781,619,704,542,335,307,359,907,727,959,161,699,123,650,147,459,657,188,304,268,405,685,620,721,351,570,899,60,388,771,24,659,425,440,508,373,32,645,409,272,356,175,533,740,370,152,34,510,745,251,227,494,258,527,817,773,178,194,860,387,627,851,449,736,15,212,529,950,316,28,65,484,968,63,4,643,795,669,203,677,139,636,289,555,430,849,150,493,301,377,240,873,965,441,230,349,447,470]
target4 = 718

    # Input
    # [2222222,2222222]
    # 4444444
    # Output
    # [0,0]
    # Expected
    # [0,1]

nums5 = [2222222,2222222]
target5 = 4444444

arr = []
# print(nums[27])
# print(nums[40])
# print(nums[79])
numz = [nums1, nums2, nums3, nums4, nums5]
targetz = [target1, target2, target3, target4, target5]

for nums, target in zip(numz, targetz):
    arr = []
    for i in range(0, len(nums)):
        if ((target - nums[i]) in nums):
            # print((target - nums[i]), (target - nums[i]) in nums, nums.index(target - nums[i]), (target - nums[i]) == nums[i], nums[i])
            # if ((target - nums[i]) is nums[i]):
            if ((target - nums[i]) == nums[i]):
                a = [j for j, val in enumerate(nums) if (val == target - nums[i])]
                if len(a) > 1:
                    arr = a
                    # print ("a: ", a)
                    print ("aarr: ", arr)
                    break
                else:
                    continue
                # print(i)
            arr.append(i)
            arr.append(nums.index(target - nums[i]))
            # print i
            break

    print(nums, target)
    print ("output: ", arr)
    print ("-----------------------------------------------------------")
# arr = []
# for i in range(0, len(nums)):
#     if ((target - nums[i]) in nums) and (((target - nums[i]) is nums[i]) and ((target - nums[i]) in nums[i+1:]) or ((target - nums[i]) in nums[:i-2])):
#         arr.append(i)
#         print i
#
# print arr

