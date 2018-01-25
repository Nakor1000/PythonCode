seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
print "Length of Sequence -",
print len(seq)
print "Exons are in uppercase letters."
print "Introns are in lowercase letters."
loc1 = str(seq[0:63]).upper()
loc2 = str(seq[63:91]).lower()
loc3 = str(seq[91:len(seq)]).upper()
print '%s' % loc1+loc2+loc3





