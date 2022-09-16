import datetime
nr = input('Skriv ditt personnummer som ååmmddnnnn: ')
dt = datetime.datetime.now()
s = str(dt.date())
if nr[2:4] == s[5:7] and nr[4:6] == s[8:]:
    print('Grattis!')
