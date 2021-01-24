import matplotlib.pyplot as pyplot

pyplot.style.use("seaborn")
fig,ax=pyplot.subplots()
ax.scatter(2,4,s=2000,c='red')

ax.set_title("point fig",fontsize=22)
ax.set_xlabel("x",fontsize=22)
ax.set_ylabel("y",fontsize=22)

ax.tick_params(axis="both",which='major',labelsize=10)


pyplot.show()