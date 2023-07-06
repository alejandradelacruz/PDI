import cv2
import numpy as np

def umbral(valor):
    img2 = imgRgb.copy()
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
    umbralX = valor/100
    rectangulos = np.where(res >= umbralX)

    for puntos in zip(*rectangulos[::-1]):
        print(puntos)
        cv2.rectangle(img2, puntos, (puntos[0] + w, puntos[1] + h), (0,255,0), 1)
    cv2.imshow('match', img2)

cv2.namedWindow('match', cv2.WINDOW_NORMAL)

imgRgb = cv2.imread('engranaje.jpg')
imgGray = cv2.cvtColor(imgRgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template.jpg', 0)
cv2.imshow('match', imgRgb)

cv2.createTrackbar('Umbral', 'match', 0, 100, umbral)

cv2.waitKey(0)
cv2.destroyAllWindows()

# imgRgb = cv2.imread('engranaje.jpg')

# roi = cv2.selectROI('match', imgRgb, True)
# x = roi[0]
# y = roi[1]
# w = roi[2]
# h = roi[3]

# template = imgRgb[y:y+h, x:x+w]

# imgGray = cv2.cvtColor(imgRgb, cv2.COLOR_BGR2GRAY)
# template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
# cv2.imshow('match', imgRgb)

# cv2.createTrackbar('Umbral', 'match', 0, 100, umbral)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


