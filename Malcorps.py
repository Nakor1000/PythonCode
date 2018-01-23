#Practice program coded by Anthony Young
#For python class 1/21/18
print "How many malcorps did you find on Exflon?",
Exflon = raw_input()
print "How many malcorps did you find on Mobiles?",
Mobiles = raw_input()
print "How many malcorps did you find on Monsantoes?",
Monsantoes = raw_input()
#Don't forget to int wrap strings that you want to add
total = (int(Exflon) + int(Mobiles) + int(Monsantoes))
print "You found %s malcorps!" % total
#use .2f to specify the number of decimals for floating point 
print "The average number of malcorps per planet is %.2f." % (total/3.0)
