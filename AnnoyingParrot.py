import time
from string import whitespace, punctuation


# This prints a string up to a certain number of times equaling the number of characters in the string.  
print "I'm a parrot! Teach me a phrase! SQUAK!",
parrot = raw_input()              
count =  range(0, int(len(parrot.translate(None, punctuation).translate(None, whitespace))),
(int(len(parrot.translate(None, punctuation).translate(None, whitespace)))-(int(len(parrot.translate(None, punctuation).translate(None, whitespace))-1))))
for i in count:
    print 'SQUAK!',
    print parrot 
    time.sleep(1.5)


print str('That phrase had %s letters in it! SQUAK!') % len(parrot.translate(None, punctuation).translate(None, whitespace))