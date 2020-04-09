import os
import pandas as pd
filepath="C:/Users/ajink/Duties_made_easy"
print("The file path is : ")
os.chdir(filepath)
file=pd.read_excel("DataFile.xlsx",sheet_name="Sheet1",na_values=" ")
#print(file)


#######################    Accissing the Required Data    ########################


def deleterow(i):
    for j in range(i):
        teacherfile.drop(teacherfile.index[j], inplace=True)
        


teacherfile=pd.read_excel("DataFile.xlsx",sheet_name="old Jr. Sup. order Nov. 2019", na_values=" ")
#deleterow(3)
to_delete=[0,1,2]
teacherfile.drop(teacherfile.index[to_delete], inplace=True)

colname=teacherfile.loc[3,:]
colname[7]="Favorable Dates"
teacherfile.columns=colname
teacherfile=teacherfile.drop('Jr. Sup. Sign', axis=1)
teacherfile=teacherfile.drop(index=3,axis=0)
teacherfile=teacherfile.set_index("Sr. No.",drop=False)


reqfile=teacherfile.loc[1.0:116.0,["Name of the faculty","Total duties","Favorable Dates"]]
#print(reqfile)

##############          Getting the Exam Dates

date=file.loc[:,['Day/Date','Year','Time','Total Jr. Sup. Req.']]
weekdays=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
for i in range(len(weekdays)):
    weekdays[i]=weekdays[i].title()    
#print(weekdays)
datesofexam=[]
dateswithshift=[]
examdate=[]
dayduty=[]
for i in range(len(date['Day/Date'])):
    j=date.loc[i][0]
    if str(j) == 'nan':
        continue
    else:
        k=j
        j=j.split(" ")[0].title()
        if j in weekdays:
            shift=int(date.iloc[i][2][0])
            if shift == 1:    
                l=k.split(" ")[1].strip() + 'm'
            elif shift == 2:
                l=k.split(" ")[1].strip() + 'e'
            dat=k.split(" ")[1].strip()
            dayduty.append((l,date.iloc[i][3]))
            dateswithshift.append(l)
            datesofexam.append(dat)
            con=date.iloc[i][0]+date.iloc[i][2]
            examdate.append(con)
        else:
            continue


#############################        Processing of Data        


class Teacher():
    def __init__(self,name ,noOfDuties):
        self.name = name
        self.noOfDuties = noOfDuties
        self.alloteddate=['12/12/2020']
    def putdata(self):
        print("Teacher Name : ",self.name, "\nTeacher Dutfavdt.iloc[cou][16]favdt.iloc[cou][16]ies : ",self.noOfDuties)


supreq=[]
for i in range(0,len(date['Total Jr. Sup. Req.']),1):
    if type(date['Total Jr. Sup. Req.'][i]) is int:
        supreq.append(date['Total Jr. Sup. Req.'][i])
        
        
thr=[]
for z in range(1,len(reqfile['Name of the faculty'])+1):
    thr.append(Teacher(reqfile.loc[z][0], reqfile.loc[z][1]))


toblocks=[]
maxi=max(supreq)
for jrsup in range(1,max(supreq)+1,1):
    toblocks.append(jrsup)


day=[]
for x in range(0,len(dateswithshift),1):
   day.append([dateswithshift[x],[]])

forteacher=[]
sorteddates=[]
teacherlist=[]
teacherwithduties=[]
reqfile["Favorable Dates"].fillna("0",inplace=True)
for u in range(1,len(reqfile['Name of the faculty'])+1,1):
    if reqfile["Favorable Dates"][u] != str(0):
        forteacher.append([reqfile['Name of the faculty'][u],[]])
        sorteddates.append([reqfile['Name of the faculty'][u],[]])
        teacherlist.append(reqfile['Name of the faculty'][u].strip('.'))
        teacherwithduties.append((reqfile['Name of the faculty'][u], reqfile["Total duties"][u], reqfile["Favorable Dates"][u]))
    
    


#=================================    Let's assign the dates


    mylist=list(dict.fromkeys(datesofexam))
