#This is the print function. It prints the literal string in single or double quotes.
print("Hello World")
print("Hi Again")
#You can separate words by a comma.  A space appears automatically.
print("Hi", "Again")
#You can change the word separator by adding sep="".  And put the separator in the quotes.
print("Hi", "Again", sep="-")
#You can change the ending part by end="".  Defaults to new line character.  Put the end string in the quotes.
print("Hi", "Again", end="#")
print("Hi", "Again", end="\n")

#You can print a string of text by wrapping the text in single or double quotes, but not both at same time.
print("double quotes")
print('single quotes')
#The next line is commented out because it's broken.
#So the python interpreter will ignore it when your code is run.
#print("mixed quotes')

#prints a single quote
print('\'')
#prints a double quote
print("\"")
# prints 1 backslash
print("\\")
#prints 2 backslashes
print("\\\\")

#prints a tab of 4 spaces followed by the word Hello
print("\tHello")
#prints a extra newline.
print("\n")
print("Hello")

#This is a multiline comment.
#It is written with hashtags.
#But there is a better way

'''
This is a multiline comment.
Feel free to space them out.

Starts and ends with three single quote marks
'''
