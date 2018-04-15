import tkinter
import Registratie_Systeem
from tkinter import ttk

class Login(tkinter.Tk):
    def __init__(self, parent):
        # constructor voor de tkinter
        tkinter.Tk.__init__(self, parent)
        # verwijzing naar de parent
        self.parent = parent
        # roep de methode initialize aan
        self.Loginwindow()

    def Loginwindow(self):
        # verdele het form in een gid voor het possitioneren van de gui elementen
        self.grid()

        # label naam
        label_Sys = tkinter.Label(self, text='Login Registratie systeem ', font=('Calibri', 16), anchor='e')
        label_Sys.grid(column=0, row=1, sticky='EW', columnspan=2)

        # label Medewerker id
        label_Batch = tkinter.Label(self, text='Medewerker ID: ', anchor="w")
        label_Batch.grid(column=0, row=2, sticky='EW', pady=5)

        # entry Medewerker id
        Entry_Batch = ttk.Entry(self)
        Entry_Batch.grid(column=1, row=2, sticky='EW', pady=5, padx=5)

        # label Wachtwoord
        label_Locatie = tkinter.Label(self, text='Wachtwoord: ', anchor="w")
        label_Locatie.grid(column=0, row=3, sticky='EW', pady=5)

        # entry Wachtwoord
        Entry_Locatie = ttk.Entry(self, show="*")
        Entry_Locatie.grid(column=1, row=3, sticky='EW', pady=5, padx=5)

        # Button Login
        button_Login = tkinter.Button(self, text='Login', command=self.Regi_window)
        button_Login.grid(column=0, row=4, sticky='EW', pady=5, padx=5, columnspan=2)
    
    # registratie window wordt geopend
    def Regi_window(self):
        #self.RegiWindow = tkinter.Toplevel(self.parent)
        self.app = Registratie(None)
        self.destroy()

if __name__ == "__main__":
    app = Login(None)
    app.title('Batch registratie systeem')
    app.mainloop()