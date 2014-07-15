#!/usr/bin/python2
import os
from datetime import datetime, timedelta, date
from random import randrange

x=0
while x<10000:
    with open('x.txt', 'w') as f:
        f.write(str(x))
    os.system('git add .')
    pastdays = randrange(1, 2555)
    datendaysago = datetime.utcnow() - timedelta(days = pastdays)
    print datendaysago.strftime("%c -0400")
    os.system("GIT_AUTHOR_DATE='%s' GIT_COMMITTER_DATE='%s' git commit -m 'new (old) files'" % (datendaysago, datendaysago))
    x=x+1

