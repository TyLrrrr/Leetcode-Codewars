# LeetcodeChallenge: create a roman numeral to integer converter
class Solution(object):
    def romanToInt(self, s):
        romNum = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        stest = s[::-1]
        sum = 0
        y = 0
        for i in stest:
            if romNum[i] >= y:
                sum += romNum[i]
            else:
                sum -= romNum[i]
            y = romNum[i]
        return sum
