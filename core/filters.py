"""
فیلترها و افکت‌های Image Lab
هر تابع: تصویر ورودی را می‌گیرد و تصویر جدید برمی‌گرداند (ورودی را تغییر نمی‌دهد).
"""
import random
import cv2
import numpy as np


def _odd(k: int) -> int:
    """اندازه کرنل در بلور باید فرد و حداقل ۱ باشد."""
    k = max(1, int(k))
    return k if k % 2 == 1 else k + 1


# ---------- Blur ----------
def box_blur(img, ksize: int = 5):
    """Mean/Box Blur: میانگین ساده همسایه‌ها."""
    k = _odd(ksize)
    return cv2.blur(img, (k, k))


def gaussian_blur(img, ksize: int = 7):
    """Gaussian Blur: میانگین وزن‌دار؛ پیکسل‌های نزدیک‌تر وزن بیشتری دارند (طبیعی‌تر)."""
    k = _odd(ksize)
    return cv2.GaussianBlur(img, (k, k), 0)


def median_blur(img, ksize: int = 5):
    """Median Blur: مقدار میانه همسایه‌ها؛ بهترین گزینه برای نویز نمک‌فلفلی."""
    k = _odd(ksize)
    return cv2.medianBlur(img, k)  # فقط دو آرگومان!


def bilateral_blur(img, d: int = 9, sigma_color: int = 75, sigma_space: int = 75):
    """Bilateral: نویز را کم می‌کند ولی لبه‌ها را حفظ می‌کند."""
    return cv2.bilateralFilter(img, d, sigma_color, sigma_space)


# ---------- Sharpen ----------
def sharpen(img):
    """شارپ با کرنل کانولوشن (Convolutional Kernel)."""
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]], dtype=np.float32)
    return cv2.filter2D(img, -1, kernel)


# ---------- Flip ----------
FLIP_CODES = {"horizontal": 1, "vertical": 0, "both": -1}


def flip(img, mode: str = "horizontal"):
    """
    horizontal: حول محور Y (کد 1)
    vertical:   حول محور X (کد 0)
    both:       هر دو (کد -1)
    """
    return cv2.flip(img, FLIP_CODES[mode])


# ---------- Rotate ----------
def rotate(img, angle: float, fit: bool = True):
    """
    چرخش حول مرکز تصویر (زاویه مثبت = خلاف جهت عقربه‌های ساعت).
    fit=False: اندازه ثابت، گوشه‌ها بریده می‌شوند.
    fit=True:  بوم بزرگ‌تر می‌شود تا هیچ بخشی بریده نشود.
    """
    h, w = img.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    if not fit:
        return cv2.warpAffine(img, M, (w, h))

    cos, sin = abs(M[0, 0]), abs(M[0, 1])
    new_w = int(h * sin + w * cos)
    new_h = int(h * cos + w * sin)
    # انتقال تا مرکز تصویر در مرکز بوم جدید قرار بگیرد
    M[0, 2] += new_w / 2 - center[0]
    M[1, 2] += new_h / 2 - center[1]
    return cv2.warpAffine(img, M, (new_w, new_h))


# ---------- Noise ----------
def add_gaussian_noise(img, sigma: float = 10):
    """
    نویز گاوسی.
    نکته: نویز را float می‌سازیم، جمع می‌کنیم و clip می‌کنیم.
    (astype(uint8) روی مقدار منفی باعث می‌شود 253 بشود و نویز اشتباه بسازد!)
    """
    noise = np.random.normal(0, sigma, img.shape)
    noisy = img.astype(np.float32) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)


# ---------- Pipeline تصادفی ----------
def apply_random_filter(img, seed: int | None = None):
    """
    پایپ‌لاین افکت تصادفی (پایه Data Augmentation).
    خروجی: (تصویر نهایی, لیست افکت‌های اعمال‌شده)
    """
    rng = random.Random(seed)
    result = img.copy()
    applied = []

    if rng.random() > 0.5:
        k = rng.choice([3, 5, 7, 9])
        result = box_blur(result, k)
        applied.append(f"Blur {k}x{k}")

    if rng.random() > 0.5:
        k = rng.choice([3, 5, 7])
        result = gaussian_blur(result, k)
        applied.append(f"Gaussian Blur {k}x{k}")

    if rng.random() > 0.7:
        result = sharpen(result)
        applied.append("Sharpen")

    if rng.random() > 0.5:
        k = rng.choice([3, 5])
        result = median_blur(result, k)
        applied.append(f"Median Blur {k}x{k}")

    if rng.random() > 0.5:
        mode = rng.choice(list(FLIP_CODES))
        result = flip(result, mode)
        applied.append(f"Flip {mode}")

    if rng.random() > 0.3:
        angle = rng.choice([45, 90, 180, 270])
        result = rotate(result, angle, fit=True)
        applied.append(f"Rotation {angle}°")

    if rng.random() > 0.8:
        sigma = rng.choice([5, 10, 15])
        result = add_gaussian_noise(result, sigma)
        applied.append(f"Noise {sigma}")

    return result, applied
