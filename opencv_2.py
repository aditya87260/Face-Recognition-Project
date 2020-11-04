import cv2
img = cv2.imread('1.jpg')
gray = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Dog Image',img)
cv2.imshow('Gray Dog Image',gray)

cv2.waitKey(0) # Program will stop when any key is pressed
cv2.destroyAllWindows()