#yaml을 이용해 data.yaml의 train set과 valid set의 경로를 바꾸어주도록 하자

'''
python data_yaml_dump.py --data /home/joo/jw_detection/Ladder_Working_Dataset/data.yaml  --traintxt /home/joo/jw_detection/Ladder_Working_Dataset/train.txt
--testtxt /home/joo/jw_detection/Ladder_Working_Dataset/test.txt  --validtxt /home/joo/jw_detection/Ladder_Working_Dataset/valid.txt

'''

import yaml
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str, default='/home/joo/jw_detection/Ladder_Working_Dataset/data.yaml', help='dataset.yaml path')
parser.add_argument('--traintxt', type=str, default='/home/joo/jw_detection/Ladder_Working_Dataset/train.txt', help='train.txt path')
parser.add_argument('--validtxt', type=str, default='/home/joo/jw_detection/Ladder_Working_Dataset/valid.txt', help='valid.txt path')
parser.add_argument('--testtxt', type=str, default='/home/joo/jw_detection/Ladder_Working_Dataset/test.txt', help='test.txt path')
opt = parser.parse_args()


 
with open(opt.data, 'r') as f:
	data = yaml.load(f)
    
#print(data)
 
data['train'] = opt.traintxt
data['val'] = opt.validtxt
data['test'] = opt.testtxt

with open(opt.data, 'w') as f:
	yaml.dump(data, f)
    
print(data)

# Print classes
with open(opt.data) as f:
  d = yaml.load(f, Loader=yaml.FullLoader)  # dict
  for i, x in enumerate(d['names']):
    print(i, x)
