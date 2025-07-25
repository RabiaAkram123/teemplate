import cv2
import numpy as np
img=cv2.imread("group.jpg")
resize_img=cv2.resize(img,(800,600))  # Resize the image to 800x600 pixels
gray=cv2.cvtColor(resize_img,cv2.COLOR_BGR2GRAY)
template=cv2.imread("t.jpg",0)
template1=cv2.resize(template,(118,122))  # Resize the template to 100x100 pixels

w,h=template1.shape[::-1]
res=cv2.matchTemplate(gray,template1,cv2.TM_CCOEFF_NORMED)
print(res)
threshold=0.7
loc=np.where(res>=threshold)
print(loc)

for pt in zip(*loc[::-1]):
 cv2.rectangle(resize_img,pt,(pt[0]+w,pt[1]+h),(0,0,255),1)
    

cv2.imshow("image",resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows