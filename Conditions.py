# Well done

# CONDITIONS (15PTS TOTAL)

# PROBLEM 1 (GPA - 4pts)
# Grades are values between 0 and 100
# We will translate grades to letters using:
# http://www.collegeboard.com/html/academicTracker-howtoconvert.html
# Make a variable for your percentage grade.
# Make a series of if/elif/else statements to print the letter grade.
# If the user enters a grade lower than zero or higher than 100, just give an error message.
# Don't worry about making an exception for these right now.
percentage = 95
if percentage >= 0 or percentage <= 100:
    if percentage >= 97:
        print("A+")
    elif percentage >= 93:
        print("A")
    elif percentage >= 90:
        print("A-")
    elif percentage >= 87:
        print("B+")
    elif percentage > 83:
        print("B")
    elif percentage >= 80:
        print("B-")
    elif percentage >= 77:
        print("C+")
    elif percentage >= 73:
        print("C")
    elif percentage >= 70:
        print("C-")
    elif percentage >= 67:
        print("D+")
    elif percentage >= 65:
        print("D")
    else:
        print("Your grade is very unsatisfactory")
else:
    print("ERROR")

# PROBLEM 2 (Vowels - 5pts)
# Ask the user to supply a string.
# Print how many different vowels there are in the string.
# The capital version of a lower case vowel is considered to be the same vowel.
# y is not considered a vowel.
# Try to print proper output (e.g., printing “There are 1 different vowels in the string” is ugly).
# Example: When the user enters the string “It’s Owl Stretching Time,”
# the program should say that there are 3 different vowels in the string.

string_var = input("Please enter your string: ").lower()
number_of_vowels = 0
count_i = 0
count_a = 0
count_e = 0
count_u = 0
count_o = 0
for i in range(len(string_var)):
    if string_var[i] == "i":
        if count_i < 1:
            number_of_vowels += 1
            count_i += 1
    if string_var[i] == "a":
        if count_a < 1:
            number_of_vowels += 1
            count_a += 1
    if string_var[i] == "e" and count_e < 1:
        number_of_vowels += 1
        count_e += 1
    if string_var[i] == "o" and count_o < 1:
        number_of_vowels += 1
        count_o += 1
    if string_var[i] == "u" and count_u < 1:
        number_of_vowels += 1
        count_u += 1
if number_of_vowels > 1:
    print("There are", number_of_vowels, "different vowels in the sentence")
elif number_of_vowels == 1:
    print("There is only one vowel in the sentence")
else:
    print("There are no vowels in your sentence")

# PROBLEM 3 (Quadratic Equation - 6pts)
# You can solve quadratic equations using the quadratic formula.
# Quadratic equations are of the form Ax2 + Bx + C = 0.
# Such equations have zero, one or two solutions.
# The first solution is (−B + sqrt(B^22 − 4AC))/(2A).
# The second solution is (−B − sqrt(B^2 − 4AC))/(2A).
# There are no solutions if the value under the square root is negative.
# There is one solution if the value under the square root is zero.
# Write a program that asks the user for the values of A, B, and C,
# then reports whether there are zero, one, or two solutions,
# then prints those solutions.
# Note: Make sure that you also take into account the case that A is zero,
# and the case that both A and B are zero.
import math as m

print("Welcome to the quadratic solver")
a = int(input("Please insert value a: "))
b = int(input("Please insert value b: "))
c = int(input("Please insert value c: "))

if (b ** 2 - 4 * a * c) == 0:
    print("There is one solution to this quadratic and that is: ", b / 2 * a)
elif (b ** 2 - 4 * a * c) > 0:
    print("The first solution is: ", (-b + m.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
    print("The second solution is:", (-b - m.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
elif (b ** 2 - 4 * a * c) < 0:
    print("There are no real solutions for your quadratic")
