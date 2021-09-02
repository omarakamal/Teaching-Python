#if statement
is_male = False #create boolean expressions
is_tall = False

if is_male or is_tall:
    print("you are a male or tall or both") #if both of these conditions are satisfied then the machine will print this
elif is_male and not(is_tall):
    print("you are a male and short") #this will print only if the is_male condition is true
elif not(is_male) and is_tall:
    print("you are not a male and tall") #this prints only if the is_tall condition is true
else:
    print("you are a female and short") #else is used as a catch all for if none of the other conditions are met

words = input("enter a word: ")
