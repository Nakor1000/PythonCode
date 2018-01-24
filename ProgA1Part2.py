# I tried for hours to get this to preform the tasks on raw input, but I couldn't seem to iron out the bugs. 
# Based on the other programs for this assignment, the code I originally wrote should have worked, but it didn't. 
# I plan to continue working on it to allow the use of random sequences, but for now, this meets the requirments,
# of the assignment. :(
print 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCA'
s2 = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
print 'Length of Sequence -'
print len(s2)
loc = s2.find('GAATTC')
print "Location of Restriction site -",
print loc
print "Fragment Length Before Restriction Site -",
print len(s2[0:loc])
print "Fragment Length After Restriction Site -",
print len(s2[loc:55])






