list = ['five','thirteen','eleven','seventeen', 'two', 'one', 'thirteen', 'ten', 'four', 'eight', 'five', 'nineteen']
result = []
for i in list:
    if i not in result:
        result.append(i)
print('deleted duplicates:'+ str(result))


dict = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19, 'twenty':20, 'twentyone':21}
numresult=[]  
for k,v in dict.items():
    if result.count (k):
        numresult.append (v)
numresult.sort()
print('text transformed in numbers:'+ str(numresult))


s=0
for g in numresult:
    if g % 2 != 0:
        s += g
print('total sum of all odd numbers:'+ str(s))


numresult1=numresult[1::2]
numresult2=numresult[::2]
t=[]
for x,y in zip (numresult1,numresult2):
    t=(x*y)
    print('mult-in-pair:'+ str(t))


numresult3=numresult[1:]
numresult4=numresult3[::2]
numresult5=numresult3[1::2]
w=[]
for c1,c2 in zip (numresult4, numresult5):
    w=(c1+c2)
    print('sum-in-pair:'+str(w))