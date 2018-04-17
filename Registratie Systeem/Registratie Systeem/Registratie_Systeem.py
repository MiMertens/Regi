import MySQLdb
import tkinter
from tkinter import ttk

# connection details voor de database
try:
    conn = MySQLdb.connect(host='localhost',
                        port=3307,
                        database='sbsh',
                        user='root',
                        password='usbw')
except :
    print("Er is geen verbinding met de database")

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
        try:
            cursor.execute("SELECT Medewerker_ID, Wachtwoord, Functie FROM medewerker Where Medewerker_ID= %s AND Wachtwoord= %s",  (ID, WW))
            # Check of het wachtwoordt klopt
            for row in cursor:
                if row[1] == WW:  
                    self.Func = row[2]
                    # open het registratie scherm
                    self.app = Registratie(None)
                    self.app.title('Batch registratie systeem')
                    self.destroy()
        except :
            pass

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

        # label medewerker
        label_Medewerker = tkinter.Label(self, text='Medewerker ID: ', anchor="w")
        label_Medewerker.grid(column=0, row=4, sticky='EW', pady=5)

        # entry medewerker
        self.Entry_Medewerker = ttk.Entry(self)
        self.Entry_Medewerker.grid(column=1, row=4, sticky='EW', pady=5)

        # label apparaat
        label_Apparaat = tkinter.Label(self, text='Recycle: ', anchor="w")
        label_Apparaat.grid(column=0, row=5, sticky='EW', pady=5)

        # entry apparaat
        self.Entry_Apparaat = ttk.Entry(self)
        self.Entry_Apparaat.grid(column=1, row=5, sticky='EW', pady=5)

        # label aantal
        label_Aantal = tkinter.Label(self, text='Aantal: ', anchor="w")
        label_Aantal.grid(column=0, row=6, sticky='EW', pady=5)

        # entry apparaat
        self.Entry_Aantal = ttk.Entry(self)
        self.Entry_Aantal.grid(column=1, row=6, sticky='EW', pady=5)

        # label inkom datum
        label_inkom = tkinter.Label(self, text='Inkomst datum: ', anchor="w")
        label_inkom.grid(column=0, row=7, sticky='EW', pady=5)

        # entry inkom datum
        self.Entry_inkom = ttk.Entry(self)
        self.Entry_inkom.grid(column=1, row=7, sticky='EW', pady=5)

        # label sloop datum
        label_sloop = tkinter.Label(self, text='Sloop datum: ', anchor="w")
        label_sloop.grid(column=0, row=8, sticky='EW', pady=5)

        # entry sloop datum
        self.Entry_sloop = ttk.Entry(self)
        self.Entry_sloop.grid(column=1, row=8, sticky='EW', pady=5)

        # label voortgang
        label_voortgang = tkinter.Label(self, text='Voortgang: ', anchor="w")
        label_voortgang.grid(column=0, row=9, sticky='EW', pady=5)

        # entry voortgang
        self.Entry_voortgang = ttk.Entry(self)
        self.Entry_voortgang.grid(column=1, row=9, sticky='EW', pady=5)

        # Button set data
        button_set = tkinter.Button(self, text='Voeg batch toe', command=self.InsertBatch)
        button_set.grid(column=0, row=10, sticky='EW', pady=5, padx=5)

        # Button Get data
        button_update = tkinter.Button(self, text='Update batch', command=self.UpdateBatch)
        button_update.grid(column=1, row=10, sticky='EW', pady=5, padx=5)

        # Button haal lijst op
        button_lijst = tkinter.Button(self, text='Refresh lijst', command=self.Getbatch)
        button_lijst.grid(column=0, row=11, sticky='EW', pady=5, padx=5)

        # Button Details
        button_detail = tkinter.Button(self, text='Meer details', command=self.OpenDetail)
        button_detail.grid(column=1, row=11, sticky='EW', pady=5, padx=5)

        # Button Details
        button_Moverzicht = tkinter.Button(self, text='Medewerker Overzicht', command=self.MedewerkerOverzicht)
        button_Moverzicht.grid(column=0, row=12, columnspan=2, sticky='EW', pady=5, padx=5)

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
        self.app.title('Batch registratie systeem')

    def MedewerkerOverzicht(self):
        self.app = OverzichtMedewerkers(None)
        self.app.title('Medewerker overzicht')

    def EmtyEntrybox(self):
        self.Entry_Batch.config(state = 'normal')
        self.Entry_Batch.delete(0, 'end')
        self.Entry_Locatie.config(state = 'normal')
        self.Entry_Locatie.delete(0, 'end')
        self.Entry_Opslag.delete(0, 'end')
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
        try:
            # voer de query uit
            cursor.execute("""SELECT 
                                    b.Batch_ID, 
                                    concat(b.Locatie_ID,'. ',l.Adres),
                                    concat(b.Opslag_ID, '. ',o.Adres),
                                    o.Omschrijving,
                                    concat(b.Medewerker_ID, '. ',m.Naam),
                                    concat(b.Recycle_ID,'. ',r.Naam, ' ',r.Type ),
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
        except :
            pass

    def Getentry(self):
        self.batch = int(self.Entry_Batch.get())
        self.locatie = int(self.Entry_Locatie.get())
        self.opslag = int(self.Entry_Opslag.get())
        self.medewerker = int(self.Entry_Medewerker.get())
        self.recycle = int(self.Entry_Apparaat.get())
        self.aantal = int(self.Entry_Aantal.get()) 
        self.inkom = self.Entry_inkom.get()
        self.voortgang = self.Entry_voortgang.get()      

    def InsertBatch(self):
        self.Getentry()
            # voer de query uit
        cursor = conn.cursor()
        try:
            cursor.execute("""insert into batch (Locatie_ID, Opslag_ID, Medewerker_ID, Recycle_ID, Aantal, Inkomst_Datum, Voortgang) 
                                values (%s, %s, %s, %s, %s, %s, %s);""",(self.locatie, self.opslag, self.medewerker, self.recycle, self.aantal, self.inkom, self.voortgang))
            conn.commit()
            self.EmtyEntrybox()
        except :
            pass

    def UpdateBatch(self):
        self.Getentry()
            # voer de query uit
        cursor = conn.cursor()
        try:
            cursor.execute("""UPDATE batch 
                              SET Locatie_ID =%s, Opslag_ID =%s, Medewerker_ID =%s, Recycle_ID =%s, Aantal =%s, Inkomst_Datum =%s, Voortgang =%s
                              WHERE Batch_ID = %s
                              """,(self.locatie, self.opslag, self.medewerker, self.recycle, self.aantal, self.inkom, self.voortgang, self.batch))
            conn.commit()
            self.EmtyEntrybox()
        except :
            pass       

class details(tkinter.Tk):
    def __init__(self, parent):
        # constructor voor de tkinter
        tkinter.Tk.__init__(self, parent)
        # verwijzing naar de parent
        self.parent = parent
        # roep de methode initialize aan
        self.DetailWindow()

    def DetailWindow(self):
        # verdele het form in een gid voor het possitioneren van de gui elementen
        self.grid()
        # label naam
        label_Sys = tkinter.Label(self, text='Opbrengst Batch ', font=('Calibri', 20), anchor='e')
        label_Sys.grid(column=3, row=1, sticky='EW')

        # label batch
        label_Batch = tkinter.Label(self, text='Batch ID: ', anchor="w")
        label_Batch.grid(column=0, row=1, sticky='EW')

        # entry batch
        self.Entry_Batch = ttk.Entry(self)
        self.Entry_Batch.grid(column=1, row=1, sticky='EW')

        # label materiaal
        label_Materiaal = tkinter.Label(self, text='Materiaal ID: ', anchor="w")
        label_Materiaal.grid(column=0, row=2, sticky='EW')

        # entry materiaal
        self.Entry_Materiaal = ttk.Entry(self)
        self.Entry_Materiaal.grid(column=1, row=2, sticky='EW')

        # label killogram
        label_Kilo = tkinter.Label(self, text='Kilogram: ', anchor="w")
        label_Kilo.grid(column=0, row=3, sticky='EW')

        # entry killogram
        self.Entry_Kilo = ttk.Entry(self)
        self.Entry_Kilo.grid(column=1, row=3, sticky='EW')

        # label totaal
        label_Totaal = tkinter.Label(self, text='Totaal Waarde €: ', anchor="w")
        label_Totaal.grid(column=0, row=4, sticky='EW')

        # entry totaal
        self.Entry_Totaal = ttk.Entry(self, state='disabled')
        self.Entry_Totaal.grid(column=1, row=4, sticky='EW')

        # Button get details
        button_overzicht = tkinter.Button(self, text='Geef opbrengst weer', command=self.GetMateriaal)
        button_overzicht.grid(column=0, row=5, sticky='EW')

        # Button Insert
        button_Insert = tkinter.Button(self, text='Voeg materiaal toe', command=self.InsertMateriaal)
        button_Insert.grid(column=1, row=5, sticky='EW')

         # Set the treeview
        self.tree = ttk.Treeview(self, columns=('Materiaal', 'Recyclebaar', 'Kilogram', 'Waarde'))
        # naam/ positie waardes voor de treeview
        self.tree.heading('#1', text='Materiaal')
        self.tree.heading('#2', text='Recyclebaar')
        self.tree.heading('#3', text='Kilogram')
        self.tree.heading('#4', text='Waarde in €')
        self.tree.column('#0', minwidth=0)
        self.tree.column('#0', width=0)
        self.tree.grid(column=2, row=2, columnspan=4, rowspan=10, sticky='nsew', pady=5, padx=5)

    def GetMateriaal(self):
        # de treeview leegmaken
        for row in self.tree.get_children():
            self.tree.delete(row)

        batch = self.Entry_Batch.get()
        cursor = conn.cursor()
        # voer de query uit
        try:
            cursor.execute("""
                    SELECT
	                    m.Materiaalsoort,
                        m.Recyclebaar,
	                    b.Kilogram,
	                    round(d.Dagprijs * b.Kilogram,2) AS Waarde
                    FROM 
                        Batch_Materiaal b
	                    INNER JOIN Materiaal m ON b.Materiaal_ID = m.Materiaal_ID
	                    INNER JOIN Dagprijs d on m.Materiaal_ID = d.Materiaal_ID
                    Where 
	                    b.Batch_ID = %s""", (batch))
            for row in cursor:
                self.tree.insert('', 0, values=(row[0], row[1], row[2], row[3]))
        except :
            pass

        try:
            cursor.execute("""
                    SELECT
                        ROUND(SUM(d.Dagprijs * b.Kilogram),2)
                    FROM 
	                    Batch_Materiaal b
                        INNER JOIN Materiaal m ON b.Materiaal_ID = m.Materiaal_ID
                        INNER JOIN Dagprijs d on m.Materiaal_ID = d.Materiaal_ID
                    WHERE
	                    b.Batch_ID = %s""", (batch))
            for row in cursor:
                self.Entry_Totaal.config(state = 'normal')
                self.Entry_Totaal.delete(0, 'end')
                self.Entry_Totaal.insert(0, row[0])
                self.Entry_Totaal.config(state = 'disabled')
        except :
            pass
    def InsertMateriaal(self):
        Batch = int(self.Entry_Batch.get())
        Materiaal = int(self.Entry_Materiaal.get())
        Kilo = float(self.Entry_Kilo.get())
        cursor = conn.cursor()
        # voer de query uit
        try:
            cursor.execute("""insert into batch_materiaal (Batch_ID, Materiaal_ID, Kilogram) 
                                values (%s, %s, %s);""",(Batch, Materiaal, Kilo))
            conn.commit()
        except Exception as e:
            print(e)

class OverzichtMedewerkers(tkinter.Tk):
    def __init__(self, parent):
        # constructor voor de tkinter
        tkinter.Tk.__init__(self, parent)
        # verwijzing naar de parent
        self.parent = parent
        # roep de methode initialize aan
        self.Overzicht()

    def Overzicht(self):
        # verdele het form in een gid voor het possitioneren van de gui elementen
        self.grid()
        # label naam
        label_Overzicht = tkinter.Label(self, text='Opbrengsten medewerkers', font=('Calibri', 20), anchor='e')
        label_Overzicht.grid(column=2, row=1, sticky='EW')

        # label datum
        label_Datum = tkinter.Label(self, text='Datum: ', anchor="w")
        label_Datum.grid(column=0, row=2, sticky='EW')

        # entry datum
        self.Entry_Datum = ttk.Entry(self)
        self.Entry_Datum.grid(column=1, row=2, sticky='EW')

        # Button overzicht
        button_Overzicht = tkinter.Button(self, text='Geef overzicht weer')
        button_Overzicht.grid(column=1, row=3, sticky='EW')

        # Set the treeview
        self.tree = ttk.Treeview(self, columns=('Medewerker','Opbrengste'))
        # naam/ positie waardes voor de treeview
        self.tree.heading('#1', text='Medewerker')
        self.tree.heading('#2', text='Opbrengste in €')
        self.tree.column('#0', minwidth=0)
        self.tree.column('#0', width=0)
        self.tree.grid(column=2, row=2, columnspan=2, rowspan=10, sticky='nsew', pady=5, padx=5)

if __name__ == "__main__":
    app = Login(None)
    app.title('Batch registratie systeem')
    app.mainloop()
