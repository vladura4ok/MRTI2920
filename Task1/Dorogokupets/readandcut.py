with open('lorem.txt', 'r') as f:#открываем файл с текстом
    txt = f.read()#содержимое файла загоняем в переменную txt
#ввод количества символов в одной строке, сохраняем в переменную 
spliter = int(input("enter what the number of characters in one string you wish as an integer from 15 to 150: "))

text_length = len(txt)#определяем длину текста чтобы проверить больше ли она числа введенных символов

if int(spliter) <= int(text_length):
    spliter = spliter
else:
    spliter = int(input("a number that is too large, enter a number less than the previous one"))

mylist = txt.split()#делим текст на слова и загоняем в список mylist

def new_text(text_list, string_length):#объявляем функцию с параметрами список слов и длина строки
    string = ''#новая строка пока пуста
    for i in range(0, len(text_list)):#цикл для каждого слова из списка слов
        if len(string) <= string_length:#пока длина нашей строки меньше или равна нужной длине строки
            #условие которое работает только на самое первое слово
            if len(string) == 0:#если длина строки равна нулю и мы записываем первое слово, перед ним не нужен пробел
                string = string + text_list[i]#мы добавляем к пустой строке первое слово
            elif len(string) > 0:#если в строке уже есть слово, то следующее слово прибавляем через пробел
                string1 = string + ' ' + text_list[i]#вариант 1 - мы добавляем пробел и слово к старой строке
                string2 = string#вариант 2 - мы оставляем строку прежней
                #условие которое работает если длина строки меньше требуемой, в итоге строка равна старой строке плюс слово
                if len(string1) <= string_length:#если в итоге новая строка короче 
                    string = string1#строка равна старая строка плюс слово
                else:#иначе, если строка длиннее нужной нам длины и нам нужно прекращать ее дополнение словами
                    string = string2#строка по факту не меняется, она равна строке без нового слова
                    spaces = string.count(' ')#находим сколько пробелов в исходной строке
                    delta = string_length - len(string)#находим разницу между требуемой длиной и исходной строкой
                    k1 = (delta + spaces) // spaces#находим коэффициент на сколько раз нужно увеличивать пробелы
                    k2 = delta % spaces#находим добавочный коэффициент добавления отдельных пробелов
                    x = ' ' * k1#получаем нужное нам количество пробелов
                    string = string.replace(' ', x, spaces)#добавляем пробелы в замену каждому имеющемуся пробелу
                    string = string.replace(x, (x + ' '), k2)#добавляем отдельные пробелы которых не хватает
                    #записываем данные в файл:
                    with open('lorem_new.txt', 'a') as newfile:
                        newfile.write(string + '\n')
                        string = text_list[i]#после записи строка становится равна тому слову, которое отбросили от записанной строки, и идет на новый цикл
                        #условие если у нас самое последнее слово списка
                        if i == (len(text_list) - 1):
                            #записываем это слово в файл
                            with open('lorem_new.txt', 'a') as newfile:
                                newfile.write(string)

new_text(mylist, spliter)
