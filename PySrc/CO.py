import sys
import pandas as pd
import statsmodels.formula.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import numpy as np
import statistics as st
import sys
from sklearn.linear_model import LinearRegression
import os, stat, glob
import csv


global path
# linux
path = "/usr/share/tomcat/webapps/"
inpath = "/"

def get_index_from_file(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith("PS"):
            index_string = line.split(";")[-1]
            index_string.replace(" ", "")
            return [int(x) for x in index_string.split(",")]
    return None


def calcorrelation(data_frame, column_type, columns_list):
    data = data_frame

    if columns_list != None:
        if column_type == "index":
            columns_list = [int(x) for x in columns_list]
            print("Coluns Index Selected")
            data = data_frame.iloc[:, columns_list]
        elif column_type == "names":
            data = data_frame[columns_list]
            print("Coluns Names Selected")

    return data.corr()
# sever
ID = str(sys.argv[1])
column_type = str(path)+str(ID)+str(inpath)+"ColmIndex"+str(inpath)+str(ID)+".txt"
columns_list = get_index_from_file(column_type)
column_type = "index"

csvPath=str(path)+str(ID)+str(inpath)+"UploadedFile"+str(inpath)+"ps1.csv"
data = pd.read_csv(csvPath)

data.fillna(0)

correlation_df = calcorrelation(data, column_type, columns_list)
output_file_name = csvPath=str(path)+str(ID)+str(inpath)+"SummaryRG"+str(inpath)+"correlation_result.txt"

correlation_df.to_csv(output_file_name)


# server
testpath = "/usr/share/tomcat/webapps/temp/"

test_txt_append = open(testpath + "log.txt",'a')
test_txt_append.close()
