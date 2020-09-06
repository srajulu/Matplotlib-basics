#bar chart to represent COVID cases in May and June

import numpy as np
import matplotlib.pyplot as plt

#data to plot
n=8
State=('MH','Rajasthan','UP','Kerala','Punjab','Jharkhand','Haryana','Orisha')
May=(28078,17067,12670,19765,18566,5700,3450,2300)
June=(39678,13456,19654,10879,12009,9100,8700,7800)

#create a plot
y_pos=np.arange(n)
barwidth=0.35
opacity=0.8

rects1=plt.bar(y_pos,May,barwidth,alpha=opacity,color='b',label='May')

rects1=plt.bar(y_pos+barwidth,June,barwidth,alpha=opacity,color='g',label='June')

plt.xlabel('State -->')
plt.ylabel('Cases -->')
plt.title('Covid cases in May and June')
plt.xticks(y_pos+barwidth,State)

plt.legend()

plt.show()




