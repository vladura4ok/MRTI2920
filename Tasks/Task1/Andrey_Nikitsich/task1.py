depozit = int(input('Input your depozit: '))
percentPerYear = 0.15
timeInMonth = 5*12

#first varient with loop
i = 0
endDepozit = depozit
while i<timeInMonth:
    endDepozit+=endDepozit*percentPerYear/12
    i+=1
endDepozit = round(endDepozit, 2)
print('Your depozit after ' + str(timeInMonth) + ' months' + '[first varient] : ' + str(endDepozit))


#second varient without loop
endDepozit2 = depozit*((1+percentPerYear/12)**timeInMonth)
endDepozit2 = round(endDepozit2, 2)
print('Your depozit after ' + str(timeInMonth) + ' months' + '[second varient] : ' + str(endDepozit2))