import csv
import matplotlib.pyplot as plt
from datetime import datetime

'''由csv格式数据绘制折线图2'''

filename='data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader=csv.reader(f)
    head_row=next(f)
    print(head_row)

    highs=[]
    lows=[]
    dates=[]
    for row in reader:
        high=int(row[5])
        highs.append(high)

        low=int(row[6])
        lows.append(low)

        date=datetime.strptime(row[2],'%Y-%m-%d')
        dates.append(date)

#print(highs)
#print(dates)

plt.style.use("seaborn")
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.8,linewidth=1)#plot 日最高温
ax.plot(dates,lows,c='blue',alpha=0.8,linewidth=1)#plot 日最低温
ax.fill_between(dates,lows,highs,facecolor='purple',alpha=0.2)#填充颜色
ax.set_title('the hightest and lowest temprature in sitka in 2018'.title(),fontsize=20)
ax.set_xlabel('',fontsize=16)
ax.set_ylabel('temp(F)',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)


fig.autofmt_xdate()#使x刻度标签倾斜
plt.show()

