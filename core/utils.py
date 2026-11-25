"""
توابع کمکی پروژه Image Lab
خواندن/ذخیره تصویر، تغییر اندازه و نمایش قبل/بعد
"""
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_image(path: str):
    """
    خواندن تصویر از مسیر.
    نکته مهم: cv2.imread اگر مسیر اشتباه باشد ارور نمی‌دهد و فقط None برمی‌گرداند!
    برای همین خودمان بررسی می‌کنیم.
    """
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"تصویر پیدا نشد یا قابل خواندن نیست: {path}")
    return img


def save_image(img, path: str):
    """ذخیره تصویر (اگر پوشه وجود نداشت، ساخته می‌شود)."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    ok = cv2.imwrite(path, img)
    if not ok:
        raise IOError(f"ذخیره تصویر ناموفق بود: {path}")


def resize_image(img, width: int | None = None, height: int | None = None,
                 keep_aspect: bool = True):
    """
    تغییر اندازه تصویر.
    - فقط width بدهی و keep_aspect=True  => height خودکار حساب می‌شود.
    - فقط height بدهی و keep_aspect=True => width خودکار حساب می‌شود.
    - هر دو بدهی => همان اندازه (ممکن است تصویر کش بیاید).

    یادآوری: img.shape = (h, w, c) ولی cv2.resize اندازه را به صورت (w, h) می‌گیرد!
    """
    h, w = img.shape[:2]
    if width is None and height is None:
        return img.copy()

    if keep_aspect:
        if width is not None and height is None:
            height = int(round(h * width / w))
        elif height is not None and width is None:
            width = int(round(w * height / h))
    else:
        width = width or w
        height = height or h

    # برای کوچک کردن INTER_AREA و برای بزرگ کردن INTER_LINEAR کیفیت بهتری دارد
    shrinking = (width * height) < (w * h)
    interp = cv2.INTER_AREA if shrinking else cv2.INTER_LINEAR
    return cv2.resize(img, (int(width), int(height)), interpolation=interp)


def image_info(img) -> dict:
    """اطلاعات پایه تصویر (برای آموزش و نمایش در برنامه)."""
    h, w = img.shape[:2]
    channels = 1 if img.ndim == 2 else img.shape[2]
    return {
        "width": w,
        "height": h,
        "channels": channels,
        "dtype": str(img.dtype),
        "size_kb": round(img.nbytes / 1024, 1),  # حجم در حافظه (بدون فشرده‌سازی)
    }


def show_before_after(img_before, img_after,
                      title_1: str = "Before", title_2: str = "After"):
    """
    نمایش تصویر قبل و بعد کنار هم با matplotlib.
    OpenCV رنگ‌ها را BGR می‌خواند ولی matplotlib به RGB نیاز دارد، پس تبدیل می‌کنیم.
    """
    def to_rgb(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB) if img.ndim == 3 else img

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    for ax, im, title in ((ax1, img_before, title_1), (ax2, img_after, title_2)):
        ax.imshow(to_rgb(im), cmap="gray" if im.ndim == 2 else None)
        ax.set_title(title)
        ax.axis("off")
    plt.tight_layout()
    plt.show()


def create_sample_image(path: str = "images/sample_image.jpg",
                        size: tuple[int, int] = (640, 480)):
    """
    اگر عکس نداری، یک تصویر نمونه می‌سازد تا بتوانی کدها را اجرا کنی.
    (بهتر است بعداً عکس خودت را در پوشه images بگذاری.)
    """
    w, h = size
    img = np.zeros((h, w, 3), dtype=np.uint8)
    for x in range(w):
        img[:, x] = (int(255 * x / w), 120, int(255 * (1 - x / w)))
    cv2.circle(img, (w // 2, h // 2), 100, (0, 220, 255), -1)
    cv2.rectangle(img, (40, 40), (220, 160), (60, 200, 60), -1)
    cv2.putText(img, "Image Lab", (w // 2 - 130, h - 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.6, (255, 255, 255), 3)
    save_image(img, path)
    return path
