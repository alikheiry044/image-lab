# Image Lab 🖼️

[English](#english) | [فارسی](#فارسی)

---

## English

**Image Lab** is a small image-processing playground built with Python, OpenCV and Streamlit. Upload an image, pick an effect, tweak the parameters with sliders, and instantly compare the **Before** and **After** results.

### Features

- **Blur:** Box, Gaussian, Median, Bilateral
- **Sharpen** using a convolution kernel
- **Flip:** horizontal, vertical, both
- **Rotate** around the center (with an option to enlarge the canvas so nothing gets cropped)
- **Gaussian noise** (safe float + clip implementation)
- **Random filter pipeline**, the basis of data augmentation, with an optional seed for reproducible results
- Download the result as PNG

### Project Structure

```
image-lab/
├── core/
│   ├── filters.py     # all image filters and effects
│   └── utils.py       # helper functions
├── lessons/           # step-by-step OpenCV lessons
├── images/            # sample images
├── app.py             # Streamlit web app
└── requirements.txt
```

### Installation

```bash
git clone https://github.com/alikheiry044/image-lab.git
cd image-lab
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

### Run

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

### Tech Stack

Python 3.10+ · OpenCV · NumPy · Streamlit

> **Note:** this project uses `opencv-python<5`. OpenCV 5 changed parts of the API, so version 4.x is recommended.

### Author

Ali Kheiri

---

## فارسی

**Image Lab** یک آزمایشگاه کوچک پردازش تصویر است که با پایتون، OpenCV و Streamlit ساخته شده. تصویر را آپلود می‌کنید، یک افکت انتخاب می‌کنید، پارامترها را با اسلایدر تنظیم می‌کنید و نتیجه **قبل** و **بعد** را کنار هم می‌بینید.

### امکانات

- **بلور:** Box، Gaussian، Median، Bilateral
- **شارپ** با کرنل کانولوشن
- **قرینه (Flip):** افقی، عمودی، هر دو
- **چرخش** حول مرکز تصویر (با گزینه بزرگ‌تر کردن بوم برای جلوگیری از بریده شدن گوشه‌ها)
- **نویز گاوسی** (پیاده‌سازی ایمن با float و clip)
- **پایپ‌لاین فیلتر تصادفی**، پایه Data Augmentation، با امکان seed برای نتیجه تکرارپذیر
- دانلود نتیجه به‌صورت PNG

### ساختار پروژه

```
image-lab/
├── core/
│   ├── filters.py     # همه فیلترها و افکت‌ها
│   └── utils.py       # توابع کمکی
├── lessons/           # درس‌های گام‌به‌گام OpenCV
├── images/            # تصاویر نمونه
├── app.py             # اپ وب Streamlit
└── requirements.txt
```

### نصب

```bash
git clone https://github.com/alikheiry044/image-lab.git
cd image-lab
python -m venv venv
venv\Scripts\activate        # ویندوز
pip install -r requirements.txt
```

### اجرا

```bash
streamlit run app.py
```

سپس آدرس `http://localhost:8501` را در مرورگر باز کنید.

### تکنولوژی‌ها

Python 3.10+ · OpenCV · NumPy · Streamlit

> **نکته:** این پروژه از `opencv-python<5` استفاده می‌کند، چون OpenCV نسخه ۵ بخشی از API را تغییر داده است. نسخه ۴.x توصیه می‌شود.

### نویسنده

علی خیری
