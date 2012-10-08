# Open a file
import os
os.mkdir("/media/sda5/python/file")
os.chdir("/media/sda5/python/file")
fo = open("foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");

# Close opend file
fo.close()

