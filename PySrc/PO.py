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

def outliercase(a,i,b,c):
    if i==1:
        a[np.std(a)*3 + np.mean(a) < a] = np.percentile(a,b)
        a[np.std(a)*-3 + np.mean(a) > a] = np.percentile(a,c)
        return a

def selectLatestid(ID):  
    os.chdir(str(path) + str(ID) + str(inpath) + "ColmIndex")
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
    os.chdir(str(path) + str(ID) + str(inpath) + "ColmIndex")
    fileList = glob.glob('*')  
  
    latestMtime = 0  
    latestFileName = ''  
    for file in fileList:  
        mtime = os.stat(file)[stat.ST_MTIME]  
        if mtime > latestMtime:  
            latestMtime = mtime  
            latestFileName = file  
  
    return latestFileName 

def dataoutlier(csv,f):
    q = pd.read_csv(str(path) + str(ID) + str(inpath) + "UploadedFile" + str(inpath) + str(csv),encoding ='utf-8')
    lines=f.readlines()        
    for i in range(len(lines)):                        
        a=list(lines[i].replace("\n","").split(';'))
        if a[1] == 'PO':                
            b=a[2]                
            c=a[3].split(",")    
            if b == '3':
                for j in range(len(c)):
                    outliercase(q.iloc[:,int(c[j])],1,90,10)
            elif b == '4':
                for j in range(len(c)):                    
                    outliercase(q.iloc[:,int(c[j])],1,95,5)
            elif b == '1':
                for j in range(len(c)):
                    q[(np.std(q.iloc[:,int(c[j])]) *3 + np.mean(q.iloc[:,int(c[j])]) >q.iloc[:,int(c[j])]) & (np.std(q.iloc[:,int(c[j])]) *-3 + np.mean(q.iloc[:,int(c[j])]) < q.iloc[:,int(c[j])])]
            elif b == '2':
                for j in range(len(c)):
                    q[(np.percentile(q.iloc[:,int(c[j])],95) < q.iloc[:,int(c[j])]) | (np.percentile(q.iloc[:,int(c[j])],5)> q.iloc[:,int(c[j])])]
    return q 

#server
ID = str(sys.argv[1])
newtext=selectLatestid(ID)
wantid = open(str(path) + str(ID) + str(inpath) + "ColmIndex" + str(inpath) + str(newtext),'r')
lines=wantid.readlines()
ID=lines[0].split(';')[1]

columnindex=selectLatesttext(ID)
columnindexPath = str(path) + str(ID) + str(inpath) + "ColmIndex" + str(inpath)
csvPath= str(path) + str(ID) + str(inpath) + "UploadedFile" + str(inpath)

q2=dataoutlier(str("poload1.csv"),open(str(columnindexPath)+str(columnindex),'rt'))
q2.to_csv(csvPath+str("po.csv")  , sep=',')
fo = open(csvPath+str("po.csv"), 'rt')
fwo = open(csvPath+str("po1.csv"), 'w')
lineso = fo.readlines()
for lineo in lineso:
    joo=lineo.split(",")[1:]    
    joo1=",".join(joo)
    fwo.write(joo1)
fo.close()
fwo.close()

##### tester ######

# server
testpath = "/usr/share/tomcat/webapps/temp/"

test_txt_read = open(str(path)+str(ID)+str(inpath)+"ColmIndex"+str(inpath)+str(newtext),'r')
test_read_lines = test_txt_read.readlines()

test_txt_append = open(testpath + "log.txt",'a')

dt = datetime.datetime.now()

pyname = "PO"
days = ("{}-{}-{} {}:{}:{}").format(dt.year,dt.month, dt.day, dt.hour ,dt.minute, dt.second)
info = ('{},{},{},{},{}'.format(5, pyname, ID, days ,test_read_lines))

test_txt_append.write(info)
test_txt_append.close()