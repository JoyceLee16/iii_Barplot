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

#print(names)
#print(family)

#print len(num)
#print names
#print family
#print num

data = pd.DataFrame({'Family':family[1:], 'Num':num[1:]})
#print data
com = data.groupby(['Family','Num']).size().reset_index().rename(columns={0:'Count'})
#print com
a = com.Family.unique()
ll = 600/50


g = numpy.arange(50, 601, 50)
for j in range(0,len(a)):
    #b = pd.DataFrame(com.loc[com['Family'] == a[j]])
    #b.to_csv(a[j] + '.csv', index=False, header=False)
    a1 = com.loc[com['Family'] == a[j]].Num.tolist()
    #print(a1)
    a2 = com.loc[com['Family'] == a[j]].Count.tolist()
    # a1 = map(int, a1)
    aa = pd.DataFrame({'A': a1, 'B': a2})

    bb = []
    for i in range(1, ll):
        c = aa.loc[(aa['A'] > 50 * i) & (aa['A'] <= 50 * (i + 1)), 'B'].sum()
        bb.append(c)
    #print bb,len(numpy.arange(75, 576, 50))
    plt.bar(numpy.arange(5, 16, 1), bb, alpha=0.5)
    labels = ['51-100', '101-150', '151-200', '201-250', '251-300', '301-350', '351-400',
              '401-450', '451-500', '501-550', '551-600']
    plt.xticks(numpy.arange(5.5, 16.5, 1), labels, rotation=30)
    plt.xlabel('Number')
    plt.ylabel('Count')
    plt.title(a[j] + ' Bar Plot')
    plt.ylim([0, 400])
    plt.xlim([4.5, 16])
    plt.show()



#print(a2)
#plt.figure()
# df2 = pd.DataFrame(a2)
# df2.index = a1
# print df2
# df2 = a1.to_frame().join(a2.to_frame())


#from bokeh.charts import Bar, output_file, show
#p=Bar(a2, a1)
#output_file("bar.html")
#show(p)
