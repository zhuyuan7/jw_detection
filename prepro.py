from glob import glob
import yaml


# 이미지들의 주소 리스트로 만들어줌
train_img_list = glob('/home/joo/jw_detection/Ladder_Working_Dataset/test/images/*.jpg')
valid_img_list = glob('/home/joo/jw_detection/Ladder_Working_Dataset/valid/images/*.jpg')
test_img_list = glob('/home/joo/jw_detection/Ladder_Working_Dataset/test/images/*.jpg')
 
# 리스트를 txt파일로 생성
with open('/home/joo/jw_detection/Ladder_Working_Dataset/train.txt', 'w') as f:
	f.write('\n'.join(train_img_list) + '\n')
    
with open('/home/joo/jw_detection/Ladder_Working_Dataset/valid.txt', 'w') as f:
	f.write('\n'.join(valid_img_list) + '\n')

with open('/home/joo/jw_detection/Ladder_Working_Dataset/test.txt', 'w') as f:
	f.write('\n'.join(test_img_list) + '\n')
	


#data_yaml_dump.py
# data.yaml 파일에 train,val,test image text 경로 추가
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
def data2text():
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
	
	return data2text


def data_yaml_dump():
	with open("/home/joo/jw_detection/Ladder_Working_Dataset/data.yaml", 'r') as f:
		data = yaml.load(f)
		#print(data)
 
		data['train'] = "/home/joo/jw_detection/Ladder_Working_Dataset/train.txt"
		data['val'] = "/home/joo/jw_detection/Ladder_Working_Dataset/valid.txt"
		data['test'] = "/home/joo/jw_detection/Ladder_Working_Dataset/test.txt"

	with open("/home/joo/jw_detection/Ladder_Working_Dataset/data.yaml", 'w') as f:
		yaml.dump(data, f)
    
	print(data)
	return data_yaml_dump

'''
