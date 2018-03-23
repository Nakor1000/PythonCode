#This is my AT content function(use bioinformatics.atcontent)
def atcontent(sequence):
    seqUpper = sequence.upper()
    T = seqUpper.count('T')
    A = seqUpper.count('A')
    total = int(A) + int(T)
    totalbases = len(sequence)
    percent = '%.2f' % (total/(totalbases/1.0)*100)
    return percent
    

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
    polypeptideUpper = polypeptide.upper()
    total = len(polypeptide) #gives total length of sequence entered
    count = 0 #This holds a count of residues, because you can't add to nothing, so instead we say "zero +" 
    print 'Length of Polypeptide:',
    print total
    for let in residues: #This loops allows the program to cycle through the sequence in search of given residues
        count = count + polypeptideUpper.count(let.upper())
    print 'Percent of Residues:',
    print '%.2f' % (count/(total/1.0)* 100)+'%' #This is the calculation for percentages.


def ATmagnitude(sequence):
    if float(atcontent(sequence)) <= 45.00:
        return str('Low')
    elif 65.00 > float(atcontent(sequence)) > 45.00: 
        return str('Medium')
    elif float(atcontent(sequence)) >= 65.00:
        return str('High')    
    


def low(sequence):
    if float(atcontent(sequence)) <= 45.00:
        return True
    
    
def medium(sequence):
    if 65.00 > float(atcontent(sequence)) > 45.00: 
        return True
    

def high(sequence):
    if float(atcontent(sequence)) >= 65.00:
        return True

    