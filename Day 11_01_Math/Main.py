'''
What you know so far.

Basics of Variables
Variable Reassignment.
Assignment Operator:  =
The assignment operator assigns values or
new values to variables.

There are 9 mathematical operators:
binary

+ : Addition
- : Subtraction
* : Multiplication
/ : Division
** : Exponentiation
// : Floor Division
% : Modulus

unary
- : Unary minus, makes a number negative
+ : Unary plus, makes a number positive

Mathematical Assignment Operators
7
all binary

+= : Addition Assignment Operator
-= : Subtraction Assignment Operator
*= : Multiplication Assignment Operator
/= : Division Assignment Operator
**= : Exponentiation Assignment Operator
// : Floor Division Assignment Operator
%= : Modulus Assignment Operator
'''

sum = 34 + 42
print("The sum of 34 and 42 is:", sum)
difference = 42 - 34
print("The difference of 42 and 34 is:", difference)
a = 34.0
b = 42.0
product = a * b
print("The product of a and b is:", product)
quotient = a / b
print("The quotient of a and b is:", quotient)

# Divison by zero is not possible in python
# b = 0.0
# quotient = a / b
# print("The quotient of a and b is:", quotient)

c = 7
d = 4
answer = c ** d
print("The answer is:", answer)

floor_division = c // d
print("The floor division is:", floor_division)

f = 5
f = -f
print("The f is:", f)

c = 8
d = 5
quotient = c // d
remainder = c % d
print("c divided by d is:", quotient, "R", remainder)

print("c divided by d is:", c / d)

a = 5
a = a + 1

b = 7
a = a + b
print(a)

a = 5
a += 1
a -= 1
a *= 1
a /= 2
a **= 2
a //= 2
a %= 2
print(a)

'''
Please -> Parentheses or Grouping Symbols
Excuse -> Exponentiation
My -> Multiplication and Division
Dear -> Multiplication and Division
Aunt -> Addition
Sally -> Subtraction 
'''

x = ((3+2) + 5) ** 2 + 7
print(x)

y = 2 ** 3 ** 2
# Chained exponent.   right to left
# 2 ** 9
# 512
print(y)

z = 2 / 3
print(z)

a = 0.1
print(a + a + a)
