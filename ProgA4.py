import re
splice = [0]
message = str("One fragment size is")
data = open("dna.txt", "r")

for seq in data:
    pass
strand = len(seq)-1
seqUpper = seq.upper()

for match in re.finditer(r"A.TAAT", seqUpper):
    splice.append(match.start() + 3)
    pass

for match in re.finditer(r"GC(A|G)(A|T)TG", seqUpper):
    splice.append(match.start() + 4)
    pass

lis = sorted(splice+[strand])
print lis 
print message +' '+str(lis[1]-lis[0])+'.'
print message +' '+str(lis[2]-lis[1])+'.'
print message +' '+str(lis[3]-lis[2])+'.'
print message +' '+str(lis[4]-lis[3])+'.'
print message +' '+str(strand-lis[4])+'.'










        
    

