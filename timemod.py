
def countdown(seconds):
    import time
    count = range((int(seconds)+1), 0, -1)
    for t in count:
            if t == 1:
                    pass
                    
            else:
                    print('{0}'.format(t-1))
            time.sleep(1)
    while t >= 1:
        alarm = str("TIME'S UP!!           ")
        print alarm ,
        time.sleep(.009)



def checktime(t):
    import time
    ticks = time.time()
    localtime = time.strftime("%a, %d %b %Y %I:%M %z ", time.localtime())
    print localtime
    


