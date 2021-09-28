#yaml을 이용해 data.yaml의 train set과 valid set의 경로를 바꾸어주도록 하자

'''
python data_yaml_dump.py 

'''

import yaml

 
with open("/home/joo/jw_detection/Ladder_Working_Dataset/data.yaml", 'r') as f:
	data = yaml.load(f)
    
#print(data)
 
data['train'] = "/home/joo/jw_detection/Ladder_Working_Dataset/train.txt"
data['val'] = "/home/joo/jw_detection/Ladder_Working_Dataset/valid.txt"
data['test'] = "/home/joo/jw_detection/Ladder_Working_Dataset/test.txt"

with open("/home/joo/jw_detection/Ladder_Working_Dataset/data.yaml", 'w') as f:
	yaml.dump(data, f)
    
print(data)


'''
# Print classes
with open(opt.data) as f:
  d = yaml.load(f, Loader=yaml.FullLoader)  # dict
  for i, x in enumerate(d['names']):
    print(i, x)
'''
