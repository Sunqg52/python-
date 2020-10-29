import plotly.express as px
import json




# 处理json数据
file_path = "data/json/eq_data_1_day_m1.json"
with open(file_path) as f:
	all_data = json.load(f)

'''
# 将文件处理为易读
readable_file = 'data/json/reable_eq_data.json'
with open(readable_file, 'w') as f:
	json.dump(all_date, f, indent=4)			# 使用indent处理缩进
'''

# 提取相关联的数据
all_eq_dicts = all_data['features']

mags,titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']		# 提取properties部分下 mag键下的值
	title = eq_dict['properties']['title']
	lon = eq_dict['geometry']['coordinates'][0]	# [0] 提取列表中的第一个值
	lat = eq_dict['geometry']['coordinates'][1]
	mags.append(mag)
	titles.append(title)
	lats.append(lat)
	lons.append(lon)
'''
print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])
'''

# 绘制散点图
fig = px.scatter(
	x=lons,
	y=lats,
	labels={'x': '经度', 'y': '纬度'},
	range_x=[-200, 200],
	range_y=[-90, 90],
	width=800,
	height=800,
	title='全球地震散点图'
	)
fig.write_html('global_earthquakes.html')
fig.show()