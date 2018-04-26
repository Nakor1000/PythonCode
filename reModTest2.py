import re
sid = raw_input("Enter Student A#:")
sidUpper = sid.upper()

if(re.search(r"^A[0123456789]{8}", sidUpper)):
    print "This is a valid MCLA id!"
else:
    print "This is not a valid MCLA id!"


phone = raw_input("Enter phone number [###-###-####]:")

if(re.search(r"[0123456789]{3}-[0123456789]{3}-[0123456789]{4}", phone)):
    print "This is a valid phone number!"
else:
    print "This is a not a valid phone number!"
    
