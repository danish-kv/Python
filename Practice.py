# first = 0
# second = 0
#
# myList = [12, 65, 78, 3, 9, 2, 4, 5, 6, 34]
#
# for i in range(len(myList)):
#     if myList[i] > first:
#         first = myList[i]
#     elif myList[i] < first and myList[i] > second:
#         second = myList[i]
#
# print(first,second)


# def romanToInt(s: str) -> int:
#     translations = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000
#     }
#     number = 0
#     s = s.replace("IV", "IIII").replace("IX", "VIIII")
#     s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#     s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#     for char in s:
#         number += translations[char]
#     return number
#
#
# print(romanToInt('MCMXCIV'))



myList = [1,1,1,4,4,4,4,3,2,5]
# print(myList.count(max(myList)))
print(max(myList,key=myList.count))

