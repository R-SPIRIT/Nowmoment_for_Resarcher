import pandas as pd
import statsmodels.formula.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import numpy as np
import statistics as st
import sys
from sklearn.linear_model import LinearRegression
import os, stat, glob
import csv
import datetime

global path
# linux
path = "/usr/share/tomcat/webapps/"
inpath = "/"

def fillnull(a,i):
    if i==1:
        a[a !=a ]=a.fillna(a.mean())
        return a
    if i==2:
        a[a !=a ]=a.fillna(a.median())
        return a
    if i ==3:
        a[a !=a ]=a.fillna(a.min())
        return a
    if i==4:
        a[a !=a ]=a.fillna(a.max())
        return a
    if i==5:
        a[a !=a ]=a.fillna(0)
        return a

def selectLatestid(ID):  
    os.chdir(str(path)+str(ID)+str(inpath)+"ColmIndex")
    fileList = glob.glob('*')  
  
    latestMtime = 0  
    latestFileName = ''  
    for file in fileList:  
        mtime = os.stat(file)[stat.ST_MTIME]  
        if mtime > latestMtime:  
            latestMtime = mtime  
            latestFileName = file  
  
    return latestFileName 

def selectLatesttext(ID):  
    os.chdir(str(path)+str(ID)+str(inpath)+"ColmIndex")
    fileList = glob.glob('*')  
  
    latestMtime = 0  
    latestFileName = ''  
    for file in fileList:  
        mtime = os.stat(file)[stat.ST_MTIME]  
        if mtime > latestMtime:  
            latestMtime = mtime  
            latestFileName = file  
  
    return latestFileName 

def datafillnull(csv,f):
    q = pd.read_csv(str(path) + str(ID) + str(inpath) + "UploadedFile" + str(inpath) + str(csv))
    lines=f.readlines()  
    for i in range(len(lines)):
        a=list(lines[i].replace("\n","").split(';'))           
        if a[1] == 'PF': 
            b=a[2]
            c=a[3].split(",")                                    
            if b == '1':
                for j in range(len(c)):
                    fillnull(q.iloc[:,int(c[j])],1)
            elif b == '2':
                for j in range(len(c)):
                    fillnull(q.iloc[:,int(c[j])],2)                             
                   
            elif b == '3':
                for j in range(len(c)):
                    fillnull(q.iloc[:,int(c[j])],3)  
                   
            elif b == '4':
                for j in range(len(c)):
                    fillnull(q.iloc[:,int(c[j])],4)
                  
            elif b == '5':
                for j in range(len(c)):
                    fillnull(q.iloc[:,int(c[j])],5)

    return  q    

def selectcolumn(df,f):
    lines=f.readlines()
    new = pd.DataFrame()
    for i in range(len(lines)):
        a=list(lines[i].replace("\n","").split(';'))
        b=a[2]
        c=a[3].split(",")  
        if a[1] == 'PF':              
            if b == '1':
                for j in range(len(c)):                  
                    a=df.iloc[:,int(c[j])]
                    new[df.columns[int(c[j])]]=a
                    new1= new
            elif b == '2':
                for j in range(len(c)):
                    a=df.iloc[:,int(c[j])]
                    new[df.columns[int(c[j])]]=a
                    new2=new
            elif b == '3':
                for j in range(len(c)):
                    a=df.iloc[:,int(c[j])]
                    new[df.columns[int(c[j])]]=a
                    new3=new
            elif b == '4':
                for j in range(len(c)):
                    a=df.iloc[:,int(c[j])]
                    new[df.columns[int(c[j])]]=a
                    new4=new   
            elif b == '5':
                for j in range(len(c)):
                    a=df.iloc[:,int(c[j])]
                    new[df.columns[int(c[j])]]=a
                    new5=new  
    return new
#server
ID = str(sys.argv[1])
newtext=selectLatestid(ID)
wantid=open(str(path)+str(ID)+str(inpath)+"ColmIndex"+str(inpath)+str(newtext),'r')
lines=wantid.readlines()
ID=lines[0].split(';')[1]

columnindex=selectLatesttext(ID)
columnindexPath=str(path)+str(ID)+str(inpath)+"ColmIndex"+str(inpath)
csvPath=str(path)+str(ID)+str(inpath)+"UploadedFile"+str(inpath)

q1=datafillnull(str("pfload1.csv"), open(str(columnindexPath)+str(columnindex),'rt'))
q1=selectcolumn(q1, open(str(columnindexPath)+str(columnindex),'rt'))
q1.to_csv(csvPath+str("pf.csv"), sep=',',encoding='euc-kr')

f = open(csvPath+str("pf.csv"), 'rt')
fw = open(csvPath+str("pf1.csv"), 'w')

lines = f.readlines()
for line in lines:
    jo=line.split(",")[1:]
    jo1=",".join(jo)
    fw.write(jo1)
f.close()
fw.close()

##### tester ######
# server
testpath = "/usr/share/tomcat/webapps/temp/"

test_txt_read = open(str(path)+str(ID)+str(inpath)+"ColmIndex"+str(inpath)+str(newtext),'r')
test_read_lines = test_txt_read.readlines()

test_txt_append = open(testpath + "log.txt",'a')

dt = datetime.datetime.now()
pyname = "PF"
days = ("{}-{}-{} {}:{}:{}").format(dt.year,dt.month, dt.day, dt.hour ,dt.minute, dt.second)
info = ('{},{},{},{},{}'.format(3, pyname, ID, days ,test_read_lines))

test_txt_append.write(info)
test_txt_append.close()
