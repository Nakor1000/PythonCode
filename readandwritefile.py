f = open('sequence.txt')
data = f.read().rstrip('\n')
lowerSeq = data.lower()
seqLen = len(data)

f2 = open('output.txt', 'w')
f2.write('Original Sequence:' + data + '\n')
f2.write('Lowercase Sequence:' + lowerSeq + '\n')
f2.write('Length of Sequence:' + str(seqLen) + '\n')

f2.close()