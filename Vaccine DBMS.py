def leap(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                c='yes'
            else:
                c='no'
        else:
            c='yes'
    else:
        c='no'
    return c    


def dateoapp(dat):
    if dat[3:5]=='02':
        if leap(int(dat[6:10]))=='yes':
            if int(dat[0:2])>15:
                y1=str(int(dat[0:2])-15)
                if len(y1)==1:
                    y1='0'+y1
                g12='03'
                f12=dat[6:10]
                sp='/'.join((y1,g12,f12))
            else:
                y1=str(int(dat[0:2])+14)
                g12='02'
                f12=dat[6:10]
                sp='/'.join((y1,g12,f12))    
        else:
             if int(dat[0:2])>14:
                y1=str(int(dat[0:2])-14)
                if len(y1)==1:
                    y1='0'+y1
                g12='03'
                f12=dat[6:10]
                sp='/'.join((y1,g12,f12))
             else:
                y1=str(int(dat[0:2])+14)
                g12='02'
                f12=dat[6:10]
                sp='/'.join((y1,g12,f12))
    elif dat[3:5]=='01' or dat[3:5]=='03' or dat[3:5]=='05' or dat[3:5]=='07' or dat[3:5]=='08' or dat[3:5]=='10' or dat[3:5]=='12':
        if dat[3:5]=='12':
            if int(dat[0:2])>17:
                y1=str(int(dat[0:2])-17)
                if len(y1)==1:
                    y1='0'+y1
                g12='01'
                f12=str(int(dat[6:10])+1)
                sp='/'.join((y1,g12,f12))
            else:
                y1=str(int(dat[0:2])+14)
                g12='12'
                f12=dat[6:10]
                sp='/'.join((y1,g12,f12))
        else:
            if int(dat[0:2])>17:
                y1=str(int(dat[0:2])-17)
                if len(y1)==1:                       
                    y1='0'+y1
                g12=str(int(dat[3:5])+1)
                if len(g12)==1:                     
                    g12='0'+g12
                f12=dat[6:10]
                sp='/'.join((y1,g12,f12))
            else:
                y1=str(int(dat[0:2])+14)
                g12=dat[3:5]
                f12=dat[6:10]
                sp='/'.join((y1,g12,f12))
    else:
        if int(dat[0:2])>16:
            y1=str(int(dat[0:2])-16)
            if len(y1)==1:
                y1='0'+y1
            g12=str(int(dat[3:5])+1)
            if len(g12)==1:
                g12='0'+g12
            f12=dat[6:10]
            sp='/'.join((y1,g12,f12))
        else:
            y1=str(int(dat[0:2])+14)
            g12=dat[3:5]
            f12=dat[6:10]
            sp='/'.join((y1,g12,f12))
    return sp        

                       
import mysql.connector as msql
print("                                                                                       𝒲𝑒𝓁𝒸𝑜𝓂𝑒 𝓉𝑜                                                                    ")
print("                                                            ------------------------------------------------------------                                   ")
print("                                                                 𝖁𝖆𝖈𝖈𝖎𝖓𝖊 𝕯𝖆𝖙𝖆𝖇𝖆𝖘𝖊 𝕸𝖆𝖓𝖆𝖌𝖊𝖒𝖊𝖓𝖙 𝕻𝖗𝖔𝖌𝖗𝖆𝖒                                  ")
print("                                                            ------------------------------------------------------------                                   ")
usern=input("\nEnter Username (Default : root) : ")
passw=input("Enter Password : ")
d=msql.connect(host="localhost",username=usern,password=passw)

                                                                                                                                                                                    
if d.is_connected():
    print("\n                                                                    Connection to Database Established....")
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

print("\nAvailable Databases : \n")
c=d.cursor()
a="show databases"
b=c.execute(a)

for i in c:
    print(i[0])


chck=int(input("""
                                                                  How do you want to proceed?
                                                      [Choose any one of the following to proceed]
                                                              
1. CREATE new database Vaccine Management

2. CONTINUE with existing database Vaccine Management
    [If the database is already created]
    

Enter Option : """))
print()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

if chck==1:
    c=d.cursor()
    c.execute("drop database if exists vaccinemanagement")
    c.execute("create database vaccinemanagement")
    c.execute("use vaccinemanagement")
    c.execute("create table vaccine( s_no integer not null unique, token_number integer not null primary key, Name varchar(35) not null , gender char(1) not null, age char(3) not null, Adhaar_no char(12) not null unique,DOB char(10),vaccine_center varchar(20) not null, vaccine_type varchar(11) not null,date_of_dose char(10) not null, mobile_no bigint, date_of_2nd_dose char(10), date_of_3rd_dose char(10))")
    c.execute("insert into vaccine values(0,100,'','','','','','','','',0,'','')")
    d.commit()
    print("""
                                                   **Vaccine Management** - Database created successfully!

                                                                    ---------------------------------------------
                                                                    Covid - 19 Vaccine DBMS Software
                                                                    ---------------------------------------------
                                                          
""")
    
elif chck==2:
    c=d.cursor()
    c.execute("use vaccinemanagement")
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

while 1<2 and chck!=3:
    print("""                                                         ------------Data of Vaccinated Patients------------
                                               [Choose any of the following to modify the patient's data]
                                                        
MAIN MENU :

1. ADD data
2. CHANGE data
3. VIEW data
4. DELETE data
5. View STATISTICS
6. View RECEIPT
7. EXIT program

                                ___________________________________________________________                                       """)
    
    msd=int(input("\nEnter Option : "))
    if msd==1: 
        x1=1
        c.execute("select * from vaccine")
        datain= c.fetchall()
        list2=[]
        
        for rowk in datain:
            list2.append(rowk)   
        s_nu= list2[len(list2)-1][0] +1
        tkno=list2[len(list2)-1][1]+1
        
        while x1==1:
            nam=str(input("\nEnter Name of the patient (max : 35 characters) : "))                                                               
            gen=str(input("Enter Gender (M/F) : "))
            agee=str(input("Enter Age : "))
            adhaarno=str(input("Enter Aadhaar Number (12 digits) : "))
            dateobirth=str(input("Enter Date Of Birth (DD/MM/YYYY) : "))
            vaccinecen=str(input("Enter Name of Vaccine Center : "))
            vaccinetyp=str(input("Enter Type of Vaccine (Covaxin/Covishield) : "))
            dateodose=str(input("Enter Date of Dose : "))
            mobno=int(input("Enter Mobile Number (10 digits) : "))
            
            dat_2=dateoapp(dateoapp(dateoapp(dateoapp(dateoapp(dateoapp(dateodose))))))
            dat_3=dateoapp(dateoapp(dateoapp(dateoapp(dateoapp(dateoapp(dat_2))))))
            
            ts="insert into vaccine(s_no, token_number, Name, gender, age, Adhaar_no, DOB, vaccine_center, vaccine_type, date_of_dose, mobile_no, date_of_2nd_dose, date_of_3rd_dose) values({},{},'{}','{}','{}','{}','{}','{}','{}','{}',{},'{}','{}')".format(s_nu, tkno, nam, gen, agee, adhaarno, dateobirth, vaccinecen, vaccinetyp, dateodose, mobno, dat_2, dat_3)
            c.execute(ts)
            d.commit()
            print()
            
            file2=open("medicalr2.txt","a")
            print("""                                                                    ------------Enter Medical Results------------
""")
            BP=input("Enter Blood pressure (in mm Hg) : ")
            sugar=int(input("Enter sugar level in blood (in mg/dL) : "))
            pulse=int(input("Enter pulse rate (in beats/min) : "))
            
            mrec=" ".join((str(tkno),nam,agee,str(BP),str(sugar),str(pulse)))+'$'
            file2.write(mrec)
            file2.close()
            print()
            
            print("----Data Added Successfully----")
            
            lok=int(input("""
                                                                  How do you want to proceed?
                                                      [Choose any one of the following to proceed]

1. Add another patient's data
2. Back to main menu

Enter Option : """))

            if lok==1:
                print()
                x1=1
                tkno=tkno+1
                s_nu=s_nu+1
            elif lok==2:
                x1=0
                print("\nFinal Table :-")
                c.execute("select * from vaccine")
                dataout=c.fetchall()
                print("""\nColumn names :
(S.NO, Token Number, Name, Gender, Age, Aadhaar Number, DOB, Vaccine Center, Vaccine Type, Date of Dose, Mobile Number, Date of 2nd Dose, Date of 3rd Dose)\n""")
                
                for rowh in dataout:
                    if dataout.index(rowh)!=0:
                        print(rowh)
                print()    
            else:
                print("Invalid Input")
                print()
                x1=0
        file2.close()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
        
    elif msd==2:
        tnov=int(input("\nEnter Token number (for verification) : "))
        c.execute("select * from vaccine")
        datao=c.fetchall()     
        S1=[]
        F1=[]

        for rowh in datao:
            if datao.index(rowh)!=0:
                S1.append(rowh)

        for kq in range(0,len(S1)):  
            if tnov in S1[kq]: 
                F1.append('Success')

        if 'Success' in F1:   
            d2="select * from vaccine where token_number={}".format(tnov)
            c.execute(d2)
            q0=c.fetchall()
            print()
            print("""\nColumn names :
(S.NO, Token Number, Name, Gender, Age, Aadhaar Number, DOB, Vaccine Center, Vaccine Type, Date of Dose, Mobile Number, Date of 2nd Dose, Date of 3rd Dose)\n""")
            
            for v in q0:    
                print(v)
            fq=int(input("""\n                                                                         What do you want to change?

1. Name
2. Gender
3. Age
4. Aadhaar Number
5. DOB
6. Mobile Number

Enter Option : """))

            
            if fq==1:   
                NN=input("\nEnter New Name : ")
                quer="UPDATE vaccine set Name='{}' where token_number={}".format(NN,tnov)                
                c.execute(quer)
                d.commit()
                print()
                fil3=open("medicalr2.txt",'r')
                stro4=fil3.readline()
                strin90=stro4.split('$')
                fil3.close()
                fil4=open("medicalr2.txt",'w')
                
                for xy7 in strin90:
                    if str(tnov) in xy7:
                        delta=xy7.split()
                        delta[1]=NN
                        mgm=" ".join(delta)                                                            
                        indexo=strin90.index(xy7)
                        strin90[indexo]=mgm
                xy8="$".join(strin90)
                fil4.write(xy8)        
                fil4.close()
                print("----Name --> Successfully Updated----")                                                   


            elif fq==2:
                NN=input("\nEnter Gender : ")
                quer="UPDATE vaccine set gender='{}' where token_number={}".format(NN,tnov)
                c.execute(quer)
                d.commit()
                print()
                print("----Gender --> Successfully Updated----")


            elif fq==3:
                NN=input("\nEnter Age : ")
                quer="UPDATE vaccine set age='{}' where token_number={}".format(NN,tnov)
                c.execute(quer)
                d.commit()
                print()
                fil3=open("medicalr2.txt",'r')
                stro4=fil3.readline()
                strin90=stro4.split('$')
                fil3.close()
                fil4=open("medicalr2.txt",'w')                                                          

                for xy7 in strin90:
                    if str(tnov) in xy7:
                        delta=xy7.split()
                        delta[2]=NN
                        mgm=" ".join(delta)                                                            
                        indexo=strin90.index(xy7)
                        strin90[indexo]=mgm
                xy8="$".join(strin90)
                fil4.write(xy8)        
                fil4.close()
                print("----Age --> Successfully Updated----")


            elif fq==4:
                NN=str(input("\nEnter Aadhar Number : "))
                quer="UPDATE vaccine set Adhaar_no='{}' where token_number={}".format(NN,tnov)
                c.execute(quer)
                d.commit()
                print()
                print("----Aadhar Number --> Successfully Updated----")


            elif fq==5:
                NN=input("\nEnter DOB : ")
                quer="UPDATE vaccine set DOB='{}' where token_number={}".format(NN,tnov)
                c.execute(quer)
                d.commit()
                print()
                print("----DOB --> Successfully Updated----")    


            elif fq==6:
                NN=int(input("\nEnter Mobile Number : "))
                quer="UPDATE vaccine set mobile_no='{}' where token_number={}".format(NN,tnov)
                c.execute(quer)
                d.commit()
                print()
                print("----Mobile Number --> Successfully Updated----")


            else:
                print()
                print("""Invalid Option!!
Returning to MAIN MENU....""")
                print()
            d3="select * from vaccine where token_number={}".format(tnov)
            c.execute(d3)
            q9=c.fetchall()
            print()
            
            print("""\nColumn names :
(S.NO, Token Number, Name, Gender, Age, Aadhaar Number, DOB, Vaccine Center, Vaccine Type, Date of Dose, Mobile Number, Date of 2nd Dose, Date of 3rd Dose)\n""")

            for ut in q9:
                print(ut)
            print()    

        else:
            print()
            print("Entered Token Number does not exist. \nInvalid token number!!")
            print()            

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    elif msd==3:
        while 4>3:
            print()
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
            op=int(input("""                                                                         What do you want to view?

1. ALL Data
2. Particular Patient's Data
3. Exit

Enter Option : """))

            if op==1:
                print()
                c.execute("select * from vaccine")
                dataoutin=c.fetchall()
                print("""\nColumn names :
(S.NO, Token Number, Name, Gender, Age, Aadhaar Number, DOB, Vaccine Center, Vaccine Type, Date of Dose, Mobile Number, Date of 2nd Dose, Date of 3rd Dose)\n""")
                
                for rowhg in dataoutin:
                    if dataoutin.index(rowhg)!=0:
                        print(rowhg)


            elif op==2:
                print()
                tnoo=int(input("Enter Token Number (for verification) : "))
                c.execute("select * from vaccine")
                datai=c.fetchall()
                A1=[]
                E1=[]

                for rowhh in datai:
                    if datai.index(rowhh)!=0:
                        A1.append(rowhh)

                for kt in range(0,len(A1)):
                    if tnoo in A1[kt]:
                        E1.append("Success")

                if "Success" in E1:
                    d5="select * from vaccine where token_number={}".format(tnoo)
                    c.execute(d5)
                    q90=c.fetchall()
                    print()
                    
                    print("""\nColumn names :
(S.NO, Token Number, Name, Gender, Age, Aadhaar Number, DOB, Vaccine Center, Vaccine Type, Date of Dose, Mobile Number, Date of 2nd Dose, Date of 3rd Dose)\n""")
                    for x in q90:
                        print(x)
                    print()    

                else:
                    print()
                    print("Entered Token number does not exists. \nInvalid token number!!")
                    print()


            elif op==3:
                print("\nReturning to MAIN MENU....")
                print()
                break;


            else:
                print()
                print("Invalid option!!  \nEnter again.")      

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    elif msd==4:
        print()
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        ok=int(input("""                                                                         What data do you want to delete?

1. Whole Database
2. Particular Row
3. Exit

Enter Option : """))

        if ok==1:
            c.execute("drop database if exists vaccinemanagement")
            file28=open("medicalr2.txt","w")
            file28.close()
            print("----Database **vaccinemanagement** successfully deleted----")
            print()     
            break;


        elif ok==2:
            print()
            tnoo=int(input("Enter Token Number (for verification) : "))
            c.execute("select * from vaccine")
            datai=c.fetchall()
            A1=[]
            E1=[]

            for rowhh in datai:
                if datai.index(rowhh)!=0:
                    A1.append(rowhh)

            for kt in range(0,len(A1)):
                if tnoo in A1[kt]:
                    E1.append('Success')

            if 'Success' in E1:
                d5="select * from vaccine where token_number={}".format(tnoo)
                c.execute(d5)
                q90=c.fetchall()
                print()
                print("""\nColumn names :
(S.NO, Token Number, Name, Gender, Age, Aadhaar Number, DOB, Vaccine Center, Vaccine Type, Date of Dose, Mobile Number, Date of 2nd Dose, Date of 3rd Dose)\n""")

                for x in q90:
                    print(x)
                print()    
                yon=int(input("""                                                                         Do you want to delete this row?

1. Yes
2. No [Exits to Main Menu]

Enter Option : """))

                if yon==1:
                    fil=open("medicalr2.txt",'r')
                    stro=fil.readline()
                    stro2=stro.split("$")                                                      
                    fil.close()
                    fil2=open("medicalr2.txt",'w')      
                    stro3=''

                    for x9 in stro2:
                        if x9!='':
                            if str(tnoo) in x9:                                               
                                continue;                                                     
                            stro3=stro3+x9+'$'
                        else:
                             continue;                                                                
                    fil2.write(stro3)
                    fil2.close()
                    d6="delete from vaccine where token_number={}".format(tnoo)
                    do2="update vaccine set s_no=s_no-1 where token_number>{}".format(tnoo)
                    c.execute(d6)
                    c.execute(do2)
                    d.commit()
                    print()
                    print("----Row --> Successfully deleted from the table----")
                    print()

                elif yon==2:
                    print("Returning to MAIN MENU....")

                else:
                    print("Invalid option!! \nReturning to main menu....") 

            else:
                print("Token number does not exists. \nInvalid token number!!")


        elif ok==3:
            print("Returning to MAIN MENU....")

        else:
            print()
            print("Invalid input!! \nReturning to MAIN MENU....") 

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    elif msd==5:
        g0="select * from vaccine where gender='M'"
        c.execute(g0)
        sar=c.fetchall()
        mg=c.rowcount
        print("\nNumber of MALE patients who got 1ST DOSE of vaccine : ",mg)
        print()
        
        g100="select * from vaccine where gender='F'"
        c.execute(g100)
        sara=c.fetchall()
        ng=c.rowcount
        print("Number of FEMALE patients who got 1ST DOSE of vaccine : ",ng)
        print()
        
        gz="select * from vaccine"
        c.execute(gz)
        say=c.fetchall()
        og=c.rowcount
        print("TOTAL number of patients who got 1ST DOSE of vaccine:",og-1)
        print()
        
        gy="select * from vaccine where vaccine_type='covaxin'"
        c.execute(gy)
        sir=c.fetchall()
        pg=c.rowcount
        print("Number of patients who got dose of COVAXIN vaccine : ",pg)
        print()
        
        gx="select * from vaccine where vaccine_type='Covishield'"
        c.execute(gx)
        sr=c.fetchall()
        qg=c.rowcount
        print("Number of patients who got dose of COVISHIELD vaccine : ",qg)
        print()
        
        gw="select * from vaccine where age>44"
        c.execute(gw)
        suv=c.fetchall()
        rg=c.rowcount
        print("Number of vaccinated patients above age of 45 : ",rg)
        print()
        
        gv="select * from vaccine where age>17 and age<45"
        c.execute(gv)
        uv=c.fetchall()
        rh=c.rowcount
        print("Number of vaccinated patients between age of 18 AND 45 : ",rh)
        print()

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        
        d24=int(input("""                                    Do you want to view the number of patients from a particular vaccine center?

1. Yes
2. No [Returns to Main Menu]

Enter Option : """))
        if d24==1:
            bane=str(input("\nEnter Centre Name : "))
            gu="select * from vaccine where vaccine_center='{}'".format(bane)
            c.execute(gu)
            vv=c.fetchall()
            ri=c.rowcount
            print("\nNumber of vaccinated patients from",bane,':',ri)
            print()

        elif d24==2:                      
            print()
            print("Returning to MAIN MENU....")

        else:
            print("""Invalid Option \n Returning to MAIN MENU....""")        


    elif msd==6:
        print()
        opqr=str(input("Enter Token Number for Medical Receipt : "))
        with open("medicalr2.txt",'r') as file22:
            veron='true'
            while veron=='true':
                strin=file22.readline()
                if opqr in strin and int(opqr)>100:
                    tow=strin.split('$')
                    findx="true"
                    for xy10 in tow:
                        if opqr in xy10:
                            indext=tow.index(xy10)
                            findx='true'
                            break;
                        else:
                            findx='false'
                            
                    if findx=='false':
                        veron='false'
                        break;
                    mew=tow[indext]                                                            
                    pi=mew.split()                          
                    ga2=pi[0]
                    ga3=pi[1]
                    ga4=pi[2]
                    ga5=pi[3]
                    ga6=pi[4]
                    ga7=pi[5]
                    print()
                    
                    print("Receipt of the Patient : ")
                    print("""                                                                  
---------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                               MEDICAL RECEIPT
---------------------------------------------------------------------------------------------------------------------------------------------------------
\n                                                                              | Token Number : """,ga2,'''     
\n                                                                              | Name : ''',ga3,'''                   
\n                                                                              | Age : ''',ga4,'''                      
\n                                                                              | Blood Pressure : ''',ga5,'''     
\n                                                                              | Sugar Level : ''',ga6,'''          
\n                                                                              | Pulse Rate : ''',ga7)
                    
                    ga8="select Name, date_of_2nd_dose, date_of_3rd_dose from vaccine where token_number={}".format(opqr)
                    c.execute(ga8)
                    q90=c.fetchall()
                    print()
                    
                    print("""----| Column Names :
(Name, Date of 2nd Dose, Date of 3rd Dose)
""")
                    
                    for x in q90:
                        print(x)
                    print()
                    print("""---------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------
 """)
                    break;

                else:
                    veron='false'
            if veron=='false':
                print()
                print("Token number does not exists \nInvalid Token Number!!")
                print()           

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    elif msd==7:
        print()
        print("                                                                                     Program Terminated ")
        print("                                                                              Database closed successfully")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("                                                                  𝓣𝓱𝓪𝓷𝓴 𝓨𝓸𝓾 𝓯𝓸𝓻 𝓾𝓼𝓲𝓷𝓰 𝓥𝓪𝓬𝓬𝓲𝓷𝓮 𝓓𝓑𝓜𝓢!                                                 ")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\n                                                                    ---------------xxxxxxxxxxxxxx--------------                                                   ")
        break;
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    else:
        print("Invalid input ---- Enter again!")

        
