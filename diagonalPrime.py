import math
import unittest
class Solution:
    def is_prime(self,elem):
        if elem == 1:
            return False
        if elem in [2,3,5]:
            return True
        else:
            end_val = math.sqrt(elem)
            i = 2
            while i <= end_val:
                if elem%i == 0:
                    return False
                i+=1
            return True
            
    def diagonalPrime(self, nums):
        row_size = len(nums)
        column_size = len(nums[0])

        #traverse left to right diagonal and store it in list
        left_right_array = []
        i = 0
        j = 0
        while i < row_size and j < column_size:
            left_right_array.append(nums[i][j])
            i+=1
            j+=1



        #traverse left to right diagonal and store it in list
        right_left_array = []
        i = 0
        j = column_size - 1
        while i < row_size and j >= 0:
            right_left_array.append(nums[i][j])
            i+=1
            j-=1

        #Remove duplicates if any
        diagonal_array = set(left_right_array + right_left_array)
        elem_not_found = True

        #sort the order in desc , and check if elem is prime if so return
        for elem in sorted(diagonal_array,reverse=True):
            if (self.is_prime(elem)):
                elem_not_found = False
                return elem

        if elem_not_found:
            return 0


class TestMyProgram(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()
    def test_add_numbers(self):
        # Test case 1
        result = self.obj.diagonalPrime([[1,2,3],[5,6,7],[9,10,11]])
        self.assertEqual(result, 11)


        # Test case 2
        result = self.obj.diagonalPrime([[1,2,3],[5,17,7],[9,11,10]])
        self.assertEqual(result, 17)

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()


