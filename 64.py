#line chart to compare cases of May and June
import matplotlib.pyplot as plt

State=('MH','Rajasthan','UP','Kerala','Punjab','Jharkhand','Haryana','Orisha')
May=(28078,17067,12670,19765,18566,5700,3450,2300)
June=(39678,13456,19654,10879,12009,9100,8700,7800)

plt.plot(State,May,marker='o',markerfacecolor='blue',markersize=12,color='skyblue', linewidth=4,label='May')
plt.plot(State,June,marker='', color='olive', linewidth=2, linestyle='dashed', label="June")
plt.title('Comparing cases in May and June')
plt.legend(loc=1)
plt.show()
