#file = open('test.txt', 'r')
length = int(input())
if length > 15:
    file1 = open('/home/roman_v/mylab/text.txt', 'r')
    resultFile = open('/home/roman_v/new_text.txt', 'w')
    for line in file1:
        words = line.split()
        lenSum = 0
        resultLine = ''

        for word in words:
            lenWord = len(word)

            if lenSum + lenWord < length:
                resultLine += " " + word 
                lenSum += lenWord + 1
            else :
                strFormat = '{:^' + str(length) + '}' 
                resultFile.write(strFormat.format(resultLine)+'\n')
                resultLine = word
                lenSum = lenWord