datesofexam=mylist


fav=[]
favdt=pd.read_excel("DataFile.xlsx",sheet_name="Sheet3", na_values=" ")
favdt['Favorable Dates'].fillna(0,inplace=True)
for i in range(0,len(favdt),1):
    if favdt['Favorable Dates'][i] != 0:
        date=favdt['Favorable Dates'][i].split("/")
        dayi=date[2]
        month=date[1]
        year=date[0]
        date=dayi+"/"+month+"/"+year
        nam=favdt['Unnamed: 1'][i]
        if nam in teacherlist:
            place=teacherlist.index(nam)
            dutiesreq=teacherwithduties[place][1]
        fav.append((favdt['Unnamed: 1'][i],date,dutiesreq))
    else:
        continue



def teach(ch):
    if ch in teacherlist:
        for ijk in range(len(fav)):
            if str(fav[ijk][0]) == str(ch):
                return [fav[ijk][0], str(fav[ijk][1]), fav[ijk][2]]
    else:
        return 0


"""
def givestart(pos,p):           #pos = position of favdt in list and p = half of dutiesreq to teacher
    lb=0                        #lb = lower bound of index of datesofexam
    ub=len(datesofexam)-1       #ub = upper bound 
    if (pos >= p) and (ub-pos)>=p:
        return pos-p
    elif pos+1 <= p:
        return lb
    else:
        return ub
"""    

def check(mylist,date,name,dutyreq):
    dutyalloted=0
    if (date in dateswithshift):
        index=dateswithshift.index(date)
        count=len(day[index][1])
        if name in teacherlist:
            pos=teacherlist.index(name)
            dutyalloted=len(forteacher[pos][1])
            
#        print("/nline 163: count=",count,"index = ",index)
        
        if count < dayduty[index][1] and count>=0 :
            if dutyalloted<dutyreq:
                day[index][1].append(name)
                if name in teacherlist:
                    forteacher[teacherlist.index(name)][1].append(day[index][0])
                    sorteddates[teacherlist.index(name)][1].append(day[index][0])
        else:
            return 0
              
        
    

def checkavl(date1,date2):
    if (date1 in dateswithshift):
        index=dateswithshift.index(date1)
        counti=len(day[index][1])
        if counti < dayduty[index][1]:
            return date1
    if (date2 in dateswithshift):
        index=dateswithshift.index(date2)
        counti=len(day[index][1])
        if counti < dayduty[index][1]:
            return date2
    else:
        return -1





def allote(teacher):
    if teacher == None:
        return 0

    name=teacher[0]
    fvdt=teacher[1]
    dutiesreq=teacher[2]
    pos=datesofexam.index(fvdt)
    i=j=pos
    date1=fvdt+'m'
    date2=fvdt+'e'
    getdate=checkavl(date1, date2)
    if getdate != -1:
        check(dateswithshift, getdate,name,dutiesreq)
    #print("\n pos = ",pos)
    chk=0
    while chk <= dutiesreq:
        i=i-1
        j=j+1
        if i <0 and j > len(datesofexam):
            break
        if i >= 0:
            if name in teacherlist:
                chk=len(forteacher[teacherlist.index(name)][1])
#             print("\n\tchk = ",chk,"dutiesreq = ",dutiesreq)
            if chk > dutiesreq:
                break
            fvdt=datesofexam[i]
            date1=fvdt+'m' 
            date2=fvdt+'e'
            getdate=checkavl(date1,date2)
            if getdate != -1:
                check(dateswithshift, getdate,name,dutiesreq)
        if j< len(datesofexam):
            if name in teacherlist:
                chk=len(forteacher[teacherlist.index(name)][1])
  #              print("\n\tchk = ",chk,"dutiesreq = ",dutiesreq)
            if chk > dutiesreq:
                break
 #           print("\n\tj= ",j)
            fvdt=datesofexam[j]
            date1=fvdt+'m'
            date2=fvdt+'e'
            getdate=checkavl(date1,date2)
            if getdate != -1:
                check(dateswithshift, getdate,name,dutiesreq)
        

