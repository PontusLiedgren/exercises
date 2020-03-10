# PontusLiedgren/exercises
# (C) Pontus Liedgren 2019
# https://github.com/PontusLiedgren/exercises


# imports
import time
import math

##########################################
# övning-1
# huvudloop

def number_print(x):
    NumberOn = True
    while NumberOn:
        print(x)
        time.sleep(1)
        x += 1
    return number_print
# Ta bort kommentaren nedan för att testa funktionen
#number_print(0)

#########################################
# övning-2
# function
def questionify(user_input):
    print(user_input + "?")
    return questionify

# Ta bort kommentaren nedan för att testa funktionen
#questionify("Jag heter Pontus")

#########################################
# övning-3
# input


# function
def divisible_by_five(number_input):
    if number_input % 2 == 0 and number_input % 5 == 0:
        return True
    else:
        return False
# Ta bort kommentaren nedan för att testa funktionen
# user_number_input = int(input("Säg ett nummer: "))
# divisible_by_five(user_number_input)

##########################################
<<<<<<< HEAD
print(divisible_by_five(20))
=======
# uppgift-8
my_list = ["tokyo", "madrid", "stockholm"]
def contains(my_list, string):
    if string in my_list:
        return True
    if string not in my_list:
        return False
# print(contains(my_list, "tokyo"))
# print(contains(my_list, "madrid"))
# print(contains(my_list, "baltikum"))

###########################################
>>>>>>> e608ae0bd137fb1911676eda052b0bd3af1c94f8
