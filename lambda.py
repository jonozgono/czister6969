# str = "abcdefgh"
#
# print(str[2::-1])



# numbers = [3,7,9,12]
#
# a = numbers[0]
# b = numbers[1]
# c = numbers[2]
# d = numbers[3]
#
# print(a+b+c+d)
#
# def min():
#     if(a<b and a<c and a<d):
#         return a
#     elif(b<a and b<c and b<d):
#         return b
#     elif(c<a and c<b and c<d):
#         return c
#     elif(d<a and d<b and d<c):
#         return d
# print (min())



# numbers =[3,51,2,8,6]
#
# print(sorted(numbers, reverse =True))
# print (numbers)
#
#
# items = [
#     ("product 1", 123),
#     ("product 2", 12),
#     ("product 3", 8123)]
#
# def sort_item(item):
#      return item[1]
#
# items.sort(key=lambda item: item[1])
# print(items)


students = [
    {"imie": "Jan", "wiek":20},
    {"imie": "Karolina", "wiek":15},
    {"imie": "Brunhilda", "wiek":185}]

def sort_min_wiek():
    students.sort(key = lambda w:w["wiek"])
    return students
print (sort_min_wiek())