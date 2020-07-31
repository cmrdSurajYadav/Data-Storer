from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.title('DATA STORE APP-BY SURAJ')
root.iconbitmap('ico.ico.ico')
root.config(bg='white')
root.resizable(width=False, height=False)
# name_var=StringVar()

def action():

    with open('filedata.txt','a') as f:
        f.write(f'New Data enter From {name_ent.get()}')
        f.write(f'\nName is {name_ent.get()} ')
        f.write(f'\nAge is {age_ent.get()} ')
        f.write(f'\nEmail is {email_ent.get()} ')
        f.write(f'\n gender is {gender_ent.get()}')
        f.write(f'\nqualification is {qulification_ent.get()}')
        f.write(f'\n work as a {prop.get()}')
        f.write(f'\n______________________________________\n')
        nm=name_ent.get()
        ag=age_ent.get()
        em=email_ent.get()

        messagebox.showinfo('DATA SAVED','YOUR DATA SUCCESSFULLY SAVED')
        name.set('')
        age.set('')
        email.set('')
def reset():
        r=messagebox.askquestion('RESET','Your Data Will Be Disapear')
        if r in 'yes':
            name.set('')
            age.set('')
            email.set('')
        if r in 'no':
            name_ent.set(nm)
            age.set(ag)
            email.set(em)

        


    
f=('Helvetica')
name_lab=ttk.Label(root,text='Enter Your Name :',font=f)
name_lab.grid(row=0,column=0)
name=StringVar()
name_ent=ttk.Entry(root,textvariable=name,width=27,font=f)
name_ent.grid(row=0,column=1)
name_ent.focus()


age_lab=ttk.Label(root,text='Enter Your age :',font=f)
age_lab.grid(row=1,column=0)
age=StringVar()
age_ent=ttk.Entry(root,textvariable=age,width=27,font=f)
age_ent.grid(row=1,column=1)


email_lab=ttk.Label(root,text='Enter Your Email :',font=f)
email_lab.grid(row=2,column=0)
email=StringVar()
email_ent=ttk.Entry(root,textvariable=email,width=27,font=f)
email_ent.grid(row=2,column=1)

genderl=Label(root,text='Select Your Gender :',font=f)
genderl.grid(row=3,column=0)

gender=StringVar()

gender_ent=ttk.Combobox(root,width=24,state='readonly',textvariable=gender,font=f)
gender_ent['values']=('Male','Female','Other')
gender_ent.grid(row=3,column=1)
gender_ent.current(0)

qualification_la=ttk.Label(root,text='Your bes Qalification :',font=f)
qualification_la.grid(row=4,column=0)


quali=StringVar()

qulification_ent=ttk.Combobox(root,width=24,state='readonly',textvariable=quali,font=f)
qulification_ent.grid(row=4,column=1)
qulification_ent['values']=("10TH",'12TH','BA','Diploma','B.TECH','M.TECH')
qulification_ent.current(1)


prop=StringVar()

prop_t=ttk.Radiobutton(root,text='Student',value='student',variable=prop,)
prop_t.grid(row=5,column=0)

prop_t1=ttk.Radiobutton(root,text='Teacher',value='teachar',variable=prop,)
prop_t1.grid(row=5,column=1)


check=IntVar()

check1=ttk.Checkbutton(root,text='Your Data Will be Save In File You Can Not Change This',)
check1.grid(row=6,columnspan=3)

Button=ttk.Button(root,text='RESET',width=47,command=reset,).grid(row=7,column=0)
Button2=ttk.Button(root,text='SUBMIT',width=47,command=action,).grid(row=7,column=1)

nm=name_ent.get()
ag=age_ent.get()
em=email_ent.get()




root.mainloop()
