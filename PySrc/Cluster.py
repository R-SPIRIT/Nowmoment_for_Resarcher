import os
import sys
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
import string
import MySQLdb
import MySQLdb.cursors
import csv
from pandas import DataFrame
import numpy as np  
import warnings

# server
ID = str(sys.argv[1])
val1 = str(sys.argv[2])
val2 = str(sys.argv[3])
val3 = str(sys.argv[4])

# linux
path = "/usr/share/tomcat/webapps/"
inpath = "/"

DB_HOST = "XXX.XXX.XXX.XXX"
DB_USER = "user"
DB_PWD = "pw"
DB_NAME = "nowmoment"

db_con = MySQLdb.connect(DB_HOST, DB_USER, DB_PWD, DB_NAME, cursorclass=MySQLdb.cursors.DictCursor)
cursor = db_con.cursor()
cursor.execute("SELECT "+val1+","+val2+" FROM TN_CLUSTER_INFO")
result = cursor.fetchall()

column1=[]
column2=[]

for i in range(len(result)):
    
    column1.append(result[i].get(val1))
    column2.append(result[i].get(val2))    
    
DF=DataFrame(columns=(val1,val2))
DF.iloc[:,0]=column1
DF.iloc[:,1]=column2

makegroup=pd.ExcelWriter(str(path) + str(ID) + str(inpath) + "UploadedFile" + str(inpath)+ 'cluster.xlsx')
DF.to_excel(makegroup)
makegroup.save()

data = pd.read_excel(str(path) + str(ID) + str(inpath) + "UploadedFile" + str(inpath)+ 'cluster.xlsx')

label_encoders = []
transformed_data_list = []
for column in data.columns:    
    lb = LabelBinarizer()
    data_out = pd.DataFrame(lb.fit_transform(data[column]))
    if data_out.shape[1] == 1:
        data_out.columns = [column]
    else :
        data_out.columns = [column + "_" + s for s in lb.classes_]
    transformed_data_list.append(data_out)
binary_data = pd.concat(transformed_data_list, axis=1)

df = binary_data

pca_components = PCA(n_components=2).fit_transform(df)

kmeans_n_clusters = [int(val3)]

estimators = []
titles = []
for kmeans_n_cluster in kmeans_n_clusters:
    titles.append("{} Clusters".format(kmeans_n_cluster))
    estimators.append(('k_means_cluster_{}'.format(kmeans_n_cluster),
                       KMeans(n_clusters=kmeans_n_cluster,random_state=111)))

for name, est in estimators:
    a=est.fit_transform(df)   
    labels = est.labels_

ax = plt.subplot(1, 1, 1)
ax.figure.set_size_inches(13, 6)  

b=["+","x","o","v","^","<",">","1"]
cmaps = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

for i in range(0, pca_components.shape[0]):
    if labels[i] == 0 : plt.scatter(pca_components[i,0], pca_components[i,1], c=cmaps[0], marker=b[0])
    elif labels[i] == 1 : plt.scatter(pca_components[i,0], pca_components[i,1], c=cmaps[1], marker=b[1])
    elif labels[i] == 2 : plt.scatter(pca_components[i,0], pca_components[i,1], c=cmaps[2], marker=b[2])
    elif labels[i] == 3 : plt.scatter(pca_components[i,0], pca_components[i,1], c=cmaps[3], marker=b[3])
    elif labels[i] == 4 : plt.scatter(pca_components[i,0], pca_components[i,1], c=cmaps[4], marker=b[4])
    elif labels[i] == 5 : plt.scatter(pca_components[i,0], pca_components[i,1], c=cmaps[5], marker=b[5])
    elif labels[i] == 6 : plt.scatter(pca_components[i,0], pca_components[i,1], c=cmaps[6], marker=b[6])


plt.title('Num of Clustering:' + val3)
plt.xlabel(val1)
plt.ylabel(val2)

plt.tight_layout(w_pad=4, h_pad=3)
plt.savefig(str(path)+str(ID)+str(inpath)+"SummaryRG"+str(inpath)+str('cluResult'), dpi=200)
plt.legend(loc='upper right')
plt.show()