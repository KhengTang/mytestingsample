import numpy as np
from matplotlib import pyplot as plt
import cv2

# Read watch.jpg in gray scale
img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
# Show image 
cv2.imshow('image',img)

# Wait for any key and destroy window
cv2.waitKey(0)
cv2.destroyAllWindows()