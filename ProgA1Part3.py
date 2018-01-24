# I did a bit of googling to find out how to form complimentary values. 
print "Enter Sequence:",
spaces = " "*15
sequence = raw_input().upper()
answer = []
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
for basepair in sequence:
    answer.append(complement[basepair])
ans = ''.join(answer) 
print '%s' % spaces,
print '%s' % ans
# I feel like I could tidy this up a bit. 
