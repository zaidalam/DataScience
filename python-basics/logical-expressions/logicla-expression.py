"""
Exercise- logical expressions:
Write a python program that takes a student's score as input and assigns a grade based on the following criteria:
if score is 90 or above, the grade is A
if the score is 80 or above but less then 90, the grade is B
if the score is 70 or above but less then 80, the grade is C
if the score if below 70, the grade is F


score = 70
result = ""
if score >= 90:
    result = "A"
elif score >= 80:
    result = "B"
elif score >= 70:
    result = "C"
else:
    result = "F"

print("Grade", result)
"""

age = 19
hasLicense = False

if age >= 18 and hasLicense == True:
    result = "You can drive!"
else:
    result = "You cannot drive!"

print(result)