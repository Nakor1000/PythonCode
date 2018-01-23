# I did a lot of googling to teach myself how to form the compliment 
print "Enter Sequence:",
spaces = " "*15
sequence = raw_input().upper()
answer = []
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
for nucleotide in sequence:
    answer.append(complement[nucleotide])
ans = ''.join(answer) 
print '%s' % spaces,
print '%s' % ans
# I feel like I could tidy this up a bit. 
