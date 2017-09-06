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
ll = 431500/500
#print ll


g = numpy.arange(500, 431501, 500)
print len(g)
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
        c = aa.loc[(aa['A'] > 500 * i) & (aa['A'] <= 500 * (i + 1)), 'B'].sum()
        bb.append(c)
    #print len(bb)
    plt.bar(g, bb, alpha=0.5)
    plt.xlabel('Number')
    plt.ylabel('Count')
    plt.title(a[j] + ' Bar Plot')
    plt.ylim([0, 200])
    plt.xlim([0, 432000])
    plt.show()





