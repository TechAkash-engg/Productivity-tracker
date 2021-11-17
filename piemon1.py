import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import datetime as dt
from fpdf import FPDF
from PyPDF2 import PdfFileMerger

average=[]
performers=[]
performers1=[]
for i in range(51): 
    if i==0:
        name='Akashraj Bhat'
    elif i==1:
        name='Aman Kumar Srivastav'
    elif i==2:
        name='Anarghya S R'
    elif i==3:
        name='Anush Laila'
    elif i==4:
        name='Avish Shetty'
    elif i==5:
        name='Deekshith Prabhu'
    elif i==6:
        name='Dhanraj'
    elif i==7:
        name='Meghana'
    elif i==8:
        name='Mokshith S Pergade'
    elif i==9:
        name='Namya Shetty'
    elif i==10:
        name='Neha U'
    elif i==11:
        name='Nidish Rao'
    elif i==12:
        name='Poornima'
    elif i==13:
        name='Pranathi Acharya'
    elif i==14:
        name='Prasidda Hegde'
    elif i==15:
        name='Prathik Nayak'
    elif i==16:
        name='Prathiksha'
    elif i==17:
        name='Praveen nayak'
    elif i==18:
        name='Preetham G S'
    elif i==19:
        name='Rishabh Gujarati'
    elif i==20:
        name='S R Udith'
    elif i==21:
        name='Sharath Hulekal'
    elif i==22:
        name='Shashank H S'
    elif i==23:
        name='Shreya R'
    elif i==24:
        name='Shreyas S'
    elif i==25:
        name='Shrinivas Anand Kamath'
    elif i==26:
        name='Vadiraj'
    elif i==27:
        name='Vanshika Shenoy'
    elif i==28:
        name='Varsha G D'
    elif i==29:
        name='Vikas'
    elif i==30:
        name='Vineeth D Shetty'
    elif i==31:
        name='Vrujesh H M'
    elif i==32:
        name='Yogitha'
    elif i==33:
        name='Akshatha'
    elif i==34:
        name='Anjali'
    elif i==35:
        name='Josvin'
    elif i==36:
        name='Keerthana'
    elif i==37:
        name='Shubham'
    elif i==38:
        name='Vidhin'
    elif i==39:
        name='Sudhanva Acharya'
    elif i==40:
        name='Sameer G'
    elif i==41:
        name='Leeladhar Shetty'
    elif i==42:
        name='Vignesh Kini'
    elif i==43:
        name='Basangouda Patil'
    elif i==44:
        name='Sushmita Shetty'
    elif i==45:
        name='Vijetha'
    elif i==46:
        name='Harshitha G S '
    elif i==47:
        name='Arvind B R'
    elif i==48:
        name='Ankith Bhandary'
    elif i==49:
        name='Abhishek Dileep'
    elif i==50:
        name='Ranjitha A S' 
    elif i==51:
        name='Pramod Shet'

    df=pd.read_excel("E:\\AtharvED\\AI\\Book1.xlsx",name)
    
    def array_creater(X):
        conv_list=[]
        for i in range(len(X)):
            #j=df['Total'][i].strftime("%H:%M:%S")
            j=X[i].strftime("%H:%M:%S")
            conv_list.append(j)
        return conv_list
    
    a=df['Total']  

    list_Total=array_creater(a)

    def converter(l1):
        l2=[]
        l5=[]
        for i in l1:
          l3=i.split(':')
          l4=[]
          for j in l3:
              l4.append(int(j))
          sum=0
          for k in l4:
            if l4.index(k)==0:
               sum+=k
            if l4.index(k)==1:
               sum+=(k/60)
            if l4.index(k)==2:
               sum+=(k/3600)
          l5.append(sum)
        return l5

    Total=converter(list_Total)
    
    avg=sum(Total)/len(Total)
    
    average.append(round(avg,2))
    performers.append(name)
    performers1.append(name)


average_hours=[]
average_hours1=[] 
for i in average:
    average_hours.append(i)
    average_hours1.append(i)
    

average_working_hour=sum(average)/len(average)

average.sort(reverse=True)


top_5_performers_hour=[]
top_10_performers_hour=[]
top_20_performers_hour=[]
top_30_performers_hour=[]
for i in range(len(average)):
    if i<5:
        top_5_performers_hour.append(average[i])
    if i<10:
        top_10_performers_hour.append(average[i])
    if i<20:
        top_20_performers_hour.append(average[i])
    if i<30:
        top_30_performers_hour.append(average[i])

def performance(hour_list,ran):
    print('Top ',ran,' performers are: ')
    for i in hour_list:
        var=0
        for j in average_hours:
            if i==j:
                m=performers[var]
                print(m,':','Average working hours',i)
            var+=1

