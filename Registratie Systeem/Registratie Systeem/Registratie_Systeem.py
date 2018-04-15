import MySQLdb
import tkinter
from tkinter import ttk

# connection details voor de database
conn = MySQLdb.connect(host='localhost',
                        port=3307,
                        database='sbsh',
                        user='root',
                        password='usbw')

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
        label_Medewerker = tkinter.Label(self, text='Medewerker ID: ', anchor="w")
        label_Medewerker.grid(column=0, row=2, sticky='EW', pady=5)

        # entry Medewerker id
        self.Entry_Medewerker = ttk.Entry(self)
        self.Entry_Medewerker.grid(column=1, row=2, sticky='EW', pady=5, padx=5)

        # label Wachtwoord
        label_Wachtwoord = tkinter.Label(self, text='Wachtwoord: ', anchor="w")
        label_Wachtwoord.grid(column=0, row=3, sticky='EW', pady=5)

        # entry Wachtwoord
        self.Entry_Wachtwoord = ttk.Entry(self, show="*")
        self.Entry_Wachtwoord.grid(column=1, row=3, sticky='EW', pady=5, padx=5)

        # Button Login
        button_Login = tkinter.Button(self, text='Login', command=self.GetUser)
        button_Login.grid(column=0, row=4, sticky='EW', pady=5, padx=5, columnspan=2)
    
    # registratie window wordt geopend
    def Regi_window(self):
        #self.RegiWindow = tkinter.Toplevel(self.parent)
        self.app = Registratie(None)
        self.destroy()
    
    def GetUser(self):
        # waardes uit de entry boxen
        ID = self.Entry_Medewerker.get()
        WW = self.Entry_Wachtwoord.get()      
        # connectie naar de database openen
        cursor = conn.cursor()
        # Query uitvoeren
        cursor.execute("SELECT Medewerker_ID, Wachtwoord, Functie FROM medewerker Where Medewerker_ID= %s AND Wachtwoord= %s",  (ID, WW))
        # Check of het wachtwoordt klopt
        for row in cursor:
            if row[1] == WW:  
                self.Func = row[2]
                # open het registratie scherm
                self.app = Registratie(None)
                self.destroy()

