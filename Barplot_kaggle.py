import os
import pandas as pd
import matplotlib.pyplot as plt

pathProg = 'C:\\Users\\gugu\\Desktop\\iii\\Archive'
os.chdir(pathProg)
import csv
import numpy


names = []
family = []
num = []

with open('kaggle_opcode.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        names.append(row[0])
        family.append(row[1])
        num.append(len(row[2:]))

data = pd.DataFrame({'Family':family[1:], 'Num':num[1:]})
#print data
com = data.groupby(['Family','Num']).size().reset_index().rename(columns={0:'Count'})
#print com
a = com.Family.unique()
#ll = numpy.arange(501, 1000, 500)
ll = 432000/4000
#print ll

labels = numpy.arange(4000, 432001, 4000)

for j in range(0,len(a)):
    a1 = com.loc[com['Family'] == a[j]].Num.tolist()
    # print(a1)
    a2 = com.loc[com['Family'] == a[j]].Count.tolist()
    # a1 = map(int, a1)
    # print(a2)
    aa = pd.DataFrame({'A': a1, 'B': a2})
    # print aa
    # print aa.shape

    bb = []
    for i in range(0, ll):
        c = aa.loc[(aa['A'] > 4000 * i) & (aa['A'] <= 4000 * (i + 1)), 'B'].sum()
        bb.append(c)
    #print len(bb)
    plt.bar(numpy.arange(5, 113, 1), bb, alpha=0.5)


    plt.xticks(numpy.arange(5.5, 113.5, 1), labels, rotation='vertical')
    plt.xlabel('Number')
    plt.ylabel('Count')
    plt.title(a[j] + ' Bar Plot')
    plt.ylim([0, 200])
    plt.xlim([4, 114])
    plt.show()
