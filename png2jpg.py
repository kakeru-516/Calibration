import cv2
for i in range(144) :
    img = cv2.imread('./img/' + str(i) + '.png')
    cv2.imwrite('./jpg/220_' + str(i) + '.jpg', img)