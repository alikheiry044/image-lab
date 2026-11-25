"""
درس ۱: خواندن تصویر، shape، resize و ذخیره
اجرا از ریشه پروژه:   python lessons/lesson_01_basics.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import cv2
from core.utils import (load_image, save_image, resize_image, image_info,
                        show_before_after, create_sample_image)

PATH = "images/sample_image.jpg"
if not os.path.exists(PATH):
    create_sample_image(PATH)          # اگر عکس نداشتی، نمونه می‌سازد

# ---- ۱) خواندن تصویر ----
img = load_image(PATH)
print("اطلاعات تصویر:", image_info(img))

# ---- ۲) shape یعنی (ارتفاع، عرض، کانال) ----
h, w, c = img.shape
print(f"h={h}, w={w}, c={c}")
print("img.size =", img.size, "→ همان h*w*c =", h * w * c)

# ---- ۳) resize: توجه کن اندازه به صورت (عرض، ارتفاع) داده می‌شود ----
img_fixed = cv2.resize(img, (300, 300))             # کش می‌آید
img_keep = resize_image(img, width=300)             # نسبت حفظ می‌شود
print("بعد از resize ثابت :", img_fixed.shape)
print("بعد از resize نسبتی:", img_keep.shape)

# ---- ۴) ذخیره و نمایش ----
save_image(img_keep, "output/resized.png")
show_before_after(img, img_keep, "Original", "Resized (aspect kept)")

# ---- تمرین ----
# ۱. width=500 بده و ببین height چند می‌شود.
# ۲. هر دو مقدار width و height را بده و keep_aspect=False بگذار؛ چه اتفاقی می‌افتد؟
# ۳. عکس خودت را در images بگذار و مسیر PATH را عوض کن.
