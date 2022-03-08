"""
Calendario con python
        
Tengo que instalar la librería tkcalendar primero en el cmd
pip install tkcalendar    
"""
from tkinter import *
from tkcalendar import *
from datetime import date

root = Tk() 
root.title("Calendario")
root.geometry("500x350")
root.config(bg="gray")
 
fech_completa = date.today()  #Con esto saco la fecha actual y luego la separo en dia, mes y año
anyo= fech_completa.year
mes= fech_completa.month
dia= fech_completa.day

cal = Calendar(root, select= "day", year= anyo, month= mes, day= dia) #Selecciono la fecha actual en el calendario
cal.pack(pady=20, fill="both",expand="yes")

def fecha():
    Label.config(text="Fecha de hoy: " + cal.get_date())
    fec= cal.get_date()
    
    newWindow = Toplevel(root)
    newWindow.title("Agenda del calendario "+ fec)
    newWindow.geometry("500x350")
    newWindow.config(bg="gray")
       
    labelEx = Label(newWindow,text=fec)
    labelEx.pack(pady=20)
    #Label(newWindow, text=fec).pack()
    
    
    
Button = Button(root, text="Fecha", command=fecha)
Button.pack(pady=20)

Label = Label(root,text="")
Label.pack(pady=20)

root.mainloop()
