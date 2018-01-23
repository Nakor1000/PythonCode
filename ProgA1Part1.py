# At first I wrote a program to do the calculations with the given sequence hard coded into the language, however, I realized it would be much more useful 
# to be able to enter in any sequence we want and get the correct calculations. 
print "Enter Sequence:",
# Be sure to enter your sequence in all uppercase letters.
sequence = raw_input().upper()
T = sequence.count('T')
print "T -",
print '%s' % T
A = sequence.count('A')
print "A -",
print '%s' % A
total = int(A) + int(T)
print "Total A's and T's -",
print '%s' % total
totalbases = len(sequence)
print "Total bases in sequence -",
print '%s' % totalbases
print "AT content -",
print '%.2f' % (total/(totalbases/1.0)*100)+'%'
# It took me a little while to figure out how to force floating point division without having a definite decimal in the values I was using. 
# It turns out you can simply divide one side of the equation by 1.0, and it funtions the same as if your value was a decimal. 
# In this case, the value in question was the calculated length of the sequence entered. 
