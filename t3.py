from datetime import *

def getTimeSection(clocks) :
    result = ''
    if clocks > 20:
        decades = int(clocks / 10) * 10
        units = clocks - decades
        result = '{0} {1}'.format(a[decades], a[units])
    else:
        result = a[clocks]
    return result

today = datetime.today()
a = {
    0 : 'zero ' ,
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'fourteen',
    50 : 'fiftee',
}       
hour = today.hour
minute = today.minute

print( ' Time: ' , today.hour , ':' , today.minute , )
print("Time: {0} {1} o'clock".format(getTimeSection(hour),getTimeSection(minute)))
print("------------------------------------------------------------\n")
inTime = input()


b = inTime.split(":")
print("Time: {0} {1} o'clock".format(getTimeSection(int(b[0])),getTimeSection(int(b[1]))))
    