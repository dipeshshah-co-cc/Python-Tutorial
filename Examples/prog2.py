'''
"Basic While Loop"
x = 10
while x != 0:
    print x
    x = x - 1
    print "wow, we've counted x down, and now it equals", x
print "And now the loop has ended."
'''


'''
# if elif else
a = 10
while a > 0:
    print a
    if a > 5:
        print "Big number!"
    elif a % 2 != 0:
        print "This is an odd number"
        print "It isn't greater than five, either"
    else:
        print "this number isn't greater than 5"
        print "nor is it odd"
        print "feeling special?"
    a = a - 1
    print "we just made 'a' one less than what it was!"
    print "and unless a is not greater than 0, we'll do the loop again."
print "well, it seems as if 'a' is now no bigger than 0!"
print "the loop is now over, and without furthur adue, so is this program!"
'''


'''
# Below is the function
def hello():
    print "hello"
    return 1234

# And here is the function being used
print hello()
'''


'''
# calculator program using function

# NO CODE IS REALLY RUN HERE, IT IS ONLY TELLING US WHAT WE WILL DO LATER
# Here we will define our functions
# this prints the main menu, and prompts for a choice
def menu():
    #print what options you have
    print "Welcome to calculator.py"
    print "your options are:"
    print " "
    print "1) Addition"
    print "2) Subtraction"
    print "3) Multiplication"
    print "4) Division"
    print "5) Quit calculator.py"
    print " "
    return input ("Choose your option: ")
    
# this adds two numbers given
def add(a,b):
    print a, "+", b, "=", a + b
    
# this subtracts two numbers given
def sub(a,b):
    print b, "-", a, "=", b - a
    
# this multiplies two numbers given
def mul(a,b):
    print a, "*", b, "=", a * b
    
# this divides two numbers given
def div(a,b):
    print a, "/", b, "=", a / b
    
# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(input("Add this: "),input("to this: "))
    elif choice == 2:
        sub(input("Subtract this: "),input("from this: "))
    elif choice == 3:
        mul(input("Multiply this: "),input("by this: "))
    elif choice == 4:
        div(input("Divide this: "),input("by this: "))
    elif choice == 5:
        loop = 0

print "Thankyou for using calculator.py!"
'''


'''
print "len([1, 2, 3]):: ", len([1, 2, 3])
print "[1, 2, 3] + [4, 5, 6]:: ", [1, 2, 3] + [4, 5, 6]
print "['Hi!'] * 4:: ", ['Hi!'] * 4
print "3 in [1, 2, 3]:: ", 3 in [1, 2, 3]
for x in [1, 2, 3]: print x
student_rec = ['dave', 'B', 10, 'jane', 'B', 12, 'john', 'A', 15]
print sorted(student_rec, key=lambda student: student[1])   # sort by Grade
'''


#print sorted(['dave', 'B', 10, 'jane', 'B', 12, 'john', 'A', 15], reverse=True)


#print sorted("This is a test string from Andrew".split(), key=str.lower)


'''
strs = ['hello', 'and', 'goodbye']
shouting = [ s.upper() + '!!!' for s in strs ]
print strs
print shouting
'''



#Make the phone book:
phonebook = {'Andrew Parson':8806336, \
'Emily Everett':6784346, 'Peter Power':7658344, \
'Lewis Lame':1122345}
print phonebook

phonebook['Gingerbread Man'] = 1234567
print phonebook

del phonebook['Peter Power']
print phonebook

