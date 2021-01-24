from random import randint

class Die:
    def __init__(self,num_sides=6):
        self.num_sides=num_sides
    
    def roll(self):
        return randint(1,self.num_sides)

if __name__=="__main__":
    die=Die()
    alist=[]
    '''cot_dic={}
    for i in range(1,die.num_sides+1):
        cot_dic[i]=0'''
    frequencies=[]
    for i in range(3000):
        x=die.roll()
        alist.append(x)
    for i in range(1,die.num_sides+1):
        frequencies.append(alist.count(i))

    print(alist)
    print(frequencies)
   
