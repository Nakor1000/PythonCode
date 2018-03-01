#This is my AT content function(use Bioinformatics.ATcontent)
#This needs to be made into a proper function without user input
def ATcontent(prompt):
    print prompt,
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
    
#This is my complimentary DNA sequence generator.(Use Bioinformatics.CompStrand) 
#This needs to be made into a proper function without user input
def CompStrand(prompt):
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
    
def pctOfProtein(polypeptide, residues):
    total = len(polypeptide) #gives total length of sequence entered
    count = 0 #This holds a count of residues, because you can't add to nothing, so instead we say "zero +" 
    print 'Length of Polypeptide:',
    print total
    for let in residues: #This loops allows the program to cycle through the sequence in search of given residues
        count = count + polypeptide.count(let)
    print 'Percent of Residues:',
    print '%.2f' % (count/(total/1.0)*100)+'%' #This is the calculation for percentages.
    