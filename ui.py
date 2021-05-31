'''
this code wont run on sololearn playground.

the create button works, you have to input the correct format of information for the next button to work.

It doesnt store any information

it might not run on python 2.x and uncomment line 690 to overwrite tkinter default icon but you'll have to save and convert the facebook logo to ico filetype and make sure its the same folder with your code or just put the file type
'''


try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import re

font15 = "-family {Segoe UI} -size 10 -weight normal -slant "  \
                   "roman -underline 0 -overstrike 0"
font10 = "-family {Segoe UI} -size 11 -weight normal -slant "  \
                 "roman -underline 0 -overstrike 0"
font13 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
               "roman -underline 0 -overstrike 0"
font12 = "-family {Segoe UI} -size 13 -weight normal -slant "  \
                   "roman -underline 0 -overstrike 0"
font17 = "-family {Segoe UI} -size 10 -weight normal -slant "  \
               "roman -underline 0 -overstrike 0"


class fbapp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self,*args,**kwargs)
        box = tk.Frame(self)
        
        box.pack(side="top", fill="both", expand = True)
        
        box.grid_rowconfigure(0, weight=1)
        box.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for window in (login,pagethree,createnewaccount,pagefour,pagefive):
            
            frame = window(box,self)
            
            self.frames[window] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(login)
    
    
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class login(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="LogIn!!!")
        label.pack(pady=10,padx=10)
        
        self.configure(background="#e7e9f1")
        
        font13 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
                 "roman -underline 0 -overstrike 0"
        font15 = "-family {Segoe UI} -size 24 -weight bold -slant "  \
                 "roman -underline 0 -overstrike 0"
        
        font19 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
                   "roman -underline 0 -overstrike 0"


        self.Canvas1 = tk.Canvas(self)
        self.Canvas1.place(relx=-0.012, rely=0.0, relheight=0.115
                     , relwidth=1.038)
        self.Canvas1.configure(background="#3b5998",borderwidth="1",relief="ridge")


        self.fbheader = tk.Label(self)
        self.fbheader.place(relx=0.235, rely=0.007, height=46, width=165)
        self.fbheader.configure(background="#3b5998",font=font15,foreground="#fff",text="facebook")

        self.Canvas2 = tk.Canvas(self)
        self.Canvas2.place(relx=-0.029, rely=0.109, relheight=0.115
                           , relwidth=1.038)
        self.Canvas2.configure(background="#f0f9bf",borderwidth="1",relief="ridge")


        self.getfbwth = tk.Label(self.Canvas2)
        self.getfbwth.place(relx=0.136, rely=0.226, height=27, width=272)
        self.getfbwth.configure(background="#f0f9bf",borderwidth="0",font=font17,foreground="#5c40e1",
                                text="Get Facebook for Android and browse faster.")

        self.username_Entry = tk.Entry(self)
        self.username_Entry.place(relx=0.056, rely=0.241,height=25, relwidth=0.894)
        self.username_Entry.configure(background="white",font="TkFixedFont",foreground="#000000")
        self.username_Entry.insert(0,"Mobile number or Email address")

        self.password_Entry = tk.Entry(self)
        self.password_Entry.place(relx=0.056, rely=0.293,height=25, relwidth=0.894)
        self.password_Entry.configure(background="white",font="TkFixedFont",foreground="#000000",show="$")               

        self.Login_Button = tk.Button(self)
        self.Login_Button.place(relx=0.059, rely=0.365, height=27, width=297)
        self.Login_Button.configure(background="#4a73fd",foreground="#fff",pady="0",text="Log In")

        self.Separator1 = ttk.Separator(self)
        self.Separator1.place(relx=0.074, rely=0.45, relwidth=0.382)

        self.Separator2 = ttk.Separator(self)
        self.Separator2.place(relx=0.568, rely=0.45, relwidth=0.382)
  
        self.ore = tk.Label(self)
        self.ore.place(relx=0.459, rely=0.426, height=21, width=34)
        self.ore.configure(background="#ececec",font=font17,foreground="#000000",text="or")

        self.create_new_acc_Button = tk.Button(self)
        self.create_new_acc_Button.place(relx=0.285, rely=0.485, height=24, width=150)
        self.create_new_acc_Button.configure(background="#209926",font=font19,foreground="#fff",pady="0",text="Create New Account"
                                             ,command= lambda: controller.show_frame(createnewaccount))

        self.forgotten_password_Button = tk.Button(self)
        self.forgotten_password_Button.place(relx=0.318, rely=0.541, height=24, width=127)
        self.forgotten_password_Button.configure(background="#ececec",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                               text="Forgetten password?")

        self.Canvas3 = tk.Canvas(self)
        self.Canvas3.place(relx=-0.009, rely=0.63, relheight=0.376
                           , relwidth=1.038)
        self.Canvas3.configure(background="#fff",relief="ridge")

        self.England_Button = tk.Button(self.Canvas3)
        self.England_Button.place(relx=0.125, rely=0.11, height=24, width=77)
        self.England_Button.configure(background="#fff",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="England(UK)")

        self.French_Button = tk.Button(self.Canvas3)
        self.French_Button.place(relx=0.102, rely=0.249, height=24, width=97)
        self.French_Button.configure(background="#fff",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Français(France)")

        self.Espanol_Button = tk.Button(self.Canvas3)
        self.Espanol_Button.place(relx=0.125, rely=0.393, height=24, width=77)
        self.Espanol_Button.configure(background="#fff",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Espanol")

        self.Deutch_Button = tk.Button(self.Canvas3)
        self.Deutch_Button .place(relx=0.125, rely=0.538, height=24, width=77)
        self.Deutch_Button.configure(background="#fff",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Deutsch")
 
        self.Hausa_Button = tk.Button(self.Canvas3)
        self.Hausa_Button.place(relx=0.541, rely=0.11, height=24, width=77)
        self.Hausa_Button.configure(background="#fff",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Hausa")

        self.portugese_Button = tk.Button(self.Canvas3)
        self.portugese_Button.place(relx=0.541, rely=0.249, height=24, width=97)
        self.portugese_Button.configure(background="#fff",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Portugese(Brazil)")

        self.Arabic_Button = tk.Button(self.Canvas3)
        self.Arabic_Button.place(relx=0.541, rely=0.393, height=24, width=77)
        self.Arabic_Button.configure(background="#fff",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="العربية")

        self.Other_Button = tk.Button(self.Canvas3)
        self.Other_Button.place(relx=0.615, rely=0.538, height=24, width=27)
        self.Other_Button.configure(background="#fff",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="+")

        self.Label4 = tk.Label(self.Canvas3)
        self.Label4.place(relx=0.346, rely=0.751, height=21, width=89)
        self.Label4.configure(background="#fff",font=font17,foreground="#808080",text="Facebook Inc.")

class createnewaccount(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="LogIn!!!")
        label.pack(pady=10,padx=10)
        
        self.configure(background="#e7e9f1")
            
        self.Canvas1 = tk.Canvas(self)
        self.Canvas1.place(relx=-0.029, rely=0.0, relheight=0.1, relwidth=1.068)
        self.Canvas1.configure(background="#3b5998",borderwidth="2",relief="ridge")

                            
        self.Joinfb_header = tk.Label(self.Canvas1)
        self.Joinfb_header.place(relx=0.32, rely=0.196, height=26, width=120)
        self.Joinfb_header.configure(background="#3b5998",font=font12,foreground="#fff",text='''Join Facebook''')
        
        
        self.wyn = tk.Label(self)
        self.wyn.place(relx=0.221, rely=0.115, height=31, width=176)
        self.wyn.configure(background="#e7e9f1",font=font13,foreground="#000000",text="What's your name?")

        self.eyn = tk.Label(self)
        self.eyn.place(relx=0.159, rely=0.174, height=26, width=233)
        self.eyn.configure(background="#e7e9f1",font=font10,foreground="#808080",text="Enter the name you use in real life.")

        self.first_name = tk.Label(self)
        self.first_name.place(relx=0.076, rely=0.226, height=21, width=84)
        self.first_name.configure(background="#e7e9f1",font=font10,foreground="#000000",text="First Name")

        self.surname = tk.Label(self)
        self.surname.place(relx=0.526, rely=0.22, height=21, width=84)
        self.surname.configure(background="#e7e9f1",font="-family {Segoe UI} -size 11",text="Surname")

        self.First_name_Entry = tk.Entry(self)
        self.First_name_Entry.place(relx=0.094, rely=0.272,height=20, relwidth=0.335)
        self.First_name_Entry.configure(background="white",font="TkFixedFont",foreground="#000000")

        self.Surname_Entry = tk.Entry(self)
        self.Surname_Entry.place(relx=0.556, rely=0.27,height=20, relwidth=0.335)
        self.Surname_Entry.configure(background="white",font="TkFixedFont",foreground="#000000")
        
        def check_name_length():
            firstname = self.First_name_Entry.get()
            surname = self.Surname_Entry.get()
            pattern = re.compile("[a-z A-z]{3,}")
            if pattern.match(firstname) and pattern.match(surname):
                controller.show_frame(pagethree)
            else:
                tk.messagebox.showwarning("","Enter a name longer than 3 charactres")
        self.Next_Button = tk.Button(self)
        self.Next_Button.place(relx=0.235, rely=0.348, height=24, width=177)
        self.Next_Button.configure(background="#5c40e1",font=font10,
                             foreground="#ffffff",pady="0",text="Next",command= check_name_length)

        self.hvacct = tk.Button(self)
        self.hvacct.place(relx=0.059, rely=0.443, height=24, width=156)
        self.hvacct.configure(background="#e7e9f1",pady="0",borderwidth="0",text="Already have an account?",
                                    foreground="#5c40e1",font=font15)
        self.Canvas3 = tk.Canvas(self)
        self.Canvas3.place(relx=0.00, rely=0.543, relheight=0.376
                           , relwidth=1.038)
        self.Canvas3.configure(background="#e7e9f1",borderwidth="0",relief="ridge")

        self.England_Button = tk.Button(self.Canvas3)
        self.England_Button.place(relx=0.125, rely=0.11, height=24, width=77)
        self.England_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="England(UK)")

        self.French_Button = tk.Button(self.Canvas3)
        self.French_Button.place(relx=0.102, rely=0.249, height=24, width=97)
        self.French_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Français(France)")

        self.Espanol_Button = tk.Button(self.Canvas3)
        self.Espanol_Button.place(relx=0.125, rely=0.393, height=24, width=77)
        self.Espanol_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Espanol")

        self.Deutch_Button = tk.Button(self.Canvas3)
        self.Deutch_Button .place(relx=0.125, rely=0.538, height=24, width=77)
        self.Deutch_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Deutsch")
 
        self.Hausa_Button = tk.Button(self.Canvas3)
        self.Hausa_Button.place(relx=0.541, rely=0.11, height=24, width=77)
        self.Hausa_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Hausa")

        self.portugese_Button = tk.Button(self.Canvas3)
        self.portugese_Button.place(relx=0.541, rely=0.249, height=24, width=97)
        self.portugese_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Portugese(Brazil)")

        self.Arabic_Button = tk.Button(self.Canvas3)
        self.Arabic_Button.place(relx=0.541, rely=0.393, height=24, width=77)
        self.Arabic_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="العربية")

        self.Other_Button = tk.Button(self.Canvas3)
        self.Other_Button.place(relx=0.615, rely=0.538, height=24, width=27)
        self.Other_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="+")

        self.fbinc = tk.Label(self.Canvas3)
        self.fbinc.place(relx=0.346, rely=0.751, height=21, width=89)
        self.fbinc.configure(background="#e7e9f1",font=font17,foreground="#808080",text="Facebook Inc.")
                                    
        self.back = tk.Button(self)
        self.back.place(relx=0.385, rely=0.94, height=25, width=76)
        self.back.configure(background="#5c40e1",font=font10,
                             foreground="#ffffff",pady="0",text="Back",command= lambda: controller.show_frame(login))

class pagethree(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="LogIn!!!")
        label.pack(pady=10,padx=10)     
        
        self.configure(background="#e7e9f1")
        
        font10 = "-family {Segoe UI} -size 11 -weight normal -slant "  \
                  "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
                  "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 14 -weight bold -slant roman"  \
                   " -underline 0 -overstrike 0"
        self.Canvas1 = tk.Canvas(self)
        self.Canvas1.place(relx=0.0, rely=0.0, relheight=0.1, relwidth=1.068)
        self.Canvas1.configure(background="#3b5998",borderwidth="2",relief="ridge")
                               
        self.Joinfb_header = tk.Label(self.Canvas1)
        self.Joinfb_header.place(relx=0.32, rely=0.196, height=26, width=120)
        self.Joinfb_header.configure(background="#3b5998",font=font12,foreground="#fff",text='''Join Facebook''')

        self.wydob = tk.Label(self)
        self.wydob.place(relx=0.141, rely=0.113, height=26, width=250)
        self.wydob.configure(background="#e7e9f1",font=font9,foreground="#000",text="What's your date of birth?")

        self.choose_dob = tk.Label(self)
        self.choose_dob.place(relx=0.041, rely=0.167, height=26, width=320)
        self.choose_dob.configure(background="#e7e9f1",borderwidth="0",font=font10,foreground="#808080",
                              text="Choose your date of birth. You can always make")

        self.choose_dob_1 = tk.Label(self)
        self.choose_dob_1.place(relx=0.253, rely=0.215, height=26, width=160)
        self.choose_dob_1.configure(activeforeground="black")
        self.choose_dob_1.configure(background="#e7e9f1",borderwidth="0",font="-family {Segoe UI} -size 11",
                                foreground="#808080",text="this private later.")

        self.birthday = tk.Label(self)
        self.birthday.place(relx=0.044, rely=0.274, height=26, width=61)
        self.birthday.configure(background="#e7e9f1",font=font11,foreground="#000000",text="Birthday")

        self.day = ttk.Combobox(self)
        self.day.place(relx=0.065, rely=0.33, relheight=0.067
                              , relwidth=0.185)
        self.value_list = list(range(1,32))
        self.value_list.insert(0,"Day")
        self.day.configure(values=self.value_list,state="readonly")
        self.day.current(0)

        self.month = ttk.Combobox(self)
        self.month.place(relx=0.291, rely=0.33, relheight=0.067
                                , relwidth=0.215)
        self.value_list = ['Month','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
        self.month.configure(values=self.value_list)
        self.month.configure(state="readonly")
        self.month.current(0)

        self.year = ttk.Combobox(self)
        self.year.place(relx=0.544, rely=0.333, relheight=0.067
                                    , relwidth=0.215)
        self.value_list = list(range(1900,2020))
        self.value_list.insert(0,"Year")
        self.year.configure(values=self.value_list[::-1],state="readonly")
        self.year.current(len(self.value_list)-1)
        
        def quick_check():
            day = self.day.get()
            month = self.month.get()
            year = self.year.get()
            if day!="Day" and month!="Month" and year!="Year":
                controller.show_frame(pagefour)
            else:
                tk.messagebox.showwarning("","Select your date of birth")
        self.Next_Button = tk.Button(self)
        self.Next_Button.place(relx=0.235, rely=0.420, height=24, width=177)
        self.Next_Button.configure(background="#5c40e1",font=font10,
                             foreground="#ffffff",pady="0",text="Next",command= quick_check)
                             
        self.hvacct = tk.Button(self)
        self.hvacct.place(relx=0.059, rely=0.483, height=24, width=156)
        self.hvacct.configure(background="#e7e9f1",pady="0",borderwidth="0",text="Already have an account?",
                                    foreground="#5c40e1",font=font15)
        self.Canvas3 = tk.Canvas(self)
        self.Canvas3.place(relx=0.00, rely=0.543, relheight=0.376
                           , relwidth=1.038)
        self.Canvas3.configure(background="#e7e9f1",borderwidth="0",relief="ridge")

        self.England_Button = tk.Button(self.Canvas3)
        self.England_Button.place(relx=0.125, rely=0.11, height=24, width=77)
        self.England_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="England(UK)")

        self.French_Button = tk.Button(self.Canvas3)
        self.French_Button.place(relx=0.102, rely=0.249, height=24, width=97)
        self.French_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Français(France)")

        self.Espanol_Button = tk.Button(self.Canvas3)
        self.Espanol_Button.place(relx=0.125, rely=0.393, height=24, width=77)
        self.Espanol_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Espanol")

        self.Deutch_Button = tk.Button(self.Canvas3)
        self.Deutch_Button .place(relx=0.125, rely=0.538, height=24, width=77)
        self.Deutch_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Deutsch")
 
        self.Hausa_Button = tk.Button(self.Canvas3)
        self.Hausa_Button.place(relx=0.541, rely=0.11, height=24, width=77)
        self.Hausa_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Hausa")

        self.portugese_Button = tk.Button(self.Canvas3)
        self.portugese_Button.place(relx=0.541, rely=0.249, height=24, width=97)
        self.portugese_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Portugese(Brazil)")

        self.Arabic_Button = tk.Button(self.Canvas3)
        self.Arabic_Button.place(relx=0.541, rely=0.393, height=24, width=77)
        self.Arabic_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="العربية")

        self.Other_Button = tk.Button(self.Canvas3)
        self.Other_Button.place(relx=0.615, rely=0.538, height=24, width=27)
        self.Other_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="+")

        self.fbinc = tk.Label(self.Canvas3)
        self.fbinc.place(relx=0.346, rely=0.751, height=21, width=89)
        self.fbinc.configure(background="#e7e9f1",font=font17,foreground="#808080",text="Facebook Inc.")
        
        self.back = tk.Button(self)
        self.back.place(relx=0.385, rely=0.94, height=25, width=76)
        self.back.configure(background="#5c40e1",font=font10,
                             foreground="#ffffff",pady="0",text="Back",command= lambda: controller.show_frame(login))
                             
