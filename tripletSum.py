class Solution:
    def threeSum(self, nums):

        nums = sorted(nums)
        triplet_list = []
        for currentPos in range(0, len(nums) - 1):
            leftIndex = currentPos + 1
            rightIndex = len(nums) - 1

            sum_list = []
            while leftIndex < rightIndex:

                if nums[currentPos] + nums[rightIndex] + nums[leftIndex] == 0:
                    sum_list.extend([nums[leftIndex], nums[rightIndex], nums[currentPos]])
                    leftIndex += 1
                    rightIndex -= 1
                    if sum_list not in triplet_list:
                        triplet_list.append(sum_list)
                    sum_list = []

                #  leftIndex to be incremented since its sorted
                elif nums[currentPos] + nums[rightIndex] + nums[leftIndex] < 0:
                    leftIndex += 1
                # righIndex to be decremented
                else:
                    rightIndex -= 1
        return triplet_list

