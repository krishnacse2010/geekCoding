from collections import deque
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = deque()
        for elem in operations:
            print(elem)
            if elem not in ["+","D","C"]:
                s.append(int(elem))
            elif elem == "D":
                top_element=s[-1]
                s.append(top_element*2)
                print(s)
            elif elem=="+":
                if s[-1]:
                   top_element=s[-1]
                if s[-2]:
                   top_element_1 = s[-2]
                s.append(top_element+top_element_1)
            elif elem=="C":
                s.pop()
        return sum(list(s))