import numpy as np
from matplotlib import pyplot as plt
import cv2

# Get webcam video feed
cap = cv2.VideoCapture(0)
# Set video type
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# Create an output file
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640, 480))

while(True):
  # Return and frame of capture
  ret, frame = cap.read()
  # cvtColor convert frame to COLOR_BGR2GRAY
  grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  # Write to output file
  out.write(frame)
  
  # Display window called 'frame' 
  cv2.imshow('grayFrame',grayFrame)
  # Display another window with original values
  cv2.imshow('frame',frame)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
    
# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()