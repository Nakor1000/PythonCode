print "Enter Sequence:",
sequence = raw_input()
answer = []
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

for nucleotide in sequence:
    answer.append(complement[nucleotide])

print ''.join(answer)