avg_top_5_performers=sum(top_5_performers_hour)/len(top_5_performers_hour)
avg_top_10_performers=sum(top_10_performers_hour)/len(top_10_performers_hour)
avg_top_20_performers=sum(top_20_performers_hour)/len(top_20_performers_hour)
avg_top_30_performers=sum(top_30_performers_hour)/len(top_30_performers_hour)

for i in top_5_performers_hour:
    var=0
    for j in average_hours1:
        if i==j:
            m=performers1[var]
            performers1.remove(m)
            average_hours1.remove(i)
        var+=1

excluded_average_hours=sum(average_hours1)/len(average_hours1)

for i in range(51): 
    if i==0:
        name='Akashraj Bhat'
    elif i==1:
        name='Aman Kumar Srivastav'
    elif i==2:
        name='Anarghya S R'
    elif i==3:
        name='Anush Laila'
    elif i==4:
        name='Avish Shetty'
    elif i==5:
        name='Deekshith Prabhu'
    elif i==6:
        name='Dhanraj'
    elif i==7:
        name='Meghana'
    elif i==8:
        name='Mokshith S Pergade'
    elif i==9:
        name='Namya Shetty'
    elif i==10:
        name='Neha U'
    elif i==11:
        name='Nidish Rao'
    elif i==12:
        name='Poornima'
    elif i==13:
        name='Pranathi Acharya'
    elif i==14:
        name='Prasidda Hegde'
    elif i==15:
        name='Prathik Nayak'
    elif i==16:
        name='Prathiksha'
    elif i==17:
        name='Praveen nayak'
    elif i==18:
        name='Preetham G S'
    elif i==19:
        name='Rishabh Gujarati'
    elif i==20:
        name='S R Udith'
    elif i==21:
        name='Sharath Hulekal'
    elif i==22:
        name='Shashank H S'
    elif i==23:
        name='Shreya R'
    elif i==24:
        name='Shreyas S'
    elif i==25:
        name='Shrinivas Anand Kamath'
    elif i==26:
        name='Vadiraj'
    elif i==27:
        name='Vanshika Shenoy'
    elif i==28:
        name='Varsha G D'
    elif i==29:
        name='Vikas'
    elif i==30:
        name='Vineeth D Shetty'
    elif i==31:
        name='Vrujesh H M'
    elif i==32:
        name='Yogitha'
    elif i==33:
        name='Akshatha'
    elif i==34:
        name='Anjali'
    elif i==35:
        name='Josvin'
    elif i==36:
        name='Keerthana'
    elif i==37:
        name='Shubham'
    elif i==38:
        name='Vidhin'
    elif i==39:
        name='Sudhanva Acharya'
    elif i==40:
        name='Sameer G'
    elif i==41:
        name='Leeladhar Shetty'
    elif i==42:
        name='Vignesh Kini'
    elif i==43:
        name='Basangouda Patil'
    elif i==44:
        name='Sushmita Shetty'
    elif i==45:
        name='Vijetha'
    elif i==46:
        name='Harshitha G S '
    elif i==47:
        name='Arvind B R'
    elif i==48:
        name='Ankith Bhandary'
    elif i==49:
        name='Abhishek Dileep'
    elif i==50:
        name='Ranjitha A S' 
    elif i==51:
        name='Pramod Shet'

        
    df=pd.read_excel("E:\\AtharvED\\AI\\Book1.xlsx",name)
    

    def array_creater(X):
        conv_list=[]
        for i in range(len(df.Total)):
            j=X[i].strftime("%H:%M:%S")
            conv_list.append(j)
        return conv_list

    list_Total=array_creater(df['Total'])
    list_Learning=array_creater(df['Learning'])
    list_R_and_D=array_creater(df['R&D'])
    list_Discussion=array_creater(df['Discussion'])
    list_Project=array_creater(df['Project'])

    def converter(l1):
        l5=[]
        for i in l1:
          l3=i.split(':')
          l4=[]
          for j in l3:
              l4.append(int(j))
          lsum=0
          for k in l4:
            if l4.index(k)==0:
                lsum+=k
            if l4.index(k)==1:
                lsum+=(k/60)
            if l4.index(k)==2:
                lsum+=(k/3600)
          l5.append(lsum)
        return l5
    

    Total=converter(list_Total)
    Learning=converter(list_Learning)
    R_and_D=converter(list_R_and_D)
    Discussion=converter(list_Discussion)
    Project=converter(list_Project)

    def sum_list(lis):
        sum_l=0
        for i in lis:
            sum_l+=i
        return sum_l


    sum_Total=sum_list(Total)
    sum_Learning=sum_list(Learning)
    sum_R_and_D=sum_list(R_and_D)
    sum_Discussion=sum_list(Discussion)
    sum_Project=sum_list(Project)

    working_hours_list=[sum_Learning,sum_R_and_D,sum_Discussion,sum_Learning]
    working_labels=['learning','R&D','Discussion','Project']

    plt.pie(working_hours_list,labels=working_labels,radius=1.25,autopct='%0.2f%%',shadow=True,startangle=45)

    plt.title('Monthly Plot')

    plt.savefig("E:\\AtharvED\\AI\\{}monpie.pdf".format(name),bbox_inches='tight',pad_inches=1)
    plt.close()


    group_list=[]
    a=0
    for i in range(0,len(Total),3):
        group_list.append(Total[a:(a+3)])
        a=i+3


    average_list=[]

    for group in group_list:
        sum=0
        for num in group:
            sum+=num
        sum=sum/len(group)
        average_list.append(sum)

    x_pos=[]

    for i in range(0,len(Total),3):
        x_pos.append(i)


    df.Date=df['Date'].dt.date
    x_lim=np.arange(len(df.Date))
    plt.xticks(x_lim,df.Date,rotation=75)


    plt.plot(x_pos,average_list,label='Total hours')
    plt.axhline(excluded_average_hours,color='r',label="Average Hours")

    plt.ylim(0,15)
    plt.ylabel('Number of Hours Worked')
    plt.xlabel('Date')
    plt.title('Monthly plot')
    plt.legend()

    plt.savefig("E:\\AtharvED\\AI\\{}moncurve.pdf".format(name),bbox_inches='tight',pad_inches=1)
    plt.close()

    #calculating average
    avg=round(sum_Total/len(Total),2)

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=15)
    pdf.cell(10,10,txt='Average working hour in AthrvEd is {}'.format(round(average_working_hour,2)),ln=1)
    pdf.cell(10,30,txt='Top 5 performers are :',ln=1)
    for i in top_5_performers_hour:
            var=0
            for j in average_hours:
                if i==j:
                    m=performers[var]
                    pdf.cell(10,10,txt=str(m)+' # Average working hours is: '+str(i),ln=1)
                var+=1

    pdf.cell(10,30,txt='Average working hour of top 5 performers is '+str(round(avg_top_5_performers,2)),ln=1)

    pdf.cell(10,30,txt='Average working hours of the members excluding top 5 performers is '+str(round(excluded_average_hours,2)),ln=1)


    pdf.cell(10,20,txt=name,ln=1)
    pdf.cell(10,10,txt='Average working hour :'+str(round(avg,2)),ln=1)

    if avg<excluded_average_hours:
        pdf.cell(10,10,txt='Your performance is below average',ln=1)
        pdf.cell(10,10,txt='To meet the average working hour you have to work '+str(round(excluded_average_hours-avg,2))+' hours extrs per day',ln=1)
    elif avg in top_5_performers_hour:
        pdf.cell(10,10,txt='Keep it up. Maintain the same',ln=1)
    elif avg in top_10_performers_hour:
        pdf.cell(10,10,txt='To be among top 5 performers you should work '+str(round(avg_top_5_performers-avg,2))+' hours extra per day',ln=1)
    elif avg in top_20_performers_hour:
        pdf.cell(10,10,txt='To be among top 5 performers you should work '+str(round(avg_top_5_performers-avg,2))+' hours extra per day',ln=1)
        pdf.cell(10,10,txt='To be among top 10 performers you should work '+str(round(avg_top_10_performers-avg,2))+' hours extra per day',ln=1)
    elif avg in top_30_performers_hour:
        pdf.cell(10,10,txt='To be among top 5 performers you should work '+str(round(avg_top_5_performers-avg,2))+' hours extra per day',ln=1)
        pdf.cell(10,10,txt='To be among top 10 performers you should work '+str(round(avg_top_10_performers-avg,2))+' hours extra per day',ln=1)
        pdf.cell(10,10,txt='To be among top 20 performers you should work '+str(round(avg_top_20_performers-avg,2))+' hours extra per day',ln=1)
    
        
    pdf.output("E:\\AtharvED\\AI\\{}working_hour.pdf".format(name))


    pdfs=["E:\\AtharvED\\AI\\template.pdf".format(name),"E:\\AtharvED\\AI\\{}working_hour.pdf".format(name),"E:\\AtharvED\\AI\\{}monpie.pdf".format(name),"E:\\AtharvED\AI\\{}moncurve.pdf".format(name)]

    merger=PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("E:\\AtharvED\AI\\{}.pdf".format(name))
