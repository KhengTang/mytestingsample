import numpy as np
from matplotlib import pyplot as plt
import cv2

# Read watch.jpg
img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
# Draw line using opencv
cv2.line(img,(0,0),(150,150),(255,255,255),5)
# Draw rectangle
cv2.rectangle(img,(15,25),(200,150),(0,0,255),5)
# Draw circle
cv2.circle(img,(100,63),55,(0,255,0),1)
# Draw using np array coor
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
cv2.polylines(img,[pts],True,(0,255,255),3)
# Draw text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'My First Text',(0,130),font,1,(200,255,155),2,cv2.LINE_AA)
# Show image 
cv2.imshow('image',img)

# Wait for any key and destroy window
cv2.waitKey(0)
cv2.destroyAllWindows()