#This is my AT content function(use bioinformatics.atcontent)
#This was recently made into a proper function. :)
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

#This function performs the 3 following functions in one.
def ATmagnitude(sequence):
    if float(atcontent(sequence)) <= 45.00:
        return str('Low')
    elif 65.00 > float(atcontent(sequence)) > 45.00: 
        return str('Medium')
    elif float(atcontent(sequence)) >= 65.00:
        return str('High')    
    

#This function looks for genetic sequences with contents of Adenine and Thymine at 45% and below. 
def low(sequence):
    if float(atcontent(sequence)) <= 45.00:
        return True
    
#This function looks for genetic sequences with contents of Adenine and Thymine from 45.01% up to 64.99%.    
def medium(sequence):
    if 65.00 > float(atcontent(sequence)) > 45.00: 
        return True
    
#This function looks for genetic sequences with contents of Adenine and Thymine at 65% and above.
def high(sequence):
    if float(atcontent(sequence)) >= 65.00:
        return True


def translate_dna(seq): # This is my homework for ProgA5. It translates genetic sequences into the corresponding polypeptides. 
      
    codons = { # This is the dictionary relating codons(keys) to amino acids(values).           
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',}
    
    polypeptide ="" # This line allows me to begin building my polypeptide, starting with zero amino acids.
    if len(seq)%3 == 0: # This makes sure that the sequence entered is divisible by 3, since codons are 3 bases long.
        for i in range(0, len(seq), 3): # This loop moves over the sequence and slices out the codons, then joins the resulting values together.
            codon = seq[i:i + 3]
            polypeptide += codons[codon]
        return polypeptide # this returns a polypeptide translated from the entered DNA sequence. 
    else:
        return 'Error: Sequence not divisible by 3. Cannot be translated.' # This gives an error message if the DNA sequence has too many or too few bases. 