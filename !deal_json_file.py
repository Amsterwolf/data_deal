import json
import plotly.express as px
import pandas as pd
filename='data2/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data=json.load(f)

readable_filename='data2/readable_eq_data_30d.json'
#with open(readable_filename,'w') as f:
    #json.dump(all_eq_data,f,indent=4)

all_eq_dics=all_eq_data['features']
print(len(all_eq_dics))
mags,titles,lons,lats=[],[],[],[]
for dic in all_eq_dics:
    mag=dic['properties']['mag']
    title=dic['properties']['title']
    lon=dic['geometry']['coordinates'][0]
    lat=dic['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data_package=pd.DataFrame(
    data=zip(lons,lats,titles,mags),
    columns=['经度','纬度','命名','震级']
)

fig=px.scatter(
    data_frame=data_package,
    x='经度',
    y='纬度',
    title=all_eq_data['metadata']['title'],
    labels={'x':'lon','y':'lat'},
    width=800,
    height=800,
    range_x=[-200,200],
    range_y=[-90,90],
    size='震级',#根据震级决定点的大小
    size_max=10,
    color='震级',
    hover_name='命名',
    )
#fig.write_html('global_eq_24h.html')
fig.write_html('global_eq_30d.html')#生成html格式的图表
#fig.show()