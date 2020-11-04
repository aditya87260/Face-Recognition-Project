import cv2
import matplotlib.pyplot as plt
# Read an Image
img = cv2.imread('1.jpg')
newImg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
plt.imshow(newImg)
plt.show()
print(img)