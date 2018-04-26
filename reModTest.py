import re

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

def check(lis, target):
    for result in lis:
        if re.search(target, result):
            print result

print "accession name contains the number 5:" 
check(accessions, r"5")
print "Accession names containing d or e:"
check(accessions, r"d|e")
print "Accession names containing de:"
check(accessions, r"(de)+")
print "Accession names containing d followed by any character followed by e:"
check(accessions, r"d.e")
print "Acession names containing de or ed:"
check(accessions, r"(de|ed)")
print "Acession names starting with x or y:"
check(accessions, r"^(x|y)")
print "Acession names starting with x or y and ending with e:"
check(accessions, r"^(x|y).*e$")
print "Accession names containing 3 or more digits:"
check(accessions, r".*[0123456789]{3,}.*")
print "Accession names ending with d followed by a, r or p:"
check(accessions, r"d[arp]$")
