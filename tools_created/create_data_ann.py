import json 
import os

ann_name = "train"
classnames = {"classes": ["0", "1"]}
datalist = []
data_dir = "data_dir"

for file in os.listdir(data_dir):
    dictionary = {
        "img_path": file,
        "img_label": 0
    }
    datalist.append(dictionary)




ann_content = {
    "metainfo": classnames, 
    "data_list": datalist
}

json_object = json.dumps(ann_content, indent=4)

with open(ann_name + ".json", "w") as outfile:
    outfile.write(json_object)



