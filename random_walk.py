from random import choice
import matplotlib.pyplot as pyplot
class RandomWalk:
    """产生随机漫步数据"""
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.x_value=[0]
        self.y_value=[0]
    
    def get_step(self):
        x_direction=choice([-1,1])
        x_distance=choice([0,1,2,3,4])
        return x_direction*x_distance
    
    def fill_walk(self):
        while len(self.x_value)<self.num_points:

            x_step=self.get_step()
            x=self.x_value[-1]+x_step
            self.x_value.append(x)

            y_step=self.get_step()
            y=self.y_value[-1]+y_step
            self.y_value.append(y)

            if x==0 and y==0:
                self.x_value.pop()
                self.y_value.pop()
        

if __name__=='__main__':
    
    
    rw=RandomWalk(5000)
    rw.fill_walk()
    pyplot.style.use("classic")
    fig,ax=pyplot.subplots(figsize=(15,9),dpi=128)
    point_nums=range(rw.num_points)
    color_change_list=range(rw.num_points)
    #ax.scatter(rw.x_value,rw.y_value,s=1,c=color_change_list,cmap=pyplot.cm.Reds,edgecolors='none')#散点图
    ax.plot(rw.x_value,rw.y_value,linewidth=1)#折线图
    ax.scatter(rw.x_value[0],rw.y_value[0],s=100,c='green',edgecolors='none')
    ax.scatter(rw.x_value[-1],rw.y_value[-1],s=100,c='red',edgecolors='none')
    ax.get_xaxis().set_visible(False)#hide axes
    ax.get_yaxis().set_visible(False)

    pyplot.show()
       
      

