'''Code for discretizing microarray and RNAseq data. Code needs cleaning up'''

import tkinter as tk
from tkinter import filedialog
import easygui
datatype = easygui.buttonbox(msg = 'Please enter an option',choices = ('Microarray data','RNAseq data'))
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

import pandas as p

File = p.read_csv(file_path,index_col = 0)

if datatype == 'Microarray data':
    Means = File.mean()
    Stds = File.std()
    stddev = float(easygui.enterbox("Enter a value for the number of standard deviations from mean: ","Standard Deviation factor"))
    listMeans = list()
    listStds = list()

    for i in Means:
        listMeans.append(i)
    for i in Stds:
        listStds.append(i)
    x =0
    listoflowers = list()
    ## Make list of lowerthresholds for each sample by subtracting half a standard deviation from the mean for each sample
    for i in listMeans:
        lower = i-(stddev*listStds[x])
        x = x+1
        listoflowers.append(lower)
    ## Make list of upperthresholds for each sample by adding half a standard deviation from the mean for each sample. Since x has already been used, use new variable y

    listofuppers = list()
    y = 0
    for number in listMeans:
        upper = number+(stddev*listStds[y])
        y = y+1
        listofuppers.append(upper)

    columnname = list()
    m = 0
    z = 0
    Biggerlist =  list()
    for columns in File:
        s = File.take([z],axis = 1)
        listofvalues = s.values
        ##print (listofvalues)
        z = z+1
        ##print(z)
        for i in listofvalues:
            if i < listoflowers[m]:
                columnname.append(0)
            elif i >listofuppers[m]:
                columnname.append(2)
            else:
                columnname.append(1)
        Biggerlist.append(columnname)
        columnname = list()
    headers = list(File.columns.values)
    Rownames = list(File.index)
    Finaltable = p.DataFrame(Biggerlist)
    Finaltable = Finaltable.transpose()

    Finaltable.index = Rownames
    Finaltable.columns = headers

## For RNAseq input data

elif datatype == 'RNAseq data':
    columnname = list()
    m = 0
    z = 0
    Biggerlist =  list()
    lower = float(easygui.enterbox("Enter a value for the number of FPKMs you would like to set as lower threshold: ","FPKMs"))
    percentilevalue = float(easygui.enterbox("Enter a value for the percentile you would like to set as upper threshold: ","FPKMs"))
    newstat = File.describe(percentiles = percentilevalue)
    n =0
    valuelist = list()
    for columns in File:
        s = File.take([z],axis = 1)
        listofvalues = s.values
        ##print (listofvalues)
        z = z+1
        actual_percentile_value_list = newstat.take([n],axis = 1)
        actual_values = actual_percentile_value_list.values
        percentile_value  = actual_values[5][0]
        ##print(z)
        for i in listofvalues:
            if i < lower:
                columnname.append(-1)
            elif i >percentile_value:
                columnname.append(1)
            else:
                columnname.append(0)
        n = n+1
        Biggerlist.append(columnname)
        columnname = list()
    headers = list(File.columns.values)
    Rownames = list(File.index)
    Finaltable = p.DataFrame(Biggerlist)
    Finaltable = Finaltable.transpose()

    Finaltable.index = Rownames
    Finaltable.columns = headers
##print (Finaltable)

##write out as csv
##Finaltable.to_csv('C:/Users/rharihar/Desktop/Exercises/testdiscrete1.csv',sep = ',',header = True,index= True,mode= 'w')

Finaltable.to_csv(filedialog.asksaveasfile())





        
