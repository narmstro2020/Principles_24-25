'''
str() : converts whatever you put in the parenthesis to text
int() : converts whatever you put in the parenthesis to integer
float() : converts whatever you put in the parenthesis to float
'''

age_text = "42"
print(age_text)
print(type(age_text))
age_int = int(age_text)
print(age_int)
print(type(age_int))
age_float = float(age_text)
print(age_float)
print(type(age_float))

#Simple height converted to feet and inches into meters.

feet = int(input("How many feet tall are you: "))
inches = int(input("How many inches tall are you leftover: "))
inches_to_meters = 0.0254
total_inches = feet * 12 + inches
total_meters = total_inches * inches_to_meters
print("Your height is", feet, "feet", inches, "inches")
print("Your height is", feet, "'", inches, "\"")
print("You height is", total_inches, "inches")
print("Your height is", total_meters, "meters")

feet_as_text = str(feet)
print(type(feet_as_text))



