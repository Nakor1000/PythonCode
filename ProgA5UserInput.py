from bioinformatics import translate_dna

print 'Enter a DNA sequence:',
seq = raw_input().upper()
print 'Protein:'+' '+translate_dna(seq)

# This is my program that uses user input to translate a genetic sequence into a protein.