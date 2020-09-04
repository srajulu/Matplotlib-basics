import matplotlib.pyplot as plt
import pandas as pd
from operator import add

States=['MH','Rajasthan','UP','Kerala','Punjab','Jharkhand','Haryana','Orisha']
May=[28078,17067,12670,19765,18566,5700,3450,2300]
June=[39678,13456,19654,10879,12009,9100,8700,7800]

#find total cases in each state
total=list(map(add,May,June))
#print(total)

d={'State':States}
df=pd.DataFrame(d,index=total)

df1=df.sort_index()
#print(df1)

colors = ['yellowgreen','yellowgreen','yellowgreen','yellowgreen','lightcoral','lightcoral','lightcoral','lightcoral']
plt.pie(df1.index,labels=df['State'],shadow=False,startangle=90,colors=colors,autopct='%1.1f%%')
plt.axis('equal')
plt.show()
