import re #imports regular expression module
splice = [0] 
message = str("One fragment size is") #This makes it faster to print this.
data = open("dna.txt", "r")

for seq in data:
    pass
strand = len(seq)-1 #this was used to define the length of my sequence.
seqUpper = seq.upper()

for match in re.finditer(r"A.TAAT", seqUpper):
    splice.append(match.start() + 3)
    pass

for match in re.finditer(r"GC(A|G)(A|T)TG", seqUpper): #I used the pass command for my loops because it made it less cumbersome to work with the results.  
    splice.append(match.start() + 4)
    pass

lis = sorted(splice+[strand]) #This is what gave me trouble before. I wasn't passing 'strand' as a list with brackets. Adding the brackets fixed everything. 
print lis 
print message +' '+str(lis[1]-lis[0])+'.'
print message +' '+str(lis[2]-lis[1])+'.'
print message +' '+str(lis[3]-lis[2])+'.'
print message +' '+str(lis[4]-lis[3])+'.'
print message +' '+str(strand-lis[4])+'.'






        
    

