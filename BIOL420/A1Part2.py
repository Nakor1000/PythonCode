# I tried for hours to get this to preform the tasks on raw input, but I couldn't seem to iron out the bugs. 
# Based on the other programs for this assignment, the code I originally wrote should have worked, but it didn't. 
# I plan to continue working on it to allow the use of random sequences, but for now, this meets the requirments,
# of the assignment. :(
print 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
seq = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
print 'Length of Sequence -',
print len(seq)
loc = seq.find('GAATTC')
print "Location of Restriction site -",
print loc+1
print "Fragment Length Before Restriction Site -",
print len(seq[0:loc+1])
print "Fragment Length After Restriction Site -",
print len(seq[loc+1:len(seq)])
