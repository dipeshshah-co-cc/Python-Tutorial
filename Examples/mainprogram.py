### mainprogam.py
### IMPORTS ANOTHER MODULE
import moduletest

print moduletest.ageofqueen
cfcpiano = moduletest.Piano()
cfcpiano.printdetails()


### IMPORT ITEMS DIRECTLY INTO YOUR PROGRAM

# import them
from moduletest import ageofqueen
from moduletest import printhello

# now try using them
print ageofqueen
printhello()



