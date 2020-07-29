#multiple charts of cases in June 2020

import matplotlib.pyplot as plt

State=('MH','RJ','UP','KL','PB','JK','HR','OR')
June=(39678,13456,19654,10879,12009,9100,8700,7800)
colors=['gold','yellowgreen','lightcoral','lightskyblue','grey','turquoise','pink','blue']
plt.figure(figsize=(15,5))

plt.subplot(131)
plt.plot(State,June,'m')
plt.title('Line chart')

plt.subplot(132)
plt.bar(State,June,color='y')
plt.title('Bar chart')

plt.subplot(133)
plt.pie(June,labels=State,autopct='%1.1f%%',colors=colors,shadow=True,startangle=120)
plt.title('Pie chart')
plt.suptitle('Multiple chart for cases in June')
plt.show()
