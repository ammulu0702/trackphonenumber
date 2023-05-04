from tkinter import *
from threading import *
import pywhatkit
import urllib
import phone
import mysql.connector

from datetime import datetime 

t=datetime.now()
#print(t.hour)

root=Tk()
root.configure(bg="skyblue")
root.geometry('1030x900')
root.iconbitmap('flames/lb.ico')
root.title("FLAMES")
bg = PhotoImage(file ="nature.png")#only png formate images

# Show image using label
l= Label( root, image = bg)
l.place(x=0,y=0)



        
        
        
class flames(Thread):
    def run(self,sname,lname):
        global val,rc
        self.sname=sname
        self.lname=lname
        self.sname.lower()
        self.lname.lower()
        a,b=[],[]

        for i in self.sname:
            a.append(i)
        for j in self.lname:
            b.append(j)
        for i in self.sname:
            if i in b:
                
                a.remove(i)
                b.remove(i)
            
        m=a+b
        rc=0
        for i in m:
            rc+=1
        result=['f','l','a','m','e','s']
        while len(result)>1:
            s=(rc%len(result)-1)
            if s >= 0 :
                
                r=result[s+1:] 
                l=result[:s] 
                result=r+l

            else:
                result=result[:len(result)-1]
        key=result[0]
        d={'f':'friend','l':'lover','a':'attraction','m':'marriage','e':'enemy','s':'sister'}
        for i in d.keys():
            if i==key:
                val=d[i]
        Label(root,text=val,font=("arial",15),bg="yellow",fg="white").grid()

    def send_what_msg(self,c_code,bphone,gphone):
        self.c_code=c_code
        self.b_phone=bphone
        self.g_phone=gphone
        self.bg_phone=self.c_code+self.b_phone
        self.gb_phone=self.c_code+self.g_phone

        if phone.vpn(self.bg_phone)==True and phone.vpn(self.gb_phone)==True:
            urllib.request.urlopen('https://web.whatsapp.com/')
            pywhatkit.sendwhatmsg(self.bg_phone,val,t.hour,t.minute+2)
            
        
        
    def database(self,name1,name2
                 ,b1_phone,g1_phone):
        self.run(boy.get(),girl.get())
        self.sname=name1
        self.lname=name2
        self.bphone=b1_phone
        self.gphone=g1_phone
        self.tul=rc
        self.relation=val
        

        self.main=mysql.connector.connect(host="localhost",port='3306',user='root',database='flames')
        self.cur=self.main.cursor()
        query="insert into flames_data values(%s,%s,%s,%s,%s,%s)"
        values=(self.sname,self.lname,self.bphone,self.gphone,self.tul,self.relation)
        self.cur.execute(query,values)
        self.main.commit()
        
       
    

 


def flame():
    f=flames()
    f.daemon=True
    f.run(boy.get(),girl.get())
   
    f.database(boy.get(),girl.get(),b_phone.get(),g_phone.get())

    f.send_what_msg(country_code.get(),b_phone.get(),g_phone.get())
    
    f.start()

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
Label(root,text="Enter Boy Name:",font=("arial",15),bg="yellow",fg="black").grid(row=0,column=0,sticky=W,pady=10)
boy=Entry(root,font=("arial",15),bg="yellow",fg="green")
boy.grid(row=0,column=1,sticky=E)
Label(root,text="Enter girl Name:",font=("arial",15),bg="yellow",fg="black").grid(row=1,column=0,sticky=W,pady=10)
girl=Entry(root,font=("arial",15),bg="yellow",fg="green")
girl.grid(row=1,column=1,sticky=E)
Label(root,text="Enter Boy mobile number:",font=("arial",15),bg="yellow",fg="black").grid(row=2,column=0,sticky=W,pady=10)
b_phone=Entry(root,font=("arial",15),bg="yellow",fg="green")
b_phone.grid(row=2,column=1,sticky=E)
Label(root,text="Enter girl mobile number:",font=("arial",15),bg="yellow",fg="black").grid(row=3,column=0,sticky=W,pady=10)
g_phone=Entry(root,font=("arial",15),bg="yellow",fg="green")
g_phone.grid(row=3,column=1,sticky=E)
Label(root,text="Enter country code with sings:",font=("arial",15),bg="yellow",fg="black").grid(row=4,column=0,sticky=W,pady=10)
country_code=Entry(root,font=("arial",15),bg="yellow",fg="green")
country_code.grid(row=4,column=1,sticky=E)
boy.delete(0,END)
girl.delete(0,END)
b_phone.delete(0,END)
g_phone.delete(0,END)
country_code.delete(0,END)
b=Button(root,text="Find Relation",font=("arial",15),bg="orange",fg="yellow",command=flame).grid(row=5,column=2,sticky=W)  










root.mainloop()