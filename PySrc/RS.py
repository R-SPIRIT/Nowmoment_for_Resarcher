import pandas as pd
import statsmodels.formula.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import numpy as np

import sys
from sklearn.linear_model import LinearRegression
import os, stat, glob  
import csv


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

def dataLinearegressionpara(csv,f):
    q=pd.read_csv(str(path)+str(ID)+str(inpath)+"UploadedFile"+str(inpath)+str(csv))
    lines=f.readlines()    
    for i in range(len(lines)):        
        if lines[i].split(';')[-3] == 'RS':
            y=q.iloc[:,int(lines[i].split(';')[-2].split(',')[0])]
            df=pd.DataFrame(y)
            for l in range(len(list(lines[i].split(';'))[-1].split(','))):
                b=q.iloc[:,int(lines[i].split(';')[-1].split(',')[l])]
                df[q.columns[int(lines[i].split(';')[-1].split(',')[l])]]=b
            X=df.iloc[:,1:]
            Y=df.iloc[:,0]
            model = sm.OLS(Y, X).fit()
            return(model.params)

def dataLinearegressionbse(csv,f):
    q=pd.read_csv(str(path)+str(ID)+str(inpath)+"UploadedFile"+str(inpath)+str(csv))
    lines=f.readlines()    
    for i in range(len(lines)):        
        if lines[i].split(';')[-3] == 'RS':
            y=q.iloc[:,int(lines[i].split(';')[-2].split(',')[0])]
            df=pd.DataFrame(y)
            for l in range(len(list(lines[i].split(';'))[-1].split(','))):
                b=q.iloc[:,int(lines[i].split(';')[-1].split(',')[l])]
                df[q.columns[int(lines[i].split(';')[-1].split(',')[l])]]=b
            X=df.iloc[:,1:]
            Y=df.iloc[:,0]
            model = sm.OLS(Y, X).fit()
            return(model.bse)

def dataLinearegressiontv(csv,f):
    q=pd.read_csv(str(path)+str(ID)+str(inpath)+"UploadedFile"+str(inpath)+str(csv))
    lines=f.readlines()    
    for i in range(len(lines)):        
        if lines[i].split(';')[-3] == 'RS':
            y=q.iloc[:,int(lines[i].split(';')[-2].split(',')[0])]
            df=pd.DataFrame(y)
            for l in range(len(list(lines[i].split(';'))[-1].split(','))):
                b=q.iloc[:,int(lines[i].split(';')[-1].split(',')[l])]
                df[q.columns[int(lines[i].split(';')[-1].split(',')[l])]]=b
            X=df.iloc[:,1:]
            Y=df.iloc[:,0]
            model = sm.OLS(Y, X).fit()
            return(model.tvalues)                

def dataLinearegressionpv(csv,f):
    q=pd.read_csv(str(path)+str(ID)+str(inpath)+"UploadedFile"+str(inpath)+str(csv))
    lines=f.readlines()    
    for i in range(len(lines)):        
        if lines[i].split(';')[-3] == 'RS':
            y=q.iloc[:,int(lines[i].split(';')[-2].split(',')[0])]
            df=pd.DataFrame(y)
            for l in range(len(list(lines[i].split(';'))[-1].split(','))):
                b=q.iloc[:,int(lines[i].split(';')[-1].split(',')[l])]
                df[q.columns[int(lines[i].split(';')[-1].split(',')[l])]]=b
            X=df.iloc[:,1:]
            Y=df.iloc[:,0]
            model = sm.OLS(Y, X).fit()
            return(model.pvalues)

def dataLinearegressionconf(csv,f):
    q=pd.read_csv(str(path)+str(ID)+str(inpath)+"UploadedFile"+str(inpath)+str(csv))
    lines=f.readlines()    
    for i in range(len(lines)):        
        if lines[i].split(';')[-3] == 'RS':
            y=q.iloc[:,int(lines[i].split(';')[-2].split(',')[0])]
            df=pd.DataFrame(y)
            for l in range(len(list(lines[i].split(';'))[-1].split(','))):
                b=q.iloc[:,int(lines[i].split(';')[-1].split(',')[l])]
                df[q.columns[int(lines[i].split(';')[-1].split(',')[l])]]=b
            X=df.iloc[:,1:]
            Y=df.iloc[:,0]            
            model = sm.OLS(Y, X).fit()            
            return(model.conf_int())

def dataLinearegression(csv,f):
    q=pd.read_csv(str(path)+str(ID)+str(inpath)+"UploadedFile"+str(inpath)+str(csv))
    lines=f.readlines()    
    for i in range(len(lines)):        
        if lines[i].split(';')[-3] == 'RS':
            y=q.iloc[:,int(lines[i].split(';')[-2].split(',')[0])]
            df=pd.DataFrame(y)
            for l in range(len(list(lines[i].split(';'))[-1].split(','))):
                b=q.iloc[:,int(lines[i].split(';')[-1].split(',')[l])]
                df[q.columns[int(lines[i].split(';')[-1].split(',')[l])]]=b
            X=df.iloc[:,1:]
            Y=df.iloc[:,0]
            model = sm.OLS(Y, X).fit()
            return(model.summary())        


