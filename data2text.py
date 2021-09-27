	
# 이미지들의 주소 리스트로 만들어줌
train_img_list = glob('/home/joo/jw_detection/Ladder_Working_Dataset/train/images/*.jpg')
valid_img_list = glob('/home/joo/jw_detection/Ladder_Working_Dataset/valid/images/*.jpg')
test_img_list = glob('/home/joo/jw_detection/Ladder_Working_Dataset/test/images/*.jpg')
 
# 리스트를 txt파일로 생성
with open('/home/joo/jw_detection/Ladder_Working_Dataset/train.txt', 'w') as f:
	f.write('\n'.join(train_img_list) + '\n')
    
with open('/home/joo/jw_detection/Ladder_Working_Dataset/valid.txt', 'w') as f:
	f.write('\n'.join(valid_img_list) + '\n')

with open('/home/joo/jw_detection/Ladder_Working_Dataset/test.txt', 'w') as f:
	f.write('\n'.join(test_img_list) + '\n')
	
	

'''
	
from glob import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--trainimg', type=str, default='/home/joo/jw_detection/Ladder_Working_Dataset/train/images/*.jpg', help='train.img path')
parser.add_argument('--validimg', type=str, default='/home/joo/jw_detection/Ladder_Working_Dataset/valid/images/*.jpg', help='valid.img path')
parser.add_argument('--testimg', type=str, default='/home/joo/jw_detection/Ladder_Working_Dataset/test/images/*.jpg', help='test.img path')
parser.add_argument('--traintxt', type=str, default='/home/joo/jw_detection/Ladder_Working_Dataset/train.txt', help='train.txt path')
parser.add_argument('--validtxt', type=str, default='/home/joo/jw_detection/Ladder_Working_Dataset/valid.txt', help='valid.txt path')
parser.add_argument('--testtxt', type=str, default='/home/joo/jw_detection/Ladder_Working_Dataset/test.txt', help='test.txt path')
opt = parser.parse_args() 
 


# 이미지들의 주소 리스트로 만들어줌
train_img_list = glob(opt.trainimg)
valid_img_list = glob(opt.validimg)
test_img_list = glob(opt.testimg)
 
# 리스트를 txt파일로 생성
with open(opt.traintxt, 'w') as f:
	f.write('\n'.join(train_img_list) + '\n')
    
with open(opt.validtxt, 'w') as f:
	f.write('\n'.join(valid_img_list) + '\n')

with open(opt.testtxt, 'w') as f:
	f.write('\n'.join(test_img_list) + '\n')	
	
	
'''	