#===================== The allocation of teachers starts from here
import random
allotedteacher=[]
i=0
"""

choiceteach=random.choice(teacherlist)
li=teach(choiceteach)
allote(li)
allotedteacher.append(choiceteach)

"""
ak=0
lengthlt=[]
for shady in range(len(dateswithshift)):
    ak=ak+dayduty[shady][1]
        
terminate=0
while terminate < ak:
    terminate=0
    gin=0
    for gabbi in range(len(dateswithshift)) :
        gin=len(day[gabbi][1])
        terminate=terminate+gin
        
        
        
#    print("Terminat", terminate)  
    choiceteach=random.choice(teacherlist)
    li=teach(choiceteach)
    if choiceteach in allotedteacher:
        continue
    elif li == 0:
#       print("Got a successful Result")
        allotedteacher.append(choiceteach)
        teacherlist.remove(choiceteach)
        i=i+1
    else:
        allote(li)
        """
        if li[0] in teacherlist:
            p=teacherlist.index(li[0])
            reqdut=teacherwithduties[p][1]
            forteacher[p][1]"""
        allotedteacher.append(choiceteach)
        i=i+1

#================================Getting equal duties for teachers
   
minimum=0
def extraallote(teacher='xyz'):
    lengthlt.clear()

#   print("line 302 :  I am in while loop")
    for i in range(len(teacherlist)):
            length=len(forteacher[i][1])
            lengthlt.append(length)

    highest=max(lengthlt)
    minimum=min(lengthlt)
    if highest == minimum:
        return 0
#    print("minimum = ",minimum)
    if highest in lengthlt:
        position=lengthlt.index(highest)
        date=forteacher[position][1][highest-1]
#        print("for maximum : position = ", position,
#             "highest - 1 = " ,highest-1,"and date = ",date)
        forteacher[position][1].remove(date)
        sorteddates[position][1].remove(date)
        if teacher !='xyz':
            position=teacherlist.index(teacher)
            forteacher[position][1].append(date)
            sorteddates[position][1].append(date)
        else:
            position=lengthlt.index(minimum)
            forteacher[position][1].append(date)
            sorteddates[position][1].append(date)
            return minimum

     


#print("line 302 :  I am in while loop")
x=0
while x == 0:
    x = extraallote()
        

"""Teachers greater than 6 duties """

rearr=[]
underalloted={}
underduty={}
"""
for i in range(len(teacherlist)):
    if len(forteacher[i][1]) == fav[i][2]:
        if fav[i][2] >6:
            rearr.append((fav[i][0],fav[i][1],fav[i][2]))
    elif (len(forteacher[i][1]) < fav[i][2]) and (fav[i][2] < 6):
        if len(forteacher[i][1]) <6:
            diff=fav[i][2]-len(forteacher[i][1])
            underalloted.update({fav[i][0] : [fav[i][1],fav[i][2],diff]})
    elif len(forteacher[i][1]) < fav[i][2]:
        if len(forteacher[i][1]) <6:
            diff=fav[i][2]-len(forteacher[i][1])
            underduty.update({fav[i][0] : [fav[i][1],fav[i][2],diff]})

"""














maximum=max(lengthlt)
count=0
for i in underalloted:
    count=count+underalloted[i][2]


for i in underalloted:
    for j in range(underalloted[i][2]):
        extraallote(i)
        count=count-1


for i in underduty:
    count=underduty[i][1]
    pre=underduty[i][1] - underduty[i][2]
    count=int((count/2) + 1)
    count=count-pre
    for j in range(count):
        extraallote(i)


#================================ Arranging the Dates alloted in ascending order


def sortkar(data):
    sortedlist=[]
    year=year1=[]
    month=[]
    day=[]
    yearws=[]
    new=[]
    yrmonthday=[]
    p=-1
    for k in range(len(data)):
        i=data[k].split('/')
        j=i[2][:len(i[2])-1]
        o=i[2][:len(i[2])]
        l=i[1]
        m=i[0]
        sep1=[]
        year.append(int(j))
        month.append(int(l))
        day.append(int(m))
        yearws.append(str(o))
        