class Registratie(tkinter.Tk):
    def __init__(self, parent):
        # constructor voor de tkinter
        tkinter.Tk.__init__(self, parent)
        # verwijzing naar de parent
        self.parent = parent
        # roep de methode initialize aan
        self.Regi()

    def Regi(self):
        # verdele het form in een gid voor het possitioneren van de gui elementen
        self.grid()       
        # label naam
        label_Sys = tkinter.Label(self, text='Batch Registratie systeem ', font=('Calibri', 20), anchor='e')
        label_Sys.grid(column=3, row=1, sticky='EW')

        # label batch
        label_Batch = tkinter.Label(self, text='Batch ID: ', anchor="w")
        label_Batch.grid(column=0, row=1, sticky='EW', pady=5)

        # entry batch
        self.Entry_Batch = ttk.Entry(self)
        self.Entry_Batch.grid(column=1, row=1, sticky='EW', pady=5)

        # label locatie
        label_Locatie = tkinter.Label(self, text='Locatie: ', anchor="w")
        label_Locatie.grid(column=0, row=2, sticky='EW', pady=5)

        # entry locatie
        self.Entry_Locatie = ttk.Entry(self)
        self.Entry_Locatie.grid(column=1, row=2, sticky='EW', pady=5)

        # label opslag
        label_Opslag = tkinter.Label(self, text='Opslag: ', anchor="w")
        label_Opslag.grid(column=0, row=3, sticky='EW', pady=5)

        # entry opslag
        self.Entry_Opslag = ttk.Entry(self)
        self.Entry_Opslag.grid(column=1, row=3, sticky='EW', pady=5)

        # label opslagrij
        label_OpslagRij = tkinter.Label(self, text='Opslag rij: ', anchor="w")
        label_OpslagRij.grid(column=0, row=4, sticky='EW', pady=5)

        # entry opslag
        self.Entry_OpslagRij = ttk.Entry(self)
        self.Entry_OpslagRij.grid(column=1, row=4, sticky='EW', pady=5)

        # label medewerker
        label_Medewerker = tkinter.Label(self, text='Medewerker ID: ', anchor="w")
        label_Medewerker.grid(column=0, row=5, sticky='EW', pady=5)

        # entry medewerker
        self.Entry_Medewerker = ttk.Entry(self)
        self.Entry_Medewerker.grid(column=1, row=5, sticky='EW', pady=5)

        # label apparaat
        label_Apparaat = tkinter.Label(self, text='Recycle: ', anchor="w")
        label_Apparaat.grid(column=0, row=6, sticky='EW', pady=5)

        # entry apparaat
        self.Entry_Apparaat = ttk.Entry(self)
        self.Entry_Apparaat.grid(column=1, row=6, sticky='EW', pady=5)

        # label aantal
        label_Aantal = tkinter.Label(self, text='Aantal: ', anchor="w")
        label_Aantal.grid(column=0, row=7, sticky='EW', pady=5)

        # entry apparaat
        self.Entry_Aantal = ttk.Entry(self)
        self.Entry_Aantal.grid(column=1, row=7, sticky='EW', pady=5)

        # label inkom datum
        label_inkom = tkinter.Label(self, text='Inkomst datum: ', anchor="w")
        label_inkom.grid(column=0, row=8, sticky='EW', pady=5)

        # entry inkom datum
        self.Entry_inkom = ttk.Entry(self)
        self.Entry_inkom.grid(column=1, row=8, sticky='EW', pady=5)

        # label sloop datum
        label_sloop = tkinter.Label(self, text='Sloop datum: ', anchor="w")
        label_sloop.grid(column=0, row=9, sticky='EW', pady=5)

        # entry sloop datum
        self.Entry_sloop = ttk.Entry(self)
        self.Entry_sloop.grid(column=1, row=9, sticky='EW', pady=5)

        # label voortgang
        label_voortgang = tkinter.Label(self, text='Voortgang: ', anchor="w")
        label_voortgang.grid(column=0, row=10, sticky='EW', pady=5)

        # entry voortgang
        self.Entry_voortgang = ttk.Entry(self)
        self.Entry_voortgang.grid(column=1, row=10, sticky='EW', pady=5)

        # Button Get data
        button_set = tkinter.Button(self, text='Voeg batch toe')
        button_set.grid(column=0, row=11, sticky='EW', pady=5, padx=5)

        # Button Get data
        button_update = tkinter.Button(self, text='Update batch')
        button_update.grid(column=1, row=11, sticky='EW', pady=5, padx=5)

        # Button haal lijst op
        button_lijst = tkinter.Button(self, text='Refresh lijst', command=self.Getbatch)
        button_lijst.grid(column=0, row=12, sticky='EW', pady=5, padx=5)

        # Button Details
        button_detail = tkinter.Button(self, text='Meer details', command=self.OpenDetail)
        button_detail.grid(column=1, row=12, sticky='EW', pady=5, padx=5)

        # Set the treeview
        self.tree = ttk.Treeview(self, columns=('Batch_ID', 'Adres', 'Adres', 'Omschrijving', 'Naam', 'Naam', 'Aantal', 'Inkomst_datum', 'Sloop_Datum', 'Voortgang'))
        # naam/ positie waardes voor de treeview
        self.tree.heading('#1', text='batch ID')
        self.tree.heading('#2', text='Locatie Adres')
        self.tree.heading('#5', text='Medewerker')
        self.tree.heading('#6', text='Recyclenaam')
        self.tree.heading('#7', text='Aantal')
        self.tree.column('#0', minwidth=0)
        self.tree.column('#0', width=0)
        self.tree.column('#3', minwidth=0)
        self.tree.column('#3', width=0)
        self.tree.column('#4', minwidth=0)
        self.tree.column('#4', width=0)
        self.tree.column('#8', minwidth=0)
        self.tree.column('#8', width=0)
        self.tree.column('#9', minwidth=0)
        self.tree.column('#9', width=0)
        self.tree.column('#10', minwidth=0)
        self.tree.column('#10', width=0)
        self.tree.grid(column=2, row=2, columnspan=4, rowspan=10, sticky='nsew', padx=5)
        self.tree.bind("<Double-1>", self.OnDoubleClick)

    def OpenDetail(self):
        self.app = details(None)

    def EmtyEntrybox(self):
        self.Entry_Batch.config(state = 'normal')
        self.Entry_Batch.delete(0, 'end')
        self.Entry_Locatie.delete(0, 'end')
        self.Entry_Opslag.delete(0, 'end')
        self.Entry_OpslagRij.delete(0, 'end')
        self.Entry_Medewerker.delete(0, 'end')
        self.Entry_Apparaat.delete(0, 'end')
        self.Entry_Aantal.delete(0, 'end')
        self.Entry_inkom.delete(0, 'end')
        self.Entry_sloop.delete(0, 'end')
        self.Entry_voortgang.delete(0, 'end')

    def OnDoubleClick(self, event):
        self.EmtyEntrybox()
        # vul de entry boxen met de geselecteerde batch
        item = self.tree.selection()[0]
        self.Entry_Batch.insert(0, self.tree.item(item)['values'][0])
        self.Entry_Batch.config(state = 'disabled')
        self.Entry_Locatie.insert(0, self.tree.item(item)['values'][1])
        self.Entry_Opslag.insert(0, self.tree.item(item)['values'][2]) 
        self.Entry_OpslagRij.insert(0, self.tree.item(item)['values'][3])
        self.Entry_Medewerker.insert(0, self.tree.item(item)['values'][4]) 
        self.Entry_Apparaat.insert(0, self.tree.item(item)['values'][5]) 
        self.Entry_Aantal.insert(0, self.tree.item(item)['values'][6]) 
        self.Entry_inkom.insert(0, self.tree.item(item)['values'][7])
        self.Entry_sloop.insert(0, self.tree.item(item)['values'][8]) 
        self.Entry_voortgang.insert(0, self.tree.item(item)['values'][9]) 

    def Getbatch(self):
        # de treeview leegmaken
        for row in self.tree.get_children():
            self.tree.delete(row)

        cursor = conn.cursor()
        # voer de query uit
        cursor.execute("""SELECT 
	                        b.Batch_ID, 
	                        l.Adres, 
	                        o.Adres,
	                        o.Omschrijving,
	                        m.Naam,
	                        r.Naam,
	                        b.Aantal,
	                        b.Inkomst_Datum,
	                        b.Sloop_Datum,
	                        b.Voortgang
                          FROM 
	                        batch b
	                        INNER JOIN locatie l ON b.Locatie_ID = l.Locatie_ID
	                        INNER JOIN opslag o ON b.Opslag_ID = o.Opslag_ID
	                        INNER JOIN medewerker m ON b.Medewerker_ID = m.Medewerker_ID
	                        INNER JOIN recyclemateriaal r ON b.Recycle_ID = r.Recycle_ID""")
        for row in cursor:
            self.tree.insert('', 0, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

    #def InsertBatch(self):
    #    cursor = conn.cursor()
    #        # voer de query uit
    #    cursor.execute("""insert into batch (, Player_ID, Score_Score, Score_Date) 
    #                            values (%s, %s, %s, %s);""", (game_slice, player, score, datum))

class details(tkinter.Tk):
    def __init__(self, parent):
        # constructor voor de tkinter
        tkinter.Tk.__init__(self, parent)
        # verwijzing naar de parent
        self.parent = parent
        # roep de methode initialize aan
        self.DetailWindow()

    def DetailWindow(self):
        # label naam
        label_Sys = tkinter.Label(self, text='Opbrengst Batch ', font=('Calibri', 16), anchor='e')
        label_Sys.grid(column=2, row=0, sticky='EW')

         # Set the treeview
        self.tree = ttk.Treeview(self, columns=('Materiaal', 'Recyclebaar', 'Kilogram', 'Waarde'))
        # naam/ positie waardes voor de treeview
        self.tree.heading('#1', text='Materiaal')
        self.tree.heading('#2', text='Recyclebaar')
        self.tree.heading('#3', text='Kilogram')
        self.tree.heading('#4', text='Waarde')
        self.tree.column('#0', minwidth=0)
        self.tree.column('#0', width=0)
        self.tree.grid(column=1, row=1, columnspan=4, rowspan=10, sticky='nsew', padx=5)
        #self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.GetMateriaal()

    def GetMateriaal(self):
        # de treeview leegmaken
        for row in self.tree.get_children():
            self.tree.delete(row)

        cursor = conn.cursor()
        # voer de query uit
        cursor.execute("""SELECT
	                        m.Materiaalsoort,
                            m.Recyclebaar,
	                        b.Kilogram,
	                        round(d.Dagprijs * b.Kilogram,2) AS Waarde
                          FROM 
                            Batch_Materiaal b
	                        INNER JOIN Materiaal m ON b.Materiaal_ID = m.Materiaal_ID
	                        INNer JOIN Dagprijs d on m.Materiaal_ID = d.Materiaal_ID
                          Where 
	                        b.Batch_ID = 1""")
        for row in cursor:
            self.tree.insert('', 0, values=(row[0], row[1], row[2], row[3]))


if __name__ == "__main__":
    app = Login(None)
    app.title('Batch registratie systeem')
    app.mainloop()
