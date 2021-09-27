# jw_detection

1) git clone
    git clone https://github.com/zhuyuan7/jw_detection.git


2) jw_detection 으로 이동
    cd /home/joo/jw_detection


3) requirement 설치 
   pip install -r requirements.txt


4) train, valid, test image 다운받아 Ladder_Working_Dataset 폴더에 넣기


5) train, valid, test image의 주소 list 만들기
   data2text.py  파일 열어서 환경에 맞게 path 수정해줌.
    python data2text.py  


6) yaml을 이용해 data.yaml의 train set과 valid set의 경로를 바꾸어주도록 하자
    python data_yaml_dump.py --data /home/joo/jw_detection/Ladder_Working_Dataset/data.yaml  --traintxt /home/joo/jw_detection/Ladder_Working_Dataset/train.txt  --testtxt /home/joo/jw_detection/test.txt  --validtxt /home/joo/jw_detection/Ladder_Working_Dataset/valid.txt	


7) YOLOv5 s,m,l,x 모델 trian.py
     python train.py --img 416 --batch 16 --epochs 20 --data /home/joo/jw_detection/Ladder_Working_Dataset/data.yaml    --cfg  /home/joo/jw_detection/models/yolov5s.yaml  --weights yolov5s.pt  --cache  --name yolov5s

   train.py 을 실행하면 /home/joo/jw_detection/runs/train폴더가 생성됨. 
   train 폴더 안에  해당 모델의 weight가 생성됨.


8) YOLOv5s 모델의 train image --> detect.py
 
   python detect.py  --img 416 --conf 0.25  --source /home/joo/jw_detection/Ladder_Working_Dataset/train/images/  --weights '/home/joo/jw_detection/runs/train/yolov5s/weights/best.pt'  --name yolov5s_train

   detect.py 실행시, /home/joo/jw_detection/runs/detect 폴더가 생성됨.
   detect 폴더안에 object detection된 yolov5s_train파일들이 생성됨.


9) YOLOv5s 모델의 test하기 
   val.py에서 --task 'test' 로 설정하여 실행
   python val.py --img 416 --batch 16  --data '/home/joo/jw_detection/Ladder_Working_Dataset/data.yaml'  --weights '/home/joo/jw_detection/runs/train/yolov5s/weights/best.pt'    --task 'test'  --name yolov5s  
