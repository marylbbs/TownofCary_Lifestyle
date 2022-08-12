import os
import pandas as pd
import tkinter as tk

from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime, timedelta
import lxml.etree as et

root = tk.Tk()
root.geometry("800x480")
frame = tk.Frame(root)
variable1 = tk.StringVar()
labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

labelTest.configure(text="Town of Cary P&A Lifestyle Benefit Proprietary File")

Plan_Year_start_Date = "20220701"
Filedate = datetime.today().strftime('%Y%m%d')
PPA_num = "999"
Client_num = "33159" #current number
#Client_num = " "  #oe number
Pay_Ded_Cycle = "M"

class MyClass(object):
    df_import = pd.DataFrame()
    df_header = pd.DataFrame()
    df_footer= pd.DataFrame()
    df_output = pd.DataFrame()
    File1 = ""
    File2 = ""

def OpenFile1():
    root = tk.Tk()
    root.filename = filedialog.askopenfilename(initialdir="C:\downloads", title="Select file",
                                               filetypes=(("xml files", "*.xml"), ("all files", "*.*")))
    MyClass.File1 = root.filename
    doc = et.parse(MyClass.File1)
    xsl = et.parse("TownofCary.xslt")

    # This replaces the , in the xml file
    root = doc.getroot()
    for elem in root.getiterator():
        try:
            elem.text = elem.text.replace(',', ' ')
        except AttributeError:
            pass
    for elem in root.iter('*'):
        try:
            if elem.text is not None:
                elem.text = elem.text.strip()
            if elem.tail is not None:
                elem.tail = elem.tail.strip()
        except AttributeError:
            pass
    # RUN TRANSFORMATION
    transformer = et.XSLT(xsl)
    result = transformer(doc)  # Subscribers - ees and dependents with ee enrollments

    # ALTERNATIVE: IMPORT DIRECTLY (BYPASS .TXT SAVE)
    from io import StringIO
    hp_df = pd.read_table(StringIO(str(result)),
                          index_col=False)  # Subscribers - ees and dependents with ee enrollments
    # hp_df.to_csv(r'P:\Proprietary and Manual files\Visual Basic\IBA\TOC\P&A\Flex\Testing\hp_df.csv', header=True,
    #               index=None, sep=',')
    df = hp_df['<?xml version="1.0"?>'].str.split(',', expand=True)
    df.columns = df.iloc[0]
    df = df.reindex(df.index.drop(0)).reset_index(drop=True)


    df.columns.name = None
    df['GroupID'] = df['GroupID'].str.strip()
    df_a = df[df['GroupID'].isin(["TOC"])].copy()  # dataframe contains ee demo, ee enrollments, deps demo
    df_1 = df_a[df_a['PlanStart'].isin(["2022-07-01T00:00:00"])].copy()
    df_lifestyle = df_1[df_1['Plan'].isin(['2022-2023 Reimbursement Program'])].copy()

    df_lifestyle["Pay Date"]=Filedate
    df_lifestyle['PPA Number'] = PPA_num
    df_lifestyle['Client Number'] = Client_num
    df_lifestyle['SSN'] = df_lifestyle['SSN'].replace('-','')
    df_lifestyle['DOB'] =  pd.to_datetime(df_lifestyle['DOB']).dt.strftime ('%Y%m%d')
    df_lifestyle['HireDate'] = pd.to_datetime(df_lifestyle['HireDate']).dt.strftime ('%Y%m%d')
    df_lifestyle['TerminationDate'] = pd.to_datetime(df_lifestyle['TerminationDate']).dt.strftime ('%Y%m%d')
    df_lifestyle['Pay_Ded_Cycle'] = Pay_Ded_Cycle
    df_lifestyle['Plan Year start Date'] = Plan_Year_start_Date
    df_lifestyle['Debit_Card'] = ""
    df_lifestyle['Lifestyle_Annual_Election']="3500"
    df_lifestyle['Lifestyle_PerPay_Amount']= "0"
    df_lifestyle['Lifestyle_Eff_Date'] = pd.to_datetime(df_lifestyle['StartDate']).dt.strftime ('%Y%m%d')
    df_lifestyle['Lifestyle_Term_Date'] = pd.to_datetime(df_lifestyle['End Date']).dt.strftime('%Y%m%d')
    df_lifestyle[['Filler1','Filler2','Filler3','Filler4','Filler5','Filler6','Filler7','Filler8','Filler9','Filler10','Filler11','Filler12','Filler13','Filler14','Filler15','Filler16','Filler17','Filler18','Filler19','Filler20','Filler21','Filler22','Filler23','Filler24','Filler25','Filler26','Filler27','Filler28','Filler29','Filler30','Filler31','Filler32','Filler33','Filler34','Filler35','Filler36','Filler37','Filler38','Filler39','Filler40','Filler41','Filler42','Filler43','Filler44','Filler45','Filler46','Filler47','Filler48','Filler49',]] = ""
    MyClass.df_output = pd.DataFrame(df_lifestyle,
                                     columns=['Pay Date','SSN','Level1Report','Level2Report','Level3Report','LastName',
                                              'FirstName','Middle','Address','Address2','City','State','ZIP','Email','DOB',
                                              'Pay_Ded_Cycle','EE ID','TerminationDate','EE Rehire Date','EE LOA Date',
                                              'EE Return LOA Date','Filler1','Filler2','Filler3','PPA Number','Client Number',
                                              'Filler4','Filler5','Filler6','Filler7','Filler8','Filler9','Filler10','Filler11',
                                              'Filler12','Filler13','Filler14','Filler15','Filler16','Filler17','Filler18','Filler19',
                                              'Filler20','Filler21','Filler22','Filler23','Filler24','Filler25','Filler26','Filler27',
                                              'Filler28','Filler29','Filler30','Filler31','Filler32','Filler33','Filler34','Filler35',
                                              'Filler36','Filler37','Filler38','Filler39','Filler40','Debit Card','Filler42','Filler43',
                                              'Filler44','Filler45','Filler46','Filler47','Filler48','Filler49','Corporate_Email',
                                              'Lifestyle_Eff_Date','Lifestyle_Annual_Election', 'Lifestyle_PerPay_Amount','Lifestyle_Term_Date'])
    #
    # MyClass.df_output.to_csv(
    #     r'S:\Shared Folders\Proprietary Files\Hub Chicago\Town of Cary\P&A Group\Lifestyle\Testing\MyClass.df_output_' + datetime.now().strftime(
    #         "%Y%m%d") + '.csv', header=True, index=None, sep=',')

    # Current client number is 33159
    #MyClass.df_output.to_csv(r'S:\Shared Folders\Proprietary Files\Hub Chicago\Town of Cary\P&A Group\Lifestyle\Testing\99933159_TEST_'+ datetime.now().strftime("%Y%m%d")+'.csv',header=False, index=None, sep=',')

    # OE client number is
    #MyClass.df_output.to_csv(r'S:\Shared Folders\Proprietary Files\Hub Chicago\Town of Cary\P&A Group\Flex\Export\999xxxxx_' + datetime.now().strftime("%Y%m%d") + '.csv', header=False, index=None, sep=',')
    trailer()
    button['text'] = "Upload XML file ✓"

