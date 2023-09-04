import tkinter as tk
from tkinter import PhotoImage, StringVar, Menu, Toplevel, IntVar
import tkinter.messagebox
from func import shutdown, restart, logout , cancel 

class App:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title('System Scheduler')
        self.app.geometry('400x400')
        self.app.resizable(False, False)

        self.iconphoto = PhotoImage(file='static/icon.png')
        self.app.iconphoto(False, self.iconphoto)
        self.alarm_png = PhotoImage(file='static/alarm.png')
        self.background_label = tk.Label(self.app, image=self.alarm_png)
        self.background_label.place(relwidth=1, relheight=1)
#---------------------------------------------------------------------------------------------------------        
        self.title_label = tk.Label(self.app, text='System scheduler', bg='skyblue', fg='red', bd=6, relief='flat', cursor='clock', font=15)
        self.title_label.pack(side='top', pady=20)
#---------------------------------------------------------------------------------------------------------
        def contactwindow():
            contactwindow = Toplevel(self.app)
            contactwindow.geometry('250x50')
            iconphoto = PhotoImage(file='static/contact.png')
            contactwindow.iconphoto(False, iconphoto) 
            newlabel = tk.Label(contactwindow, text="contact me with:\n\nerfansafarali98@gmail.com")
            newlabel.pack()

        def helpwindow():
            helpwindow = Toplevel(self.app)
            helpwindow.geometry('350x70')
            iconphoto = PhotoImage(file='static/help.png')
            helpwindow.iconphoto(False, iconphoto) 
            newlabel = tk.Label(helpwindow, text="1-First choose your schedule \n 2-Set your time \n 3-Click on the run \n 4-Your can reset (cancel) your schedule by clicking on the Abort")
            newlabel.pack()

        self.menubar = Menu(self.app)
        self.help_menu = Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label='Help', command=helpwindow)
        self.help_menu.add_command(label='Contact', command=contactwindow)
        self.menubar.add_cascade(label='Help', menu=self.help_menu)
        self.app.config(menu=self.menubar)
#---------------------------------------------------------------------------------------------------------

        self.frame_radio = tk.Frame(self.app, bg='DarkOliveGreen1', cursor='hand2') 
        self.frame_radio.pack(pady=10)

        self.v1 = StringVar()

        self.radio_options_shutdown = tk.Radiobutton(self.frame_radio, text='Shutdown', variable=self.v1, value='1', bg='DarkOliveGreen1')
        self.radio_options_shutdown.pack()
   
        self.radio_options_restart = tk.Radiobutton(self.frame_radio, text='Restart', variable=self.v1, value='2', bg='DarkOliveGreen1')
        self.radio_options_restart.pack()
        self.radio_options_shutdown.select()

        self.radio_options_logout = tk.Radiobutton(self.frame_radio, text='Logout', variable=self.v1, value='3', bg='DarkOliveGreen1')
        self.radio_options_logout.pack()

        self.varhour = IntVar()
        self.varminute = IntVar()
        self.varsecond = IntVar()

        self.spinlabel = tk.Label(self.app, bg='cyan2')
        self.spinlabel.pack(pady=30)

        self.hour_label = tk.Label(self.spinlabel, text='Hour' ,bg='cyan2')
        self.hour_label.grid(row=0, column=0)
        self.hourspin = tk.Spinbox(self.spinlabel, from_=0, to=100, textvariable=self.varhour, width=5)
        self.hourspin.grid(row=1, column=0)

        self.minute_label = tk.Label(self.spinlabel, text='Minute',bg='cyan2')
        self.minute_label.grid(row=0, column=1)
        self.minutepin = tk.Spinbox(self.spinlabel, from_=0, to=60, textvariable=self.varminute, width=5)
        self.minutepin.grid(row=1, column=1)

        self.second_label = tk.Label(self.spinlabel, text='Second',bg='cyan2')
        self.second_label.grid(row=0, column=2)
        self.secondpin = tk.Spinbox(self.spinlabel, from_=0, to=60, textvariable=self.varsecond, width=5)
        self.secondpin.grid(row=1, column=2)
#---------------------------------------------------------------------------------------------------------

        self.submit_button = tk.Button(text='Run', command=self.run_command ,bg='yellow2',relief='groove')
        self.submit_button.pack(pady=10)


        def cancel_all():
                cancel()
                cancelwindow = Toplevel()
                cancelwindow.geometry('300x50')
                iconphoto = PhotoImage(file='static/icon.png')
                cancelwindow.iconphoto(False, iconphoto) 
                cancel_label =tk.Label(cancelwindow, text=f"The opration Aborted")
                cancel_label.pack()
              


        self.cancel_button = tk.Button(text='Abort' , command=cancel_all,bg='red',relief='groove')
        self.cancel_button.pack(pady=5)
#---------------------------------------------------------------------------------------------------------

        self.app.mainloop()
#---------------------------------------------------------------------------------------------------------

    def show_result(self ,sent_varsum,opration):

        resultwindow = Toplevel(self.app)
        resultwindow.geometry('300x50')
        iconphoto = PhotoImage(file='static/icon.png')
        resultwindow.iconphoto(False, iconphoto) 
        newlabel =tk.Label(resultwindow, text=f"Your PC is scheduled to {opration} in {sent_varsum} seconds")
        newlabel.pack()



    def run_command(self):
        varsum = (self.varhour.get() * 3600) + (self.varminute.get() * 60) + self.varsecond.get()
        
        if self.v1.get() == '1':  # 1 = shutdown
            shutdown(varsum)
            self.show_result(sent_varsum=varsum , opration = 'shutdown')
        elif self.v1.get() == '2':  # 2 = restart
            restart(varsum)
            self.show_result(sent_varsum=varsum , opration = 'restart')
        elif self.v1.get() == '3':  #4 = logout
            logout()       
        else:
            tkinter.messagebox.showwarning("Warning", "There is a problem with your given time ")

app = App()
