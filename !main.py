import matplotlib.pyplot as pyplot

x=range(1,1001)
y=[i**2 for i in x]
pyplot.style.use("seaborn")#set style(before...)
fig,ax=pyplot.subplots()#传递地址



ax.set_title("square",fontsize=24)
ax.set_xlabel("val",fontsize=24)
ax.set_ylabel("val*val",fontsize=24)
ax.tick_params(axis="both",labelsize=8)

ax.plot(x, y,linewidth=1)#线段绘制
#ax.scatter(x,y,s=10)#描点绘制
ax.axis([0,1100,0,1100000])

print(pyplot.style.available)

pyplot.show()
