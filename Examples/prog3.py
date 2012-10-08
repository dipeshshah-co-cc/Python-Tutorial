'''
for x in range(0, 3):
    print "We're on time %d" % (x)

string = "Hello World"
for x in string:
    print x

collection = ['hey', 5, 'd']
for x in collection:
    print x
'''




'''
# cheerleading program using for loop
word = raw_input("Who do you go for? ")

for letter in word:
    call = "Say " + letter + "!"
    print call
    print letter + "!"

print "What does that spell?"
print word + "!"
'''



#Class
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
    self.y = self.y * scale


#Inheritance
class Square(Shape):
    def __init__(self,x):
        self.x = x
	self.y = x

