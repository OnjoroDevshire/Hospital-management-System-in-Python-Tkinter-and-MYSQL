from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import _mysql_connector

class Hospital:
    def __init__(self, root):
        self.root=root
        self.root.title('Hospital Management System')
        self.root.geometry('1540x800+0+0')

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose = StringVar()
        self.Lot = StringVar()
        self.Storageadvice = StringVar()
        self.Drivingusingmachine = StringVar()
        self.Howtousemedication = StringVar()
        self.patientid = StringVar()
        self.sideEffect = StringVar()
        self.Furtherinformation = StringVar()
        self.nooftablets=StringVar()
        self.issuedate = StringVar()
        self.expdate= StringVar()
        self.dailydose = StringVar()
        self.storage = StringVar()
        self.nhsNumber= StringVar()
        self.pname = StringVar()
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()



        Ibltitle=Label(self.root, bd=20, relief=RIDGE,
                       text='HOSPITAL MANAGEMENT SYSTEM', fg='red',
                       bg='white', font=('times new roman',16,'bold'))
        Ibltitle.pack(side=TOP, fill=X)

        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft= LabelFrame(Dataframe, bd=10,
                                  relief=RIDGE, padx=10,
                                  font=('times new roman',12, 'bold'), text='Patient Information')
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        Dataframeright=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                  font=('times new roman',12, 'bold'), text='Prescription')
        Dataframeright.place(x=990, y=5, width=460, height=350)

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)


        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)
        #Dataframeleft
        lblNameTablet=Label(DataframeLeft, textvariable=self.Nameoftablets,state='disabled', text="Name of Tablet",font=('times new roman',12, 'bold'), padx=2, pady=6 )
        lblNameTablet.grid(row=0, column=0)

        comNametablet= ttk.Combobox(DataframeLeft,font=('times new roman', 12, 'bold'),
                                    width=33)
        comNametablet['value']=('Nice', 'corona Vaccine', 'Acetaminophen', 'Adderal', 'malaria','Ativan')
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        lblref= Label(DataframeLeft, font=('arial', 12, 'bold'),text='Reference No:', padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref=Entry(DataframeLeft, font=('arial',13, 'bold', ),width=35)
        txtref.grid(row=1, column=1)

        lbldose = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Dose:', padx=2, pady=4)
        lbldose.grid(row=2, column=0, sticky=W)
        txtdose = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtdose.grid(row=2, column=1)

        lblnotab = Label(DataframeLeft, font=('arial', 12, 'bold'), text='No of Tablets:', padx=2, pady=4)
        lblnotab.grid(row=3, column=0, sticky=W)
        txtnotab = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtnotab.grid(row=3, column=1)

        lbllot = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Lot:', padx=2, pady=4)
        lbllot.grid(row=4, column=0, sticky=W)
        txtlot = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtlot.grid(row=4, column=1)

        lblissd = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Issue Date:', padx=2, pady=4)
        lblissd.grid(row=5, column=0, sticky=W)
        txtissd = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtissd.grid(row=5, column=1)

        lblexpd = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Exp Date:', padx=2, pady=4)
        lblexpd.grid(row=6, column=0, sticky=W)
        txtexpd = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtexpd.grid(row=6, column=1)

        lbldld = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Daily Dose:', padx=2, pady=4)
        lbldld.grid(row=7, column=0, sticky=W)
        txtdld = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtdld.grid(row=7, column=1)

        lblsde = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Side Effect:', padx=2, pady=4)
        lblsde.grid(row=8, column=0, sticky=W)
        txtsde = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtsde.grid(row=8, column=1)

        lblfinf = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Further Information:', padx=2, pady=4)
        lblfinf.grid(row=0, column=2, sticky=W)
        txtfinf = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtfinf.grid(row=0, column=3)

        lblbp = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Blood Pressure:', padx=2, pady=4)
        lblbp.grid(row=1, column=2, sticky=W)
        txtbp = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtbp.grid(row=1, column=3)

        lblsadv = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Storage Advice:', padx=2, pady=4)
        lblsadv.grid(row=2, column=2, sticky=W)
        txtsadv = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtsadv.grid(row=2, column=3)

        lblmed = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Medication:', padx=2, pady=4)
        lblmed.grid(row=3, column=2, sticky=W)
        txtmed = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtmed.grid(row=3, column=3)

        lblid = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Patient ID:', padx=2, pady=4)
        lblid.grid(row=4, column=2, sticky=W)
        txtid = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtid.grid(row=4, column=3)

        lblnhs = Label(DataframeLeft, font=('arial', 12, 'bold'), text='NHS No:', padx=2, pady=4)
        lblnhs.grid(row=5, column=2, sticky=W)
        txtnhs = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtnhs.grid(row=5, column=3)

        lblname = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Patient Name:', padx=2, pady=4)
        lblname.grid(row=6, column=2, sticky=W)
        txtname = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtname.grid(row=6, column=3)


        lbldob = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Date Of Birth:', padx=2, pady=4)
        lbldob.grid(row=7, column=2, sticky=W)
        txtdob = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtdob.grid(row=7, column=3)


        lbladd = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Patient Address:', padx=2, pady=4)
        lbladd.grid(row=8, column=2, sticky=W)
        txtadd = Entry(DataframeLeft, font=('arial', 13, 'bold',), width=35)
        txtadd.grid(row=8, column=3)

        self.textprescription = Text(Dataframeright, font=('arial', 12, 'bold'), width=45, height=16, padx=2, pady=6)
        self.textprescription.grid(row=0, column=0)

        btnprescription = Button(Buttonframe, text='Prescription', bg='green', fg='white', font=('arial', 12, 'bold'),
                                 width=23, height=16, padx=2, pady=2)
        btnprescription.grid(row=0, column=0)

        btnprescriptionData = Button(Buttonframe, text="Prescription Data", bg='green', fg='white', font=('arial', 12, 'bold'),
                                 width=23, height=16, padx=2, pady=2)
        btnprescriptionData.grid(row=0, column=1)  # Placed in column 0

        btnupdate = Button(Buttonframe, text="Update", bg='green', fg='white', font=('arial', 12, 'bold'),
                                 width=23, height=16, padx=2, pady=2)
        btnupdate.grid(row=0, column=2)

        btndelete = Button(Buttonframe, text="Delete", bg='green', fg='white', font=('arial', 12, 'bold'),
                                 width=23, height=16, padx=2, pady=2)
        btndelete.grid(row=0, column=3)  # Placed in co

        btnclear = Button(Buttonframe, text="Clear", bg='green', fg='white', font=('arial', 12, 'bold'),
                                 width=23, height=16, padx=2, pady=2)
        btnclear.grid(row=0, column=4)  # Placed in column 0

        btnexit = Button(Buttonframe, text="Exit", bg='green', fg='black', font=('arial', 12, 'bold'),
                                 width=23, height=16, padx=2, pady=2)
        btnexit.grid(row=0, column=5)  # Placed in column 0

        #table
        #scrollbar
        scroll_x = ttk.Scrollbar(Detailsframe, orient='horizontal')
        scroll_y = ttk.Scrollbar(Detailsframe, orient='vertical')
        self.hospital_table = ttk.Treeview(Detailsframe,
                                           columns=('nameoftablet', 'ref', 'dose', 'nooftablets', 'lot', 'issuedate',
                                                    'expdate', 'dailydose', 'storage', 'nhsnumber', 'pname', 'dob',
                                                    'address'), xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)
        scroll_x.pack(
            side=BOTTOM, fill=Y)
        scroll_y.pack(side=RIGHT, fill=X)
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading('nameoftablet', text='Name Of Tablet:')
        self.hospital_table.heading('ref', text='Reference No:')
        self.hospital_table.heading('dose', text='Dose')
        self.hospital_table.heading('nooftablets', text='No of Tablets:')
        self.hospital_table.heading('issuedate', text='Date of issue:')
        self.hospital_table.heading('expdate', text='Expiry Date:')
        self.hospital_table.heading('dailydose', text='Daily Dose:')
        self.hospital_table.heading('storage', text='Storage')
        self.hospital_table.heading('nhsnumber', text='NHS Number')
        self.hospital_table.heading('pname', text='Patient Name')
        self.hospital_table.heading('dob', text='Date of Birth')
        self.hospital_table.heading('address', text='Name Of Table')

        self.hospital_table['show']='headings'

        self.hospital_table.column('nameoftablet', width=100)
        self.hospital_table.column('ref', width=100)
        self.hospital_table.column('nooftablets', width=100)
        self.hospital_table.column('issuedate', width=100)
        self.hospital_table.column('expdate', width=100)
        self.hospital_table.column('dailydose', width=100)
        self.hospital_table.column('storage', width=100)
        self.hospital_table.column('nhsnumber', width=100)
        self.hospital_table.column('pname', width=100)
        self.hospital_table.column('dob', width=100)
        self.hospital_table.column('address', width=100)
        self.hospital_table.pack(fill=BOTH, expand=1)


def iPrescriptionData(self):
    if self.Nameoftablets.get()=="" or self.ref.get()=="":
        messagebox.showerror("Error", 'All fields are required')

    else:
        conn= _mysql_connector.connect(host='localhost', username="root", password="root",database="testdatabase")
        my_cursor=conn.cursor()


root=Tk()
ob= Hospital(root)
root.mainloop()