class pagefour(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="LogIn!!!")
        label.pack(pady=10,padx=10)     
        
        font9 = "-family {Segoe UI} -size 14 -weight bold -slant roman"  \
               " -underline 0 -overstrike 0"
              
        font10 = "-family {Segoe UI} -size 11 -weight normal -slant "  \
                   "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
                  "roman -underline 0 -overstrike 0"
        
        self.configure(background="#e7e9f1")
                       
        self.Canvas1 = tk.Canvas(self)
        self.Canvas1.place(relx=0.0, rely=0.0, relheight=0.1, relwidth=1.068)
        self.Canvas1.configure(background="#3b5998",borderwidth="2",relief="ridge",)
                              
        self.Joinfb_header = tk.Label(self.Canvas1)
        self.Joinfb_header.place(relx=0.32, rely=0.196, height=26, width=120)
        self.Joinfb_header.configure(background="#3b5998",font=font12,foreground="#fff",text='''Join Facebook''')

        self.enter_ur_phone_header = tk.Label(self)
        self.enter_ur_phone_header.place(relx=0.118, rely=0.104, height=26, width=290)
        self.enter_ur_phone_header.configure(background="#e7e9f1",font=font9,foreground="#000000",text="Enter your phone number")

        self.enter_ur_phone_sub_header = tk.Label(self)
        self.enter_ur_phone_sub_header .place(relx=0.041, rely=0.154, height=26, width=320)
        self.enter_ur_phone_sub_header .configure(background="#e7e9f1",borderwidth="0",font=font10,foreground="#808080"
                              ,text="Enter the mobile number on which you can be")

        self.enter_ur_phone_sub_header_1 = tk.Label(self)
        self.enter_ur_phone_sub_header_1.place(relx=0.074, rely=0.196, height=26, width=300)
        self.enter_ur_phone_sub_header_1.configure(background="#e7e9f1",borderwidth="0",font="-family {Segoe UI} -size 11",
                                foreground="#808080",text="contacted. You can hide this from your profile")
        
        self.Label2_2 = tk.Label(self)
        self.Label2_2.place(relx=0.247, rely=0.239, height=26, width=160)
        self.Label2_2.configure(background="#e7e9f1",borderwidth="0",font="-family {Segoe UI} -size 11",
                                foreground="#808080",text="later.")

        self.phone_num = tk.Label(self)
        self.phone_num.place(relx=0.020, rely=0.291, height=26, width=120)
        self.phone_num.configure(background="#e7e9f1",font=font11,foreground="#000000",text="Phone Number")

        self.phone_num_Entry = tk.Entry(self)
        self.phone_num_Entry.place(relx=0.029, rely=0.343,height=30, relwidth=0.894)
        self.phone_num_Entry.configure(background="white",font="TkFixedFont",foreground="#000000")
                                       
        def check_phone_num():
            phone_num = self.phone_num_Entry.get()
            pattern = re.compile("[+][0-9]{8,14}|[0-9]{8,14}")
            if pattern.match(phone_num):
                controller.show_frame(login)
            else:
                tk.messagebox.showwarning("","Not a phone number format")

        self.next = tk.Button(self)
        self.next.place(relx=0.297, rely=0.437, height=24, width=117)
        self.next.configure(background="#5c40e1",font=font10,
                             foreground="#ffffff",pady="0",text="Next",command= check_phone_num)

        self.instead = tk.Button(self)
        self.instead.place(relx=0.234, rely=0.492, height=24, width=170)
        self.instead.configure(background="#e7e9f1",foreground="#5c40e1",pady="0",borderwidth="0",
                               text="Sign up using email address",command=lambda: controller.show_frame(pagefive))
                               
        self.back = tk.Button(self)
        self.back.place(relx=0.385, rely=0.94, height=25, width=76)
        self.back.configure(background="#5c40e1",font=font10,
                             foreground="#ffffff",pady="0",text="Back",command= lambda: controller.show_frame(login))
                             
        self.Canvas3 = tk.Canvas(self)
        self.Canvas3.place(relx=0.00, rely=0.553, relheight=0.376
                           , relwidth=1.038)
        self.Canvas3.configure(background="#e7e9f1",borderwidth="0",relief="ridge")

        self.England_Button = tk.Button(self.Canvas3)
        self.England_Button.place(relx=0.125, rely=0.11, height=24, width=77)
        self.England_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="England(UK)")

        self.French_Button = tk.Button(self.Canvas3)
        self.French_Button.place(relx=0.102, rely=0.249, height=24, width=97)
        self.French_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Français(France)")

        self.Espanol_Button = tk.Button(self.Canvas3)
        self.Espanol_Button.place(relx=0.125, rely=0.393, height=24, width=77)
        self.Espanol_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Espanol")

        self.Deutch_Button = tk.Button(self.Canvas3)
        self.Deutch_Button .place(relx=0.125, rely=0.538, height=24, width=77)
        self.Deutch_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Deutsch")
 
        self.Hausa_Button = tk.Button(self.Canvas3)
        self.Hausa_Button.place(relx=0.541, rely=0.11, height=24, width=77)
        self.Hausa_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Hausa")

        self.portugese_Button = tk.Button(self.Canvas3)
        self.portugese_Button.place(relx=0.541, rely=0.249, height=24, width=97)
        self.portugese_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Portugese(Brazil)")

        self.Arabic_Button = tk.Button(self.Canvas3)
        self.Arabic_Button.place(relx=0.541, rely=0.393, height=24, width=77)
        self.Arabic_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="العربية")

        self.Other_Button = tk.Button(self.Canvas3)
        self.Other_Button.place(relx=0.615, rely=0.538, height=24, width=27)
        self.Other_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="+")

        self.Label4 = tk.Label(self.Canvas3)
        self.Label4.place(relx=0.346, rely=0.751, height=21, width=89)
        self.Label4.configure(background="#e7e9f1",font=font17,foreground="#808080",text="Facebook Inc.")
                              
