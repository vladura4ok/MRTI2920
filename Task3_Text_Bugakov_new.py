with open(r"C:\\Users\\User\\Desktop\\111\\text.txt", encoding="utf8") as file:
   text = file.read().split()
textlen = int(input("Enter a number of symbols in a string (min 15): "))
def func(textlen,file):
    totallen=0
    list=[]
    with open (r"C:\\Users\\User\\Desktop\\111\\text1.txt", 'w', encoding="utf8")as wfile:
        for i in range(0, (len(text))):
            if len(text[i])==textlen:
                    wfile.write(' '.join(text[i]))
            elif len(text[i])<textlen: 
                if (totallen+(len(text[i])+1))<textlen:
                    totallen= totallen+len(text[i])+1
                    list.append(text[i])
                elif (totallen+(len(text[i])+1))==textlen:
                    list.append(text[i])
                    wfile.write(' '.join(list)+"\n")
                    totallen=0
                    list.clear()
                elif (totallen+(len(text[i])+1))>textlen:
                    rest=text[i]
                    def func2(list,textlen,totallen):
                            newlist=[]
                            x=textlen-totallen
                            k=x//len(list)
                            for i in range(0, len(list)): 
                                if k==0:
                                    if x>0:
                                        newlist.append(list[i]+('  '))
                                        x = x - 1
                                    else:
                                        newlist.append(list[i]+(' '))
                                else:
                                    newlist.append(list[i]+(k*' '))
                            else:
                                return ''.join(newlist)
                    wfile.write(func2(list,textlen,totallen)+"\n")
                    totallen=0
                    list.clear()
                    totallen=(len(text[i])+1)
                    list.append(rest)
        wfile.write(' '.join(list)+"\n")
with open (r"C:\\Users\\User\\Desktop\\111\\text1.txt") as qfile:                    
    func(textlen,file)



