import bioinformatics as bio

csv = open('data.csv', 'r')

print 'Gene   | % AT  | AT Content | Species'
print '_'* 57
for line in csv:
    data = line.split(',')
    species = data[0]
    seq = data[1]
    gene = data[2]
    bases = data[3]
    print gene+ ' |',
    print bio.atcontent(seq)+' |',
    print bio.ATmagnitude(seq)+'     |',
    print species
    
  

    