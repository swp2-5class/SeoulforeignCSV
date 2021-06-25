import os,re,csv

newPop=[]

f=open('popSeoul.csv','r')
reader=csv.reader(f)
for i in reader:
    newPop.append(i)

#print(newPop)

for i in newPop:
    for j in i:
        try:
            i[i.index(j)]=float(j)
        except:
            pass

f.close()

i=newPop[1]

foreign=round(i[2]/(i[1]+i[2])*100,1)

#print(foreign)


for a in newPop[1:]:
    foreign=0
    foreign=round(a[2]/(a[1]+a[2])*100,1)
    #print(a[0],foreign)

new=[['구','한국인','외국인','외국인 비율(%)']]

new.append([i[0],i[1],i[2],foreign])

#print(new)

for i in newPop[1:]:
    foreign=0
    foreign=round(i[2]/(i[1]+i[2])*100,1)
    if foreign>3:
        new.append([i[0],i[1],i[2],foreign])
    else:g
        pass

f=open('popSeoul.csv','w',newline='')
writer=csv.writer(f,delimiter=',')
writer.writerows(new)

f.close()
"연습용 출력 끝"
"test1"