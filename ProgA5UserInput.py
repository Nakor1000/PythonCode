from bioinformatics import translate_dna

print 'Enter a DNA sequence:',
seq = raw_input().upper()
print 'Protein:'+' '+translate_dna(seq)