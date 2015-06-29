from tkinter import *
import tkinter as tk

import os
imenik={}

class Imenik():
    def __init__(self, master):

        
        #seznami
        self.dodani=[]
        self.izbrisani=[]
          
        #Glavni menu
        menu = Menu(master)
        master.config(menu=menu)

        #podmenu File
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)

        #dodamo izbire v file_menu
        file_menu.add_command(label="Novo", command=self.novo)
        file_menu.add_command(label="Odpri", command=self.odpri)
        file_menu.add_command(label="Shrani", command=self.shrani)
        file_menu.add_separator()
        file_menu.add_command(label="Izhod", command=master.destroy)

        #podmenu Imenik
        imenik_menu = Menu(menu)
        menu.add_cascade(label="Zgodovina", menu=imenik_menu)

        #dodamo izbire v imenik_menu
        imenik_menu.add_command(label="Dodani", command=self.dodajanje)
        imenik_menu.add_command(label="Izbrisani", command=self.brisanje)
         
        #prva vrstica 
        self.ime = StringVar(master, value=" ")
        self.imeVar = StringVar()
        self.imePolje = Entry(master, textvariable=self.imeVar)
        self.imePolje.grid(row = 0, column = 1)
        znakIme = Label(text = "Ime       ")
        znakIme.grid(row = 0, column = 0)
     
        #druga vrstica
        self.telefon = IntVar(master, value=" ")
        self.telefonVar = StringVar()
        self.telefonPolje = Entry(master, textvariable=self.telefonVar)
        self.telefonPolje.grid(row = 1, column = 1)
        znakTelefon = Label(text = "Telefon ")
        znakTelefon.grid(row = 1, column = 0)

        #gumbi
        gumbDodaj = Button(master, text = "Dodaj", command = self.dodaj)
        gumbDodaj.grid(row=3, column = 0)

        gumbIzbrisi = Button(master, text = "Izbriši", command = self.izbrisi)
        gumbIzbrisi.grid(row=3, column = 1)

        gumbPrikazi = Button(master, text = "Prikaži", command = self.prikazi)
        gumbPrikazi.grid(row=3, column = 2)

        #listbox
        root.geometry("240x180+130+180")
        self.listbox = tk.Listbox(root, width=20, height=5)
        self.listbox.grid(row=2, column=1)
        
        #scrollbar
        self.yscroll = tk.Scrollbar(command=self.listbox.yview, orient=tk.VERTICAL)
        self.yscroll.grid(row=2, column=2, sticky="ns")
        self.listbox.configure(yscrollcommand=self.yscroll.set)
        
    def prikazi(self):
        if self.listbox.curselection():
            self.listbox.get(ACTIVE)
            self.telefonPolje.delete(0,END)
            self.imePolje.delete(0,END)
            self.imePolje.insert("end", self.listbox.get(self.listbox.curselection()))
            self.telefonPolje.insert("end", imenik[self.listbox.get(self.listbox.curselection())])
            
    def dodaj(self):
        imenik[self.imeVar.get()]=self.telefonVar.get()
        self.listbox.insert("end", self.imeVar.get())
        self.dodani.append(self.imeVar.get())
        
    def izbrisi(self):
        self.listbox.get(ACTIVE)
        self.izbrisani.append(self.listbox.get(self.listbox.curselection()))
        del imenik[self.listbox.get(self.listbox.curselection())]
        self.listbox.delete(0,END)        
        for ime in imenik.keys():
            self.listbox.insert("end", ime)

    def odpri(self):
        ime = filedialog.askopenfilename() 
        with open(ime, encoding="utf8") as f:
            for vrstica in f:
                kljuc, vrednost = vrstica.split()
                imenik[kljuc] = vrednost

        for ime in imenik.keys():
            self.listbox.insert("end", ime) 

    def shrani(self):
        ime = filedialog.asksaveasfilename()
        with open(ime, "wt", encoding="utf8") as f:
            for kljuc, vrednost in imenik.items():
                print(str(kljuc)+" "+str(vrednost),file=f)

    def dodajanje(self):
        popup = Toplevel()
        popup.title("Dodani")
        seznam1 = ""
        for ime in self.dodani:
            seznam1=seznam1+str(ime)+"\n"
        Message(popup,text=seznam1).pack()
        zapri = Button(popup, text="Zapri", command=popup.destroy)
        zapri.pack()

    def brisanje(self):
        popup = Toplevel()
        popup.title("Izbrisani")
        seznam2 = ""
        for ime in self.izbrisani:
            seznam2=seznam2+str(ime)+"\n"
        Message(popup, text=seznam2).pack()
        zapri = Button(popup, text="Zapri", command=popup.destroy)
        zapri.pack()

    def novo(self):
        self.imeVar.set("")
        self.telefonVar.set("")
        self.listbox.delete(0,END)
        imenik.clear()
        self.dodani=[]
        self.izbrisani=[]
                   
root = Tk(className=" Imenik ")
aplikacija = Imenik(root)
root.mainloop()

