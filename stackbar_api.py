import os
import pandas as pd
import matplotlib.pyplot as plt

pathProg = 'C:\\Users\\gugu\\Desktop\\iii\\Archive'
os.chdir(pathProg)
import csv
import numpy as np




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
g = np.arange(50, 601, 50)
for j in range(0,len(a)):
    a1 = com.loc[com['Family'] == a[j]].Num.tolist()
    #print(a1)
    a2 = com.loc[com['Family'] == a[j]].Count.tolist()
    # a1 = map(int, a1)
    aa = pd.DataFrame({'A': a1, 'B': a2})


    for i in range(1, ll):
        c = aa.loc[(aa['A'] > 50 * i) & (aa['A'] <= 50 * (i + 1)), 'B'].sum()
        bb.append(c)
    #print bb,len(numpy.arange(5, 16, 1))

tt = np.arange(5, 16, 1)
width = 0.3      # the width of the bars: can also be len(x) sequence
p1 = plt.bar(tt, bb[0:11], width, color=(1.0,0.5,0.62))
p2 = plt.bar(tt, bb[11:22], width, bottom=bb[0:11], color=(0.2588,0.4433,1.0))
p3 = plt.bar(tt, bb[22:33], width, bottom=np.array(bb[0:11])+np.array(bb[11:22]), color='green')
p4 = plt.bar(tt, bb[33:44], width,  bottom=np.array(bb[0:11])+np.array(bb[11:22])+np.array(bb[22:33]), color='black')

plt.xlabel('Length')
plt.ylabel('Count')
plt.title('Stacked Bar Chart of label\'s length')
labels = ['51-100', '101-150', '151-200', '201-250', '251-300', '301-350', '351-400',
          '401-450', '451-500', '501-550', '551-600']
plt.xticks(np.arange(5.25, 16.25, 1), labels, rotation=0)
#plt.legend((p1[0], p2[0], p3[0], p4[0]), ('adware', 'packed', 'trojan', 'worm'))
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('adware', 'packed', 'trojan', 'worm'))

plt.ylim([0, 2400])
plt.xlim([4.5, 15.5])
plt.show()


