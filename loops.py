print "Enter Your Name",
name = raw_input()
for let in name:
    print let

l = ['Dog', 'Ferret', 'Shark']
for animal in l:
    print animal
print 'Done'

f = open('sequence.txt')
for line in f:
    print len(line.rstrip('\n'))

f2 = open('sequence.txt')
lines = f2.readlines()
for line in lines:
    print line.rstrip('\n')
for num in range(1, len(lines)+1):
    print num



