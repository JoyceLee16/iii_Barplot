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
bb = []
for j in range(0,len(a)):
    a1 = com.loc[com['Family'] == a[j]].Num.tolist()
    # print(a1)
    a2 = com.loc[com['Family'] == a[j]].Count.tolist()
    # a1 = map(int, a1)
    # print(a2)
    aa = pd.DataFrame({'A': a1, 'B': a2})
    # print aa
    # print aa.shape


    for i in range(0, ll):
        c = aa.loc[(aa['A'] > 4000 * i) & (aa['A'] <= 4000 * (i + 1)), 'B'].sum()
        bb.append(c)
    #print len(bb)
#print len(bb)
tt = numpy.arange(5, 113, 1)
plt.plot(tt, bb[0:108], 'red', label="RAMNIT", alpha=3)
plt.plot(tt, bb[108:216], 'orange', label="TRACUR", alpha=3)
plt.plot(tt, bb[216:324], 'yellow', label="LOLLIPOP", alpha=3)
plt.plot(tt, bb[324:432], 'green', label="KELIHOS ver 3", alpha=3)
plt.plot(tt, bb[432:540], 'blue', label="SIMDA", alpha=3)
plt.plot(tt, bb[540:648], 'purple', label="KELIHOS ver 1", alpha=3)
plt.plot(tt, bb[648:756], 'gray', label="VUNDO", alpha=3)
plt.plot(tt, bb[756:864], 'brown', label="OBFUSCATOR.ACY", alpha=3)
plt.plot(tt, bb[864:972], 'black', label="GATAK", alpha=3)

plt.legend(bbox_to_anchor=(0.85, 1), loc=2, borderaxespad=0.)
plt.xticks(numpy.arange(5, 113, 1), labels, rotation='vertical')
plt.xlabel('Length')
plt.ylabel('Count')
plt.title('Line chart of label\'s length')
plt.ylim([0, 1200])
plt.xlim([4, 113])
plt.show()