def client_exit():
    MsgBox = tk.messagebox.askquestion("Exit application", "Are you sure you want to quit?", icon='warning')
    if MsgBox == 'yes':
        os.sys.exit()

def trailer():
    use_file = int(len(MyClass.df_output) + 1)
    data = {'Pay Date': [Filedate],
            'SSN': ["999999999"],
            'Level1Report': [use_file]}
    df_trailer = pd.DataFrame(data)
    print(df_trailer)
    file_to_write= 'S:\Shared Folders\Proprietary Files\Hub Chicago\Town of Cary\P&A Group\Lifestyle\Export\99933159_' + datetime.now().strftime( "%Y%m%d") + '.csv'
    # with open(file_to_write, 'a') as f:
    #     MyClass.df_output.to_csv(f,header=False)
    #     df_trailer.to_csv(f, header=False)
    list_of_dfs = [MyClass.df_output,df_trailer]
    with open(file_to_write, 'a',newline='') as f:
        for df in list_of_dfs:
            df.to_csv(f,header=False, index=None, sep=',')

frame.pack()

button = tk.Button(frame,
                   text="Upload XML file",
                   fg="white",
                   command=OpenFile1, bg='purple', pady=20,
                   width=25)

btn_exit = tk.Button(frame,
                   text="Exit",
                   fg="white",
                   command=client_exit, bg='purple', pady=20,
                   width=25)
button.pack()
btn_exit.pack()
root.mainloop()
