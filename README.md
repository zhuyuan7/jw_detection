# jw_detection

1) git clone<br>
    git clone https://github.com/zhuyuan7/jw_detection.git

<br>

2) jw_detection 으로 이동<br>
    cd /home/joo/jw_detection


<br>

3) requirement 설치<br> 
   pip install -r requirements.txt


<br>

4) train, valid, test image 다운받아 Ladder_Working_Dataset 폴더에 넣기


<br>

5) train, valid, test image의 주소 list 만들기<br>
   data2text.py  파일 열어서 환경에 맞게 path 수정해줌.
    python data2text.py  


<br>

6) yaml을 이용해 data.yaml의 train set과 valid set의 경로를 바꾸어주도록 하자<br>

    ```bash
    python data_yaml_dump.py --data /home/joo/jw_detection/Ladder_Working_Dataset/data.yaml  --traintxt /home/joo/jw_detection/Ladder_Working_Dataset/train.txt  --testtxt /home/joo/jw_detection/test.txt  --validtxt /home/joo/jw_detection/Ladder_Working_Dataset/valid.txt	
    ```



<br>

7) YOLOv5 s,m,l,x 모델 trian.py<br>
<img src="https://github.com/zhuyuan7/jw_detection/blob/a4eb3e3e121e022ab4ced3c1f7e2d6cbd305b251/yolo.png"></a>


python train.py --img 416 --batch 16 --epochs 20 --data /home/joo/jw_detection/Ladder_Working_Dataset/data.yaml    --cfg  /home/joo/jw_detection/models/yolov5s.yaml  --weights yolov5s.pt  --cache  --name yolov5s


   train.py 을 실행하면 /home/joo/jw_detection/runs/train폴더가 생성됨. <br>
   train 폴더 안에  해당 모델의 weight가 생성됨.


<br>

8) YOLOv5s 모델의 train image --> detect.py<br>


python detect.py  --img 416 --conf 0.25  --source /home/joo/jw_detection/Ladder_Working_Dataset/train/images/  --weights '/home/joo/jw_detection/runs/train/yolov5s/weights/best.pt'  --name yolov5s_train


   detect.py 실행시, /home/joo/jw_detection/runs/detect 폴더가 생성됨. <br>
   detect 폴더안에 object detection된 yolov5s_train파일들이 생성됨.


<br>

9) YOLOv5s 모델의 test하기<br> 
   val.py에서 --task 'test' 로 설정하여 실행


   python val.py --img 416 --batch 16  --data '/home/joo/jw_detection/Ladder_Working_Dataset/data.yaml'  --weights '/home/joo/jw_detection/runs/train/yolov5s/weights/best.pt'    --task 'test'  --name yolov5s

