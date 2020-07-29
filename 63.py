#pie chart to represent COVID cases in May
import matplotlib.pyplot as plt

State='MH','Rajasthan','UP','Kerala','Punjab','Jharkhand','Haryana','Orisha'
May=[28078,17067,12670,19765,18566,5700,3450,2300]

colors=['gold','yellowgreen','lightcoral','lightskyblue','grey','turquoise','pink','blue']

explode=(0.2,0,0,0,0,0,0,0)

plt.pie(May,explode=explode,labels=State,colors=colors,autopct='%1.1f%%',shadow=True,startangle=30)

plt.axis('equal')
plt.show()
