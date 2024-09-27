'''
    最终决定为了ID顺序不采取合并的方式
'''


import json

# phase = 'train'
phase = 'val'

# 读取第一个 JSON 文件
with open(f'../data/palmprint/annotations/Tongji_{phase}.json', 'r') as f1:
    json_data1 = json.load(f1)
# for item in json_data1["images"]:
#     item['file_name'] = item['file_name'][7:]

# 读取第二个 JSON 文件
# with open('./Tongji_val2.json', 'r') as f2:
with open(f'../data/palmprint/annotations/MPD_{phase}.json', 'r') as f2:
    json_data2 = json.load(f2)

first_batch_count =len( json_data1['images'])
for item in json_data2["images"]:
    item['id'] += first_batch_count
for item in json_data2['annotations']:
    item['id'] += first_batch_count
    item['image_id'] = item['id']
# 创建一个新的字典，合并两个 JSON 数据
merged_data = {
    "images": json_data1["images"] + json_data2["images"],
    "categories": json_data1["categories"] + json_data2["categories"],
    "annotations": json_data1["annotations"] + json_data2["annotations"]
}

# 将合并后的字典写入新的 JSON 文件
with open(f'merged_{phase}.json', 'w') as outfile:
    json.dump(merged_data, outfile, indent=4)