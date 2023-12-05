import cv2

img = cv2.imread("C:\Images\moon.jpg")

cv2.namedWindow("Moon",cv2.WINDOW_NORMAL)

img = cv2.resize(img, (640,480))

cv2.imshow("Moon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

