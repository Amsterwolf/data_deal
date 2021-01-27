import requests
from plotly.graph_objs import Bar
from plotly import offline

'''访问api获取数据，绘制html图并设置超链接'''

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
r=requests.get(url,headers=headers)
print(f"status code:{r.status_code}")
response_dic=r.json()#转json格式
print(response_dic.keys())
print(f"cot:{response_dic['total_count']}")
print(f"len:{len(response_dic['items'])}")
response_items_dic=response_dic['items']
print()

rep_starts,rep_links=[],[]
lables=[]
print("the infomations about each repository:")
for res_dic in response_items_dic:
    name=res_dic['name']
    url=res_dic['html_url']
    rep_links.append(f"<a href='{url}'>{name}</a>")
    rep_starts.append(res_dic['stargazers_count'])
    lables.append(f"{res_dic['owner']['login']}<br />{res_dic['description']}")
    

data={
    'type':'bar',
    'x':rep_links,#设置超链接
    'y':rep_starts,
    'hovertext':lables,
    'marker':{
        'color':'blue',#填充色
        'line':{'width':1.5,'color':'rgb(25,25,25)'},#边框宽度和颜色
    },
    'opacity':0.6,#不透明度
}
   

my_layout={
    'title':"GitHub上最受欢迎的python项目",
    'titlefont':{'size':28},
    'xaxis':{
        'title':'repository_name',
        'titlefont':{'size':24},
        'tickfont':{'size':14},
    },
    'yaxis':{
        'title':'stars',
        'titlefont':{'size':24},
        'tickfont':{'size':14},
    },
}
fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repostories.html')