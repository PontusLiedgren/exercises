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
    if_divisible = number_input/5
    print(if_divisible.is_integer())
    return number_input
# Ta bort kommentaren nedan för att testa funktionen
#user_number_input = int(input("Säg ett nummer: "))
#divisible_by_five(user_number_input)

##########################################
