from die import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline

'''模拟骰子结果，绘制条形图'''

die=Die()
die2=Die(10)
alist=[die.roll()+die2.roll() for i in range(3000)]#列表解析
frequencies=[]
'''for i in range(3000):
    x=die.roll()
    x2=die2.roll()
    alist.append(x+x2)'''

max_result=die.num_sides+die2.num_sides
for i in range(1,max_result+1):
    frequencies.append(alist.count(i))


x_value=[i for i in range(1,max_result+1)]
y_value=frequencies
data=[Bar(x=x_value,y=y_value)]

my_layout=Layout(title='the result of roll two dice'.title(),xaxis={'title':'result','dtick':1},yaxis={'title':'the fre of result'})


offline.plot({'data':data,'layout':my_layout},filename="d6_d10.html")