class pagefive(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="LogIn!!!")
        label.pack(pady=10,padx=10)     
        
        font9 = "-family {Segoe UI} -size 14 -weight bold -slant roman"  \
               " -underline 0 -overstrike 0"
              
        font10 = "-family {Segoe UI} -size 11 -weight normal -slant "  \
                   "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
                  "roman -underline 0 -overstrike 0"
        
        self.configure(background="#e7e9f1")
                       
        self.Canvas1 = tk.Canvas(self)
        self.Canvas1.place(relx=0.0, rely=0.0, relheight=0.1, relwidth=1.068)
        self.Canvas1.configure(background="#3b5998",borderwidth="2",relief="ridge",)
                              
        self.Joinfb_header = tk.Label(self.Canvas1)
        self.Joinfb_header.place(relx=0.32, rely=0.196, height=26, width=120)
        self.Joinfb_header.configure(background="#3b5998",font=font12,foreground="#fff",text='''Join Facebook''')

        self.sub_header1 = tk.Label(self)
        self.sub_header1.place(relx=0.118, rely=0.104, height=26, width=290)
        self.sub_header1.configure(background="#e7e9f1",font=font9,foreground="#000000",text="Enter your Email address")
                              
        self.sub_header2 = tk.Label(self)
        self.sub_header2.place(relx=0.041, rely=0.154, height=26, width=320)
        self.sub_header2.configure(background="#e7e9f1",borderwidth="0",font=font10,foreground="#808080"
                              ,text="Enter the email address at which you can be")

        self.sub_header3 = tk.Label(self)
        self.sub_header3.place(relx=0.074, rely=0.196, height=26, width=300)
        self.sub_header3.configure(background="#e7e9f1",borderwidth="0",font="-family {Segoe UI} -size 11",
                                foreground="#808080",text="contacted.You can hide this from your profile")

        self.email_label = tk.Label(self)
        self.email_label.place(relx=0.020, rely=0.291, height=26, width=120)
        self.email_label.configure(background="#e7e9f1",font=font11,foreground="#000000",text="Email address")

        self.Later = tk.Label(self)
        self.Later.place(relx=0.247, rely=0.239, height=26, width=160)
        self.Later.configure(background="#e7e9f1",borderwidth="0",font="-family {Segoe UI} -size 11",
                                foreground="#808080",text="later.")

        self.email = tk.Entry(self)
        self.email.place(relx=0.029, rely=0.343,height=30, relwidth=0.894)
        self.email.configure(background="white",font="TkFixedFont",foreground="#000000")
        #'^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$'
        def check_email():
            email = self.email.get()
            pattern = re.compile("^[a-zA-Z0-9_.+-]+@[a-z]+[.][a-z]{2,5}")
            if pattern.match(email):
                controller.show_frame(login)
            else:
                tk.messagebox.showwarning("","Not an email address format")

        self.next = tk.Button(self)
        self.next.place(relx=0.297, rely=0.437, height=24, width=117)
        self.next.configure(background="#5c40e1",font=font10,
                             foreground="#ffffff",pady="0",text="Next",command= check_email)

        self.instead = tk.Button(self)
        self.instead.place(relx=0.234, rely=0.492, height=24, width=170)
        self.instead.configure(background="#e7e9f1",foreground="#5c40e1",pady="0",borderwidth="0",
                               text="Sign up using phone number",command=lambda: controller.show_frame(pagefour))
                               
        self.back = tk.Button(self)
        self.back.place(relx=0.385, rely=0.94, height=25, width=76)
        self.back.configure(background="#5c40e1",font=font10,
                             foreground="#ffffff",pady="0",text="Back",command= lambda: controller.show_frame(login))
                             
        self.Canvas3 = tk.Canvas(self)
        self.Canvas3.place(relx=0.00, rely=0.553, relheight=0.376
                           , relwidth=1.038)
        self.Canvas3.configure(background="#e7e9f1",borderwidth="0",relief="ridge")

        self.England_Button = tk.Button(self.Canvas3)
        self.England_Button.place(relx=0.125, rely=0.11, height=24, width=77)
        self.England_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="England(UK)")

        self.French_Button = tk.Button(self.Canvas3)
        self.French_Button.place(relx=0.102, rely=0.249, height=24, width=97)
        self.French_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Français(France)")

        self.Espanol_Button = tk.Button(self.Canvas3)
        self.Espanol_Button.place(relx=0.125, rely=0.393, height=24, width=77)
        self.Espanol_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Espanol")

        self.Deutch_Button = tk.Button(self.Canvas3)
        self.Deutch_Button .place(relx=0.125, rely=0.538, height=24, width=77)
        self.Deutch_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Deutsch")
 
        self.Hausa_Button = tk.Button(self.Canvas3)
        self.Hausa_Button.place(relx=0.541, rely=0.11, height=24, width=77)
        self.Hausa_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Hausa")

        self.portugese_Button = tk.Button(self.Canvas3)
        self.portugese_Button.place(relx=0.541, rely=0.249, height=24, width=97)
        self.portugese_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="Portugese(Brazil)")

        self.Arabic_Button = tk.Button(self.Canvas3)
        self.Arabic_Button.place(relx=0.541, rely=0.393, height=24, width=77)
        self.Arabic_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="العربية")

        self.Other_Button = tk.Button(self.Canvas3)
        self.Other_Button.place(relx=0.615, rely=0.538, height=24, width=27)
        self.Other_Button.configure(background="#e7e9f1",borderwidth="0",font=font17,foreground="#5c40e1",pady="0",
                                      text="+")

        self.Label4 = tk.Label(self.Canvas3)
        self.Label4.place(relx=0.346, rely=0.751, height=21, width=89)
        self.Label4.configure(background="#e7e9f1",font=font17,foreground="#808080",text="Facebook Inc.")
                           





if __name__ == '__main__':
    app = fbapp()
    app.geometry("340x460+525+103")
    #app.iconbitmap("fb.ico")
    app.title("Facebook - log in or sign up")
    app.configure(background="#dfe3ee")
    app.mainloop()
