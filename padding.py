import numpy as np
import cv2

for i in range(147) :
    img = cv2.imread('./img/' + str(i) + '.png')
    mask = np.zeros(shape=img.shape[:2])
    cv2.circle(mask, (int(1024/2), int(768/2)), 354, 255, thickness=-1)
    img[mask==0] = [0, 0, 0]
    cv2.imwrite('./output/' + str(i) + '.png', img)


