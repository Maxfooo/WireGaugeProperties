'''
Created on Oct 28, 2014

@author: Max Ruiz
'''

import re
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as mb




class WireGauge(Frame):

    file_opt = options = {}
    options['defaultextension'] = '.csv'
    options['filetypes'] = [('all files', '.*'), ('csv files', '.csv')]
    options['initialdir'] = 'C:\\'
    options['initialfile'] = 'awg.csv'
    options['title'] = 'Import AWG file'

    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title('Wire Gauge Info')
        self.pack()


        self.openAWGFile()

        self.initGUI()

    def initGUI(self):
        g = LabelFrame(self, text = 'Gauge')
        g.pack(side='left')

        self.gg = Listbox(g)

        for i in range(len(self.awg[0])):
            self.gg.insert(i, self.awg[0][i])

        sb = Scrollbar(g)
        sb.pack(side='left', fill=Y)
        sb.config(command=self.gg.yview)
        self.gg.pack()

        d_inch = LabelFrame(self, text='Diameter(inch)')
        self.di = StringVar()
        dI = Label(d_inch, textvariable=self.di, width=10)
        dI.pack()
        d_inch.pack(side='left')


        d_mm = LabelFrame(self,text='Diameter(mm)')
        self.dmm = StringVar()
        dMM = Label(d_mm, textvariable=self.dmm, width=10)
        dMM.pack()
        d_mm.pack(side='left')



        r_ft = LabelFrame(self,text='Ohms/1000ft')
        self.rft = StringVar()
        rFT = Label(r_ft, textvariable=self.rft, width=10)
        rFT.pack()
        r_ft.pack(side='left')



        r_km = LabelFrame(self, text='Ohms/1km')
        self.rkm = StringVar()
        rKM = Label(r_km, textvariable=self.rkm, width=10)
        rKM.pack()
        r_km.pack(side='left')



        a_c = LabelFrame(self, text='Max Amp-Chassis')
        self.ac = StringVar()
        aC = Label(a_c, textvariable=self.ac, width=10)
        aC.pack()
        a_c.pack(side='left')


        a_p = LabelFrame(self, text='Max Amp-Pwr')
        self.ap = StringVar()
        aP = Label(a_p, textvariable=self.ap, width=10)
        aP.pack()
        a_p.pack(side='left')



        m_f = LabelFrame(self, text='Max Freq 100% skin depth')
        self.mf = StringVar()
        mF = Label(m_f, textvariable=self.mf, width=10)
        mF.pack()
        m_f.pack(side='left')



        b_f = LabelFrame(self, text='Break Force (lb)')
        self.bf = StringVar()
        bF = Label(b_f, textvariable=self.bf, width=10)
        bF.pack()
        b_f.pack(side='left')


        self.gg.bind('<<ListboxSelect>>', self.updateFields)

    def updateFields(self, event):
        sel = self.gg.curselection()
        sel = re.findall(r'\(([\d]+),\)', str(sel))[0]
        ind = int(sel)

        self.di.set(self.awg[1][ind])
        self.dmm.set(self.awg[2][ind])
        self.rft.set(self.awg[3][ind])
        self.rkm.set(self.awg[4][ind])
        self.ac.set(self.awg[5][ind])
        self.ap.set(self.awg[6][ind])
        self.mf.set(self.awg[7][ind])
        self.bf.set(self.awg[8][ind])

    def openAWGFile(self):
        try:
            f = open('awg.csv', 'r')
            self.awg = []
            for line in f:
                self.awg.append(line.split(','))
            f.close
        except:
            mb.showinfo("File not in directory", "Please Import awg.csv file")
            f = filedialog.askopenfile(mode='r', **self.file_opt)
            self.awg = []
            for line in f:
                self.awg.append(line.split(','))
            f.close

root = Tk()
app = WireGauge(master=root)
app.mainloop()


