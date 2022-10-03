from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

#   Global variables
name = ""
ecu_entry = ""
variant_entry = ""
supplier_entry = ""
protocol_entry = ""
cda_version = ""
mdp_version = ""
excelSheet = ""

protocols = [
    'CS-11825',
    'SD-12018',
    'CS.00053',
    'TFO 09009/02',
    'CS.00021',
    'CS.00101',
    'TFO 07287'
]

mdp_releases = ['0.3','0.65','0.95','1.0.3','1.0.6']
cda_releases = ['6.14.15x','6.15.12x','6.15.13x','6.15.14x','6.15.15x','6.15.16x']



def infoWindow(title, message):
    root = Tk()
    root.withdraw()
    root.update()
    messagebox.showinfo(title=title,
                        message=message)
    root.destroy()


def textFileGeneration():
    root = Tk()
    root.withdraw()
    root.update()
    messagebox.showinfo(title='Process complete', message='Text file generated.  Save file to a location on your drive.')
    root.destroy()


def processCompleted():
    root = Tk()
    root.withdraw()
    root.update()
    messagebox.showinfo(title='Process successful',message='Process is complete.  Close this window.')
    root.destroy()

def openExcelSheetSelectWindow(sheets):
    root = Tk()
    root.wm_title('Worksheet selection.')
    root.geometry('480x240')

    def okaySelected(*args):
        l = Label(root,text="{} selected.  Click close to continue".format(variable.get()))
        l.grid(row=1,pady=20,columnspan=2)

    def closedSelected(*args):
        global excelSheet
        excelSheet = variable.get()
        root.destroy()

    variable = StringVar(root)
    variable.set(sheets[2])

    L1 = Label(root,text='Workbook is open.  Select the worksheet and click ok.',background='blue',foreground='yellow')
    L1.grid(row=0,column=0,pady=20,padx=20)
    checklistSheet = OptionMenu(root,variable,*sheets)
    checklistSheet.grid(row=0,column=1,pady=20)

    okayButton = Button(root,text='Ok',command=okaySelected)
    okayButton.grid(row=2,column=0,pady=20)

    closeButton = Button(root,text='Close',command=closedSelected)
    closeButton.grid(row=2,column=1,pady=20)

    root.mainloop()

def openComplianceWindow():
    root = Tk()
    root.wm_title('Checklist Protocol Compliance Generator')
    root.geometry('880x320')

    def mainExit(*args):
        global ecu_entry
        ecu_entry = ""
        global variant_entry
        variant_entry = ""
        global supplier_entry
        supplier_entry = ""
        global protocol_entry
        protocol_entry = ""


    def closeWindow(*args):
        global ecu_entry
        ecu_entry = ecu.get()
        global variant_entry
        variant_entry = variant.get()
        global supplier_entry
        supplier_entry = customer.get()
        global protocol_entry
        protocol_entry = variable.get()
        global cda_version
        cda_version = cda_vers.get()
        global mdp_version
        mdp_version = mdp_vers.get()
        global name
        name = fullName.get()
        root.destroy()

    variable = StringVar(root)
    mdp_vers = StringVar(root)
    cda_vers = StringVar(root)
    variable.set(protocols[0])

    L1 = Label(root, text='ECU',background='blue',foreground='yellow')
    L1.grid(row=0,column=0,pady=10)
    ecu = Entry(root,width=50)
    ecu.grid(row=0,column=1,pady=10,padx=5)

    L2 = Label(root, text='Variant',background='blue',foreground='yellow')
    L2.grid(row=1,column=0,pady=10)
    variant = Entry(root,width=50)
    variant.grid(row=1,column=1,pady=10,padx=5)

    L3 = Label(root, text='Supplier',background='blue',foreground='yellow')
    L3.grid(row=2,column=0,pady=10)
    customer = Entry(root,width=50)
    customer.grid(row=2,column=1,pady=10)
    customer.insert(2, "Enter supplier and supplier id. (i.e Bosch - 0003)")

    L4 = Label(root, text="Select Protocol",background='blue',foreground='yellow')
    L4.grid(row=3,column=0,pady=10)
    protocolMenu = OptionMenu(root, variable, *protocols)
    protocolMenu.grid(row=3,column=1,pady=10)

    L5 = Label(root, text='MDP version (Optional)',background='blue',foreground='yellow')
    L5.grid(row=3,column=2,pady=10)
    mdp_version = OptionMenu(root,mdp_vers,*mdp_releases)
    mdp_version.grid(row=3,column=3,pady=10)

    L6 = Label(root, text='CDA version (Optional)', background='blue', foreground='yellow')
    L6.grid(row=4, column=0, pady=10)
    mdp_version = OptionMenu(root, cda_vers, *cda_releases)
    mdp_version.grid(row=4, column=1, pady=10)

    L7 = Label(root, text='Name (Optional)', background='blue', foreground='yellow')
    L7.grid(row=4, column=2, pady=10)
    fullName = Entry(root,width=25)
    fullName.grid(row=4, column=3, pady=10)

    Label(root, text="Click 'Ok' once all fields are filled in").grid(
        row=5, column=1
    )

    okay_button = Button(root, text="Ok", command=closeWindow)
    okay_button.grid(row=1,column=4,pady=10)

    root.protocol(name="WM_DELETE_WINDOW",func=mainExit())
    root.mainloop()
