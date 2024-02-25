import random
import string
import math

###############################################################################

# print("hello")
# name = input("what is your name: ")
# print("your name is: " + name)

###############################################################################

# fruits = ["a", "b", "c"]
# for fruit in fruits:
#     print(fruit)

###############################################################################

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

###############################################################################

# scores = "78 65 89 86 55 91 64 89"
# max_value = 0
# scores_list = scores.split()
# for score in scores_list:
#     if int(score) > max_value:
#         max_value = int(score)
# print(f"max score: {max_value}")

###############################################################################

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

###############################################################################

# def paint_calc(height, width, cover):
#     cans = math.ceil(height * width / cover)
#     return cans
# h = int(input("height: "))
# w = int(input("width: "))
# c = int(input("coverage: "))
# ans = paint_calc(h, w, c)
# print(f"cans: {ans}")

###############################################################################

# def prime_checker(number):
#     for i in range(2, number):
#         if i == 1 or i == number:
#             continue
#         elif number % i == 0:
#             print("divisible by 0, not a prime number")
#             break
#         else:
#             print(f"i: {i}")
# n = int(input("find prime of: "))
# prime_checker(n)

###############################################################################

# alphabet = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
#
#
# # print(alphabet)
#
# def encrypt(text, shift):
#     final_string = ""
#     for c in text:
#         pos_1 = alphabet.index(c)
#         pos_2 = pos_1 + shift
#         final_string += alphabet[pos_2]
#     print(f"encoded string: {final_string}")
#
#
# def decrypt(text, shift):
#     final_string = ""
#     for c in text:
#         pos_1 = alphabet.index(c)
#         pos_2 = pos_1 - shift
#         final_string += alphabet[pos_2]
#     print(f"encoded string: {final_string}")
#
#
# should_continue = True
# while should_continue:
#     direction = input("enter encode or decode: ")
#     text = input("message: ")
#     shift = int(input("shift: "))
#
#     if direction == "e":
#         encrypt(text, shift)
#     elif direction == "d":
#         decrypt(text, shift)
#     else:
#         print("bad input")
#
#     answer = input("should continue (yes or no): ")
#     if answer.lower() == "no":
#         should_continue = False

###############################################################################

# import random
#
# grades = {name: int(random.uniform(60, 100)) for name in
#             ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack"]}
# for name in grades:
#     if grades[name] >= 90:
#         note = "Outstanding"
#     elif grades[name] >= 80:
#         note = "Good"
#     elif grades[name] >= 70:
#         note = "OK"
#     else:
#         note = "Do better"
#     print(f"{name}: {grades[name]} - {note}")

###############################################################################

# bidding

# import os
#
# still_bidding = True
# max_bid = 0
# highest_bidder = ""
#
# while still_bidding:
#     os.system('clear')
#     name = input("enter name: ")
#     bid = int(input("enter amount: "))
#     if bid > max_bid:
#         max_bid = bid
#         highest_bidder = name
#     more = input("continue (yes or no): ")
#     if more == "no":
#         still_bidding = False
#
# print(f"highest bidder {highest_bidder}, amount of ${max_bid}")

###############################################################################

# import os
#
# # for windows
# if os.name == 'nt':
#     _ = os.system('cls')
#     print("nt")
#
# # for mac and linux(here, os.name is 'posix')
# else:
#     _ = os.system('clear')
#     print("mac or linux")

###############################################################################

# import os
#
# still_bidding = True
# highest_bid = 0
# highest_bidder = ""
# bidders = {}
#
# while still_bidding:
#     os.system('clear')
#     name = input("enter name: ")
#     bid = int(input("enter amount: "))
#     bidders[name] = bid
#     if bid > highest_bid:
#         highest_bid = bid
#         highest_bidder = name
#     more = input("continue (yes or no): ")
#     if more == "no":
#         still_bidding = False
#
# # print(f"highest bidder {highest_bidder}, amount of ${max_bid}")
#
# highest_bidder = max(bidders, key = bidders.get)
# highest_bid = bidders[highest_bidder]
# print(f"bidders: {bidders}")
# print(f"highest bidder {highest_bidder}, amount of ${highest_bid}")

###############################################################################



###############################################################################


###############################################################################


###############################################################################


###############################################################################


###############################################################################


###############################################################################


###############################################################################


###############################################################################
