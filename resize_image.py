import cv2

img = cv2.imread('Virtual_Zoom_using_OpenCV\test.jpg')
img = cv2.resize(img, (225, 225))
cv2.imwrite('Virtual_Zoom_using_OpenCV\resized_test.jpg', img)