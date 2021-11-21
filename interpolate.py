import pandas as pd

data=pd.read_excel('GW_data.xlsx')
l=[]
s=[]
# place=data['Name'].unique()
# # print(len(place))
print(data[data['Level'].isna()])

# for i in place:
#     t=data[data['Name']==i]['Level']
#     t=t.interpolate(method='linear',)
#     l.extend(t.values.tolist())
#     t=data[data['Name']==i]['Level']
#     t=t.interpolate(method='cubicspline',)
#     s.extend(t.values.tolist())

# d=pd.DataFrame({'Linear':l,'Spline':s})

# # d=pd.get_dummies(data.soil_depth,prefix='SD')

# d.to_excel('interpolate.xlsx')
