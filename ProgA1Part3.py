# I did a bit of googling to find out how to form complimentary values. 
cyan  = "\033[1;36m"
reset = "\033[0;0m"
import sys
print "Enter Sequence:",
spaces = " "*15
sequence = raw_input().upper()
answer = []
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
for basepair in sequence:
    answer.append(complement[basepair])
ans = ''.join(answer)
sys.stdout.write(cyan)
print '%s' % spaces,
print '%s' % ans 
# I made the complimentray strand a different color, because if you put in a sequence
# long enough that it occupies more than one line, then it becomes hard to keep track 
# of which strand is which. Making the output a different color makes it easier to tell. 
