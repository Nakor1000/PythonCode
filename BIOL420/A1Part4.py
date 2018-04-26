seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
print "Length of Sequence -",
print len(seq)
print "Exons are in uppercase letters."
print "Introns are in lowercase letters."
loc1 = str(seq[0:63]).upper()
loc2 = str(seq[63:91]).lower()
loc3 = str(seq[91:len(seq)]).upper()
print "Sequence:",
print '%s' % loc1+loc2+loc3
# This program would have been extremely involved if I were to try and make it work for any random sequence.
# The main problem is how to get the program to recognize when there is an exon or intron. 

# At first I wrote 3 print lines with an '%s' function for each location,
# however I realized it's much simpler to use one print '%s' function and link the strings together with + signs.
# The orginial way I did it left spaces between the exons and intron.




