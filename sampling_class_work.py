import random
import string
import math

# print("hello")
# name = input("what is your name: ")
# print("your name is: " + name)

# fruits = ["a", "b", "c"]
# for fruit in fruits:
#     print(fruit)

# height_total = 0
# height_list = "156 178 165 171 187 199"
# for height in height_list.split():
#     print(height)
#     height_total += int(height)
# print(f"height total: {height_total}")
# students_count = len(height_list.split())
# print(f"count of students: {students_count}")
# avg = round(height_total / students_count)
# print(f"average height: {avg}")

# scores = "78 65 89 86 55 91 64 89"
# max_value = 0
# scores_list = scores.split()
# for score in scores_list:
#     if int(score) > max_value:
#         max_value = int(score)
# print(f"max score: {max_value}")

# total = 0
# highest = input("highest: ")
# for num in range(0, int(highest) + 1, 2):
#     total += int(num)
# print("total: " + str(total))

# nums = range(1,100)
# for num in nums:
#     if num % 3 == 0 and num % 5 != 0:
#         print("fizz")
#     elif num % 3 != 0 and num % 5 == 0:
#         print("buzz")
#     elif num % 3 == 0 and num % 5 == 0:
#         print("fizz buzz")
#     else:
#         print(num)

def paint_calc(height, width, cover):
    cans = height * width / cover
    return cans
h = int(input("height: "))
w = int(input("width: "))
c = int(input("coverage: "))
ans = math.ceil(paint_calc(h, w, c))
print(f"cans: {ans}")
