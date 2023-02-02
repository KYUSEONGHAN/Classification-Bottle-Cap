from skimage.measure import compare_ssim
import cv2

image_a = cv2.imread('img1.jpeg')
image_b = cv2.imread('img2.jpeg')
image_c = image_a.copy()

tempDiff = cv2.subtract(image_a, image_b)

grayA = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)

cv2.imshow('grayA', cv2.resize(grayA, (960, 540)))

(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")

print(f'이미지 유사도: {score: .5f}')

assert score, "다른 점 찾을 수 없음"

thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

tempDiff[thresh == 255] = [0, 0, 255]
image_c[thresh == 255] = [0, 0, 255]

# cv2.imwrite("diff", image_c)

cv2.imshow("original", cv2.resize(image_a, (960, 540)))
cv2.imshow("compare", cv2.resize(image_b, (960, 540)))
cv2.imshow("difference", cv2.resize(image_c, (960, 540)))
cv2.imshow("gray", cv2.resize(diff, (960, 540)))
cv2.imshow("gray2", cv2.resize(tempDiff, (960, 540)))


cv2.waitKey(0)