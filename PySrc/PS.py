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

def colscaling(a,i):
    if i==1:
        a[a==a]=np.log(a)
        return a
    if i==2:
        a[a==a]=np.sqrt(a)
        return a

def colbinning(a,i,b,c,d):
    if i == 1:
        bins=np.linspace(b,c,d)
        a[a==a]=np.digitize(a,bins)
        return a
    else:
        a=a
        return a

def colper(a,i,b,c,d):
    if i == 1:
        a[(a >= b) & (a <= c)]= d
            
        return a
    else:
        a = a
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

def selectLatescsv(ID):  
    os.chdir(str(path)+str(ID)+str(inpath)+"UploadedFile")
    fileList = glob.glob('*')  
  
    latestMtime = 0  
    latestFileName = ''  
    for file in fileList:  
        mtime = os.stat(file)[stat.ST_MTIME]  
        if mtime > latestMtime:  
            latestMtime = mtime  
            latestFileName = file  
  
    return latestFileName 

def datascaling(csv,f):
    # q=pd.read_csv(str(path)+str(ID)+str(inpath)+"UploadedFile"+str(inpath)+str(csv),encoding ='utf-8')
    q = pd.read_csv(str(path) + str(ID) + str(inpath) + "UploadedFile" + str(inpath) + str(csv))
    lines=f.readlines()
    for i in range(len(lines)):
        a=list(lines[i].replace("\n","").split(';'))
        if a[2] == 'LO':
            c=a[3].split(",")
            d=a[4].split(",")
            if c == [''] :
                for j in range(len(d)):
                    colscaling(q.iloc[:,int(d[j])],1) 
            else:
                for j in range(len(d)):
                    colscaling(q.iloc[:,int(d[j])],1)
                    colper(q.iloc[:,int(d[j])],1,int(c[0]),int(c[1]),int(c[2]))
                    
                 
        elif a[2] == 'SR':
            c=a[3].split(",")
            d=a[4].split(",")
            if c == [''] :
                for j in range(len(d)):
                    colscaling(q.iloc[:,int(d[j])],2)
            else:
                for j in range(len(d)):
                    colscaling(q.iloc[:,int(d[j])],2)
                    colper(q.iloc[:,int(d[j])],1,int(c[0]),int(c[1]),int(c[2]))
                    
                 
        elif a[2] == 'DF':
            c=a[3].split(",")            
            d=a[4].split(",")
            if c == ['']:
                pass
            else:
                for j in range(len(d)):
                    colper(q.iloc[:,int(d[j])],1,int(c[0]),int(c[1]),int(c[2]))
               
    return q    

#server
#ID = str(sys.argv[1])
#local
ID = "test"
newtext=selectLatestid(ID)
wantid=open(str(path)+str(ID)+str(inpath)+"ColmIndex"+str(inpath)+str(newtext),'r')
lines=wantid.readlines()
ID=lines[0].split(';')[1]

columnindex=selectLatesttext(ID)
# csv=selectLatescsv(ID)
columnindexPath=str(path)+str(ID)+str(inpath)+"ColmIndex"+str(inpath)
csvPath=str(path)+str(ID)+str(inpath)+"UploadedFile"+str(inpath)
q3=datascaling(str("psload1.csv"),open(str(columnindexPath)+str(columnindex),'rt'))
q3.to_csv(csvPath+str("ps.csv")  , sep=',',encoding='euc-kr')
# q3.to_csv(csvPath+str("ps.csv")  , sep=',')

# fs = open(csvPath+str("ps.csv"), 'rt',encoding='euc-kr')
# fws = open(csvPath+str("ps1.csv"), 'w',encoding='utf-8')
fs = open(csvPath+str("ps.csv"), 'rt')
fws = open(csvPath+str("ps1.csv"), 'w')
liness = fs.readlines()
for lines in liness:
    jos=lines.split(",")[1:]    
    jos1=",".join(jos)
    fws.write(jos1)
fs.close()
fws.close()

##### tester ######

# server
testpath = "/usr/share/tomcat/webapps/temp/"

test_txt_read = open(str(path)+str(ID)+str(inpath)+"ColmIndex"+str(inpath)+str(newtext),'r')
test_read_lines = test_txt_read.readlines()

test_txt_append = open(testpath + "log.txt",'a')
dt = datetime.datetime.now()
pyname = "PS"
days = ("{}-{}-{} {}:{}:{}").format(dt.year,dt.month, dt.day, dt.hour ,dt.minute, dt.second)
info = ('{},{},{},{},{}'.format(7, pyname, ID, days ,test_read_lines))

test_txt_append.write(info)
test_txt_append.close()