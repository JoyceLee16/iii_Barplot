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

with open('api.csv') as csvDataFile:
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
ll = 600/50

bb = []
g = numpy.arange(50, 601, 50)
for j in range(0,len(a)):
    a1 = com.loc[com['Family'] == a[j]].Num.tolist()
    #print(a1)
    a2 = com.loc[com['Family'] == a[j]].Count.tolist()
    # a1 = map(int, a1)
    aa = pd.DataFrame({'A': a1, 'B': a2})


    for i in range(1, ll):
        c = aa.loc[(aa['A'] > 50 * i) & (aa['A'] <= 50 * (i + 1)), 'B'].sum()
        bb.append(c)
    print bb,len(numpy.arange(5, 16, 1))

#print (bb)
tt = numpy.arange(5, 16, 1)
plt.plot(tt, bb[0:11], 'red', label="adware", alpha=3)
plt.plot(tt, bb[11:22], 'blue', label="packed", alpha=3)
plt.plot(tt, bb[22:33], 'green', label="trojan", alpha=3)
plt.plot(tt, bb[33:44], 'black', label="worm", alpha=3)
plt.legend(bbox_to_anchor=(0.9, 1), loc=2, borderaxespad=0.)

#plt.plot(tt, bb[0:11], 'red', tt, bb[11:22], 'blue', tt, bb[22:33], 'green', tt, bb[33:44], 'black',alpha=2)
labels = ['51-100', '101-150', '151-200', '201-250', '251-300', '301-350', '351-400',
          '401-450', '451-500', '501-550', '551-600']
plt.xticks(numpy.arange(5, 16, 1), labels, rotation=30)
plt.xlabel('Length')
plt.ylabel('Count')
plt.title('Line chart of label\'s length')
plt.ylim([0, 1700])
plt.xlim([4.5, 15.5])
plt.show()