#functions
def addTwo (x): #this function takes the parameter x and adds 2 onto it
    return x+2
def subTwo (number):
    return number - 2 #this function takes the parameter x and subtracks 2 from it

Newnumber = subTwo(2)
print(addTwo(4))
print(Newnumber)

def printstring(string):
    print(string[1:5]) #this function prints the second letter all the way to the fourth letter of a string. as a string starts at [0]

printstring("hello") #removes the h
printstring("my name is")

file = open('file.txt', 'w')

file.write("python/n")
file.write("i am learning how to write a character")

file.close()
