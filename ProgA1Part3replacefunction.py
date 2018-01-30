cyan  = "\033[1;36m"
reset = "\033[0;0m"
import sys
print "Enter Sequence:",
spaces = " "*15
sequence = raw_input().upper()
complement = sequence.replace('A', 't').replace('G', 'c').replace('T', 'a').replace('C', 'g')
sys.stdout.write(cyan)
print '%s' % spaces,
print '%s' % complement.upper()
