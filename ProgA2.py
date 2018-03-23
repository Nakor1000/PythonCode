import Bioinformatics
print "Enter Amino Sequence",
seq = raw_input().upper()
print "Enter Residues Without Spaces:",
res = raw_input().upper()
Bioinformatics.pctOfProtein(seq, res)

#After playing around with this function, I realized it's only useful if you want to find out 
# what the percentage is for a single amino acid. This is because, even though the program 
# returns the percentage of your sequence that is comprised of the list of amino acids you enter,
# it doesn't give you a detailed breakdown of the precentage of each individual residue in the list. It could... it just needs more work....  
