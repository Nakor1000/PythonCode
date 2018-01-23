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
