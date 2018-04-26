import BIOL420 as bio

csv = open('data.csv', 'r')

print 'Gene   | % AT  | AT Content | Species'
print '_'* 57
for line in csv:
    data = line.split(',')
    species = data[0]
    seq = data[1]
    gene = data[2]
    bases = data[3]
    print gene+ ' | ' + bio.atcontent(seq)+' |',
    if bio.low(seq):
        print ' Low       | '+ species 
    elif bio.medium(seq):
        print ' Medium    | '+ species
    elif bio.high(seq):
        print ' High      | ' + species

# This is a script that utilizes three seperate
#functions to return True based on three parameters.
#These parameters are based on relative adenine and thymine content in genetic sequences, 
#and are given designations of "High, Medium or Low". 


