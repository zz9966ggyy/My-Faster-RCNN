
import cv2 

videoCapture = cv2.VideoCapture()
videoCapture.open("D:\\bishe\\faster-rcnn\\faster-rcnn-tensorflow-python3-master\\video\pigs.mp4")

fps = videoCapture.get(cv2.CAP_PROP_FPS)
frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
#fps是帧率，意思是每一秒刷新图片的数量，frames是一整段视频中总的图片数量。
print("fps=",fps,"frames=",frames)

for i in range(int(frames)):
    ret,frame = videoCapture.read()
    cv2.imwrite("D:\\bishe\\faster-rcnn\\faster-rcnn-tensorflow-python3-master\\video\\pics\\1-1.avi(%d).jpg"%i,frame)