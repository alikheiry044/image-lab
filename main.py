import os
import cv2
from core.filters import box_blur

base_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(base_dir, "images", "sample_image.jpg")

img = cv2.imread(img_path)
if img is None:
    raise FileNotFoundError(f"تصویر پیدا نشد: {img_path}")

result = box_blur(img, ksize=15)

os.makedirs(os.path.join(base_dir, "output"), exist_ok=True)
cv2.imwrite(os.path.join(base_dir, "output", "blur.jpg"), result)

cv2.imshow("Original", img)
cv2.imshow("Blur", result)
cv2.waitKey()
cv2.destroyAllWindows()