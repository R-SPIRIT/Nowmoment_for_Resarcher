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

#server
ID = str(sys.argv[1])
#local
# ID = str("test")
newtext=selectLatestid(ID)
wantid=open(str(path)+str(ID)+str(inpath)+"ColmIndex"+str(inpath)+str(newtext),'r')
lines=wantid.readlines()
ID=lines[0].split(';')[1]

columnindex=selectLatesttext(ID)
csv=selectLatescsv(ID)
columnindexPath=str(path)+str(ID)+str(inpath)+"ColmIndex"+str(inpath)
csvPath=str(path)+str(ID)+str(inpath)+"UploadedFile"+str(inpath)

origin=pd.read_csv(str(csv),encoding='cp949')

origin=origin.dropna(axis=1,how='all')

origin.to_csv(csvPath+str("rn.csv") , sep=',',encoding='euc-kr')  
f = open(csvPath+str("rn.csv"), 'rt')
fw = open(csvPath+str("rn1.csv"), 'w')
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
pyname = "RN"
days = ("{}-{}-{} {}:{}:{}").format(dt.year,dt.month, dt.day, dt.hour ,dt.minute, dt.second)
info = ('{},{},{},{},{}'.format(1, pyname, ID, days ,test_read_lines))

test_txt_append.write(info)
test_txt_append.close()
