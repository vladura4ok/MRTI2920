import datetime
a = datetime.datetime.now()

b = input("введите время в формате ЧЧ:ММ ").split(":")
hours_dictionary = {"00" : "Полночь", "01" : "Час", "02" : "Два", "03" : "Три", "04" : "Четыре", "05" : "Пять", 
"06" : "Шесть", "07" : "Семь", "08" : "Восемь", "09" : "Девять", "10" : "Десять", "11" : "Одинадцать", 
"12" : "Полдень", "13" : "Час", "14" : "Четырнадцать", "15" : "Пятнадцать", "16" : "Шестнадцать", 
"17" : "Семнадцать", "18" : "Восемнадцать", "19" : "Девятнадцать", "20" : "Двадцать", "21" : "Двадцать один" , 
"22" : "Двадцать два", "23" : "Двадцать три", "1" : "Час", "2" : "Два", "3" : "Три", "4" : "Четыре", "5" : "Пять", 
"6" : "Шесть", "7" : "Семь", "8" : "Восемь", "9" : "Девять", "24" : "Полночь"}
minuts_dictionary = {"00" : "ровно", "01" : "одна", "02" : "две", "03" : "три", "04" : "четыре", "05" : "пять", 
"06" : "Шесть", "07" : "Семь", "08" : "Восемь", "09" : "Девять", "10" : "Десять", "11" : "Одинадцать", 
"12" : "Двенадцать", "13" : "Тринадцать", "14" : "Четырнадцать", "15" : "Пятнадцать", "16" : "Шестнадцать", 
"17" : "Семнадцать", "18" : "Восемнадцать", "19" : "Девятнадцать", "20" : "Двадцать", "21" : "Двадцать одна" , 
"22" : "Двадцать две", "23" : "Двадцать три", "24" : "Двадцать четыре", "25" : "Двадцать пять", "26" : "Двадцать шесть", 
"27" : "Двадцать семь", "28" : "Двадцать восемь" , "29" : "Двадцать девять", "30" : "Тридцать", "31" : "двадцати девяти", 
"32" : "двадцати восьми", "33" : "двадцати семи", "34" : "двадцати шести", "35": "двадцати пяти", "36" : "двадцати четырех", 
"37" : "двадцати трех", "38" : "двадцати двух", "39" : "двадцати одной", "40" : "двадцати", "41" : "девятнадцати", 
"42" : "восемнадцати", "43" : "семнадцати", "44" : "шестнадцати", "45" : "пятнадцати", "46" : "четырнадцати", "47" : "тринадцати", 
"48" : "двенадцати", "49" : "одинадцати", "50" : "десяти", "51" : "девяти", "52" : "восьми", "53" : "семи", "54" : "шести", 
"55" : "пяти", "56" : "четырех", "57" : "трех", "58" : "двух", "59" : "одной", "1" : "одна", "2" : "две", "3" : "три", 
"4" : "четыре", "5" : "пять", "6" : "Шесть", "7" : "Семь", "8" : "Восемь", "9" : "Девять"}

print("время введенное с клавиатуры:")

if int(b[0]) > 23 or int(b[1]) > 59:
    print("Такого времени не бывает")

if int(b[1]) < 31:

    if b[1] == "00":
        if b[0] in ('00', '12'):
            print("ровно " + hours_dictionary[(b[0])]) 
        elif b[0] == "01":
            print(hours_dictionary[(b[0])] + " ровно")
        elif b[0] in ("02", "03", "04"):
            print(hours_dictionary[(b[0])] + " часа " + "ровно")
        else:
            print(hours_dictionary[(b[0])] + " часов ровно")

    elif b[1] in ('01', '21'):
        if b[0] == "01":
            print(hours_dictionary[(b[0])] + " и " + minuts_dictionary[(b[1])] + " минута")
        elif b[0] in ("02", "03", "04"):
            print(hours_dictionary[(b[0])] + " часа " + minuts_dictionary[(b[1])] + " минута")
        else:
            print(hours_dictionary[(b[0])] + " часов " + minuts_dictionary[(b[1])] + " минута")

    elif b[1] in ("02", "03", "04", "22", "23", "24"):
        if b[0] == "01":
            print(hours_dictionary[(b[0])] + " и " + minuts_dictionary[(b[1])] + " минуты")
        elif b[0] in ("02", "03", "04"):
            print(hours_dictionary[(b[0])] + " часа " + minuts_dictionary[(b[1])] + " минуты")
        else:
            print(hours_dictionary[(b[0])] + " часов " + minuts_dictionary[(b[1])] + " минуты")

    else:
        if b[0] == "01":
            print(hours_dictionary[(b[0])] + " и " + minuts_dictionary[(b[1])] + " минуты")
        elif b[0] in ("02", "03", "04"):
            print(hours_dictionary[(b[0])] + " часа " + minuts_dictionary[(b[1])] + " минуты")
        else:
            print(hours_dictionary[(b[0])] + " часов " + minuts_dictionary[(b[1])] + " минуты")