#    print(i,' ',day,' ',month,' ',year) 
    year1=year.copy()
    month1=month.copy()
    day1=day.copy()
    while len(year) != 0:
        counts=year.count(min(year))
        yrmonthday.append([min(year),[]])
        p=p+1
        while counts !=0:
            minimm=min(year)
            index=year.index(minimm)
            sep1.append((year[index],month[index],day[index]))
            yrmonthday[p][1].append(month[index])
            day.remove(day[index])
            month.remove(month[index])
            year.remove(year[index])
            counts=counts-1
    for i in range(p+1):
        yrmonthday[i][1]=list(set(yrmonthday[i][1]))
    
    for i in range(len(yrmonthday)):
        for j in range(len(yrmonthday[i][1])):
            element=yrmonthday[i][1][j]
            yrmonthday[i][1][j]=[element,[]]



    for i in range(len(year1)):
        for j in range(len(yrmonthday)):
            if yrmonthday[j][0]==year1[i] :
                for k in range(len(yrmonthday[j][1])):
 #                   print("Very long : ",yrmonthday[j][1][k],month1)
                    if yrmonthday[j][1][k][0] == month1[i]:
                       yrmonthday[j][1][k][1].append(day1[i])
                       
                       
                       
                       
                       
    for i in range(len(yrmonthday)):
        for j in range(len(yrmonthday[i][1])):
            yrmonthday[i][1][j][1].sort()
            
            
#    print("\nline 459 : ",yrmonthday)
    sortedlist.clear()
    for i in range(len(yrmonthday)):
        for j in range(len(yrmonthday[i][1])):
            for k in range(len(yrmonthday[i][1][j][1])):
 #               print("\nline 465 : i = ",i,"\tj = ",j,"\tk = ",k)
#                [[2019, [[12, [5, 7, 9, 23, 26, 28, 31]]]], [2020, [[1, [2]]]]]
                a=str(yrmonthday[i][1][j][1][k]) + "/" + str(yrmonthday[i][1][j][0]) + "/" + str(yrmonthday[i][0])
                sortedlist.append(a)

    return sortedlist
#    print("sep 1 = ",sep1,"\nyrmonthday = ",yrmonthday,"\nyear1 = ",year1,"\nyear = ",year)



""" if counts == len(year):
            mmonth=min(month)
            monthcounts=month.count(mmonth)
            if monthcounts == len(month):
                while len(day) != 0:
                    mday=min(day)
                    dayin=day.index(mday)
                    sortedlist.append(str(day[dayin]) +"/"+ str(month[dayin]) +"/"+ str(yearws[dayin]))
                    day.remove(day[dayin])
                    month.remove(month[dayin])
                    year.remove(year[dayin])
                    
#        p=year.index(maximm)
#       sortedlist.append(str(day[p]) +"/"+ str(month[p]) +"/"+ str(year[p]))
    
        

    return(sortedlist)

"""



newlist=[]
for i in range(len(forteacher)):
    newlist.clear()
    sorteddates[i][1] = sortkar(forteacher[i][1])
    for j in range(len(forteacher[i][1])):
        word = len(forteacher[i][1][j]) - int(1)
        newlist.append((forteacher[i][1][j][0:len(forteacher[i][1][j])-1]))
        
    
    






    
    
    





#===============================Making the file suitable for DataFrame


for i in range(len(day)):
    while len(day[i][1]) < maxi:
        day[i][1].append(" ")
    
    
df=pd.DataFrame(dict(day))
df=df.T
df.columns=[n+1 for n in range(39)]
df1=pd.DataFrame(forteacher)
path="C:/Users/ajink/Duties_made_easy/OUTPUT/output.xlsx"
writer = pd.ExcelWriter(path, engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet_name_1')
df1.to_excel(writer, sheet_name='Sheet_name_2')
writer.save()







