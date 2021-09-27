from glob import glob
 
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