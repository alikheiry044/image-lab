"""
درس ۲: بلور، شارپ، فلیپ، چرخش، نویز و پایپ‌لاین تصادفی
اجرا:   python lessons/lesson_02_filters.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.utils import load_image, show_before_after, create_sample_image
from core import filters

PATH = "images/sample_image.jpg"
if not os.path.exists(PATH):
    create_sample_image(PATH)
img = load_image(PATH)

# هر خط را از حالت کامنت دربیاور و جداگانه امتحان کن:
show_before_after(img, filters.gaussian_blur(img, 9), "Original", "Gaussian 9")
# show_before_after(img, filters.median_blur(filters.add_gaussian_noise(img, 25), 5), "Noisy", "Median")
# show_before_after(img, filters.bilateral_blur(img), "Original", "Bilateral")
# show_before_after(img, filters.sharpen(img), "Original", "Sharpen")
# show_before_after(img, filters.flip(img, "horizontal"), "Original", "Flip H")
# show_before_after(img, filters.rotate(img, 45, fit=False), "Original", "Rotate 45 (cropped)")
# show_before_after(img, filters.rotate(img, 45, fit=True), "Original", "Rotate 45 (fit)")

# پایپ‌لاین تصادفی (seed ثابت = نتیجه تکرارپذیر)
result, applied = filters.apply_random_filter(img, seed=None)
for i, name in enumerate(applied, 1):
    print(f"{i}- {name}")
show_before_after(img, result, "Before", "After random pipeline")