#server
ID = str(sys.argv[1])

newtext=selectLatestid(ID)
wantid=open(str(path)+str(ID)+str(inpath)+"ColmIndex"+str(inpath)+str(newtext),'r')
lines=wantid.readlines()
ID=lines[0].split(';')[1]

columnindex=selectLatesttext(ID)
columnindexPath=str(path)+str(ID)+str(inpath)+"ColmIndex"+str(inpath)
csvPath=str(path)+str(ID)+str(inpath)+"UploadedFile"+str(inpath)
final=dataLinearegression(("ps1.csv"),open(columnindexPath+str(columnindex),'rt'))
summary = final.as_csv
summary = str(summary)

summaryPath=str(path)+str(ID)+str(inpath)+"SummaryRG"+str(inpath)

summarytxt = open(str(summaryPath)+str("summary.txt"), 'w')
summarytxt.write(summary)
summarytxt.close()
summarytxt = open(str(summaryPath)+str("summary.txt"), 'rt')
summLine=summarytxt.readlines()
important1=summLine[4:7]
summLine1=summarytxt.readlines()
important1=(','.join(important1))

str1='Adj.R-squared'

important1=important1.replace(' ', '').replace(':',",").replace('R-squared',',R-squared').replace('OLSAdj',',OLS').replace('LeastSquares',',LeastSquares').replace('F-statistic',',F-statistic').replace('\n','').split(',')

important1[7]=str(str1)
del important1[5]
del important1[9]

a=important1[0]+','+important1[1]+'\n'
b=important1[2]+','+important1[3]+'\n'
c=important1[4]+','+important1[5]+'\n'
d=important1[6]+','+important1[7]+'\n'
e=important1[8]+','+important1[9]+'\n'
f=important1[10]+','+important1[11]

important1=a+b+c+d+e+f
f = open(str(summaryPath)+str("summary1.txt"), 'w')      

f.write(important1)
f.close()

para=dataLinearegressionpara(str("ps1.csv"),open(columnindexPath+str(ID)+str('.txt'),'rt'))
paralist=list(para)
finalparalist=[round(paralist[i],4) for i in range(len(paralist))]
finalparalist.insert(0,'Coff')

bse=dataLinearegressionbse(str("ps1.csv"),open(columnindexPath+str(ID)+str('.txt'),'rt'))
bse
bselist=list(bse)
finalbselist=[round(bselist[i],4) for i in range(len(bselist))]
finalbselist.insert(0,'Std-Err')

tval=dataLinearegressiontv(str("ps1.csv"),open(columnindexPath+str(ID)+str('.txt'),'rt'))
tval
tvallist=list(tval)
finaltvallist=[round(tvallist[i],4) for i in range(len(tvallist))]
finaltvallist.insert(0,'t')

pval=tval=dataLinearegressionpv(str("ps1.csv"),open(columnindexPath+str(ID)+str('.txt'),'rt'))
pval
pvallist=list(pval)
fianlpvallist=[round(pvallist[i],4) for i in range(len(pvallist))]
fianlpvallist.insert(0,'P>|t|')

conf=dataLinearegressionconf(str("ps1.csv"),open(columnindexPath+str(ID)+str('.txt'),'rt'))
frontlist=[round(conf.iloc[i,0],4) for i in range(len(conf))]
frontlist.insert(0,0.025)
backlist=[round(conf.iloc[i,1],4) for i in range(len(conf))]
backlist.insert(0,0.975)

resultindex=list(conf.index)
resultindexlist=[resultindex[i] for i in range(len(resultindex))]
resultindexlist.insert(0,'Terms')
resultindexlist

finalparastr=','.join(str(v) for v in finalparalist) 
finalbseastr=','.join(str(v) for v in finalbselist) 
finaltvalstr=','.join(str(v) for v in finaltvallist) 
finalpvalstr=','.join(str(v) for v in fianlpvallist)
frontstr=','.join(str(v) for v in frontlist)
backstr=','.join(str(v) for v in backlist)
resultindexstr=','.join(str(v) for v in resultindexlist)

important2=resultindexstr[0:4]+resultindexstr[4:len(resultindexstr)]+';'+finalparastr[0:4]+finalparastr[4:len(finalparastr)]+';'+finalbseastr[0:7]+finalbseastr[7:len(finalbseastr)]+';'+finaltvalstr[0:1]+finaltvalstr[1:len(finaltvalstr)]+';'+finalpvalstr[0:5]+finalpvalstr[5:len(finalpvalstr)]+';'+frontstr[0:5]+frontstr[5:len(frontstr)]+';'+backstr[0:5]+backstr[5:len(backstr)]


important2=important2.replace(';','\n')

g = open(str(summaryPath)+str("summary2.txt"), 'w')
g.write(important2)
g.close()
