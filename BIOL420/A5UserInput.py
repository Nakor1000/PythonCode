from BIOL420 import translate_dna

print 'Enter codon sequence:',
seq = raw_input().upper()
print 'Protein:'+' '+translate_dna(seq)

# This is my program that uses user input to translate a genetic sequence into a protein.