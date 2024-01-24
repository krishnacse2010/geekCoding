import unittest


def transformString(str1):
    if len(str1)==0:
        print("Empty input")
    hashMap = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k',
               '12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z'}

    i = 0
    n= len(str1)
    tString =""
    while i < n :
        if i+2 < n:
            if str1[i+2]=='#':
                tStr = str1[i:i+2]
                try:
                    tString += hashMap[tStr]
                except:
                    print('Input String doesnt match the criteria ,should be between 0-25')
                    break
                i += 3
            else:
                tStr = str1[i]
                try:
                    tString += hashMap[tStr]
                except:
                    print('Input String doesnt match the criteria ,should be between 0-25')
                    break
                i += 1
        else:
            tStr = str1[i]
            try:
                tString += hashMap[tStr]
            except:
                print('Input String doesnt match the criteria ,should be between 0-25')
                break
            i += 1

    return tString

#print(transformString("12322#"))

class TestMyProgram(unittest.TestCase):

    def test_add_numbers(self):
        # Test case 1
        result = transformString("12322#")
        self.assertEqual(result, 'abcv')


        # Test case 2
        result = transformString("123")
        self.assertEqual(result, 'abc')

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()