else: 

    if b[1] in ('39', '59'):
        if b[0] == "00":
            print("Без " + minuts_dictionary[(b[1])] + " минуты " + hours_dictionary[(str(int(b[0])+1))])
        elif b[0] in ("01", "02", "03"):
            print("Без " + minuts_dictionary[(b[1])] + " минуты " + hours_dictionary[(str(int(b[0])+1))] + " часа") 
        else:
            print("Без " + minuts_dictionary[(b[1])] + " минуты " + hours_dictionary[(str(int(b[0])+1))] + " часов")

    else:
        if b[0] == "00":
            print("Без " + minuts_dictionary[(b[1])] + " минут " + hours_dictionary[(str(int(b[0])+1))])
        elif b[0] in ("01", "02", "03"):
            print("Без " + minuts_dictionary[(b[1])] + " минут " + hours_dictionary[(str(int(b[0])+1))] + " часа") 
        else:
            print("Без " + minuts_dictionary[(b[1])] + " минут " + hours_dictionary[(str(int(b[0])+1))] + " часов")

print()
print()
print("текущее время установленное на компьютере:")



if int(a.minute) < 31:

    if str(a.minute) in ('00', '0'):
        if str(a.hour) in ('00', '0', '12'):
            print("ровно " + hours_dictionary[str(a.hour)]) 
        elif str(a.hour) in ('01', '1'):
            print(hours_dictionary[str(a.hour)] + " ровно")
        elif str(a.hour) in ("02", "03", "04", "2", "3", "4"):
            print(hours_dictionary[str(a.hour)] + " часа " + "ровно")
        else:
            print(hours_dictionary[str(a.hour)] + " часов ровно")

    elif a.minute in ('01', '21', '1'):
        if str(a.hour) in ('01', '1'):
            print(hours_dictionary[str(a.hour)] + " и " + minuts_dictionary[str(a.minute)] + " минута")
        elif b[0] in ("02", "03", "04", "2", "3", "4"):
            print(hours_dictionary[str(a.hour)] + " часа " + minuts_dictionary[str(a.minute)] + " минута")
        else:
            print(hours_dictionary[str(a.hour)] + " часов " + minuts_dictionary[str(a.minute)] + " минута")

    elif str(a.minute) in ("02", "03", "04", "22", "23", "24"):
        if b[0] in ('01', '1'):
            print(hours_dictionary[str(a.hour)] + " и " + minuts_dictionary[str(a.minute)] + " минуты")
        elif b[0] in ("02", "03", "04", "2", "3", "4"):
            print(hours_dictionary[str(a.hour)] + " часа " + minuts_dictionary[str(a.minute)] + " минуты")
        else:
            print(hours_dictionary[str(a.hour)] + " часов " + minuts_dictionary[str(a.minute)] + " минуты")

    else:
        if str(a.hour) in ('01', '1'):
            print(hours_dictionary[str(a.hour)] + " и " + minuts_dictionary[str(a.minute)] + " минуты")
        elif b[0] in ("02", "03", "04", "2", "3", "4"):
            print(hours_dictionary[str(a.hour)] + " часа " + minuts_dictionary[str(a.minute)] + " минуты")
        else:
            print(hours_dictionary[str(a.hour)] + " часов " + minuts_dictionary[str(a.minute)] + " минуты")

else: 

    if str(a.minute) in ('39', '59'):
        if str(a.hour) in ('00', '0'):
            print("Без " + minuts_dictionary[str(a.minute)] + " минуты " + hours_dictionary[(str(int(a.hour)+1))])
        elif str(a.hour) in ("02", "03", "04", "2", "3", "4"):
            print("Без " + minuts_dictionary[str(a.minute)] + " минуты " + hours_dictionary[(str(int(a.hour)+1))] + " часа") 
        else:
            print("Без " + minuts_dictionary[str(a.minute)] + " минуты " + hours_dictionary[(str(int(a.hour)+1))] + " часов")

    else:
        if str(a.hour) in ('00', '0'):
            print("Без " + minuts_dictionary[str(a.minute)] + " минут " + hours_dictionary[(str(int(a.hour)+1))])
        elif str(a.hour) in ("02", "03", "04", "2", "3", "4"):
            print("Без " + minuts_dictionary[str(a.minute)] + " минут " + hours_dictionary[(str(int(a.hour)+1))] + " часа") 
        else:
            print("Без " + minuts_dictionary[str(a.minute)] + " минут " + hours_dictionary[(str(int(a.hour)+1))] + " часов")
