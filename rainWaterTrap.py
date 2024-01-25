from collections import deque
import unittest
def trap_rain_water(arr):
    '''
    :param arr: input Array Bar heights
    :return: max storage of water value
    '''
    
    max_storage = 0
    user_stack = deque()
    for pos,val in enumerate(arr):
        #if stack is not empty check if the current value to push is greater than top value in stack
        #in this case we need to pop till the end of the elements in stack and calculate area
        while len(user_stack)!=0 and (val > arr[user_stack[-1]]):
            #going to pop and calculate water storage
            #get the height of the top of the stack element
            temp_height = arr[user_stack[-1]]
            user_stack.pop()
            if len(user_stack) == 0:
                break

            #get distance between current pos and element next to the pop element value
            distance = pos - user_stack[-1] - 1

            #check the max height between current element and previous to measure the quantity this can store

            max_height = min(arr[pos],arr[user_stack[-1]]) - temp_height

            max_storage += distance*max_height
        #if stack is empty or current val is smaller than the top of the stack element value then push the pos to the stack
        user_stack.append(pos)

    return max_storage

trap_rain_water([4, 2, 0, 0,3, 2, 5])

class TestMyProgram(unittest.TestCase):

    def test_add_numbers(self):
        # Test case 1
        result = trap_rain_water([4,2,0,3,2,5])
        self.assertEqual(result, 9)


        # Test case 2
        result = trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1])
        self.assertEqual(result, 6)

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()