import cv2
import numpy as np
import streamlit as st

from core.filters import (
    box_blur, gaussian_blur, median_blur, bilateral_blur,
    sharpen, flip, rotate, add_gaussian_noise, apply_random_filter,
)

st.set_page_config(page_title="Image Lab", layout="wide")
st.title("Image Lab")

uploaded = st.sidebar.file_uploader("عکس رو انتخاب کن", type=["jpg", "jpeg", "png", "bmp"])
if uploaded is None:
    st.info("از نوار کناری یه عکس آپلود کن.")
    st.stop()

# بایت -> آرایه OpenCV (BGR)
data = np.frombuffer(uploaded.read(), dtype=np.uint8)
img = cv2.imdecode(data, cv2.IMREAD_COLOR)

effect = st.sidebar.selectbox(
    "افکت",
    ["Box Blur", "Gaussian Blur", "Median Blur", "Bilateral",
     "Sharpen", "Flip", "Rotate", "Noise", "Random Filter"],
)

applied = None

if effect == "Box Blur":
    k = st.sidebar.slider("اندازه کرنل", 1, 51, 5, step=2)
    result = box_blur(img, k)

elif effect == "Gaussian Blur":
    k = st.sidebar.slider("اندازه کرنل", 1, 51, 7, step=2)
    result = gaussian_blur(img, k)

elif effect == "Median Blur":
    k = st.sidebar.slider("اندازه کرنل", 1, 51, 5, step=2)
    result = median_blur(img, k)

elif effect == "Bilateral":
    d = st.sidebar.slider("d", 1, 25, 9)
    sc = st.sidebar.slider("sigma color", 1, 200, 75)
    ss = st.sidebar.slider("sigma space", 1, 200, 75)
    result = bilateral_blur(img, d, sc, ss)

elif effect == "Sharpen":
    result = sharpen(img)

elif effect == "Flip":
    mode = st.sidebar.selectbox("جهت", ["horizontal", "vertical", "both"])
    result = flip(img, mode)

elif effect == "Rotate":
    angle = st.sidebar.slider("زاویه", -180, 180, 45)
    fit = st.sidebar.checkbox("بوم بزرگ‌تر بشه (بریده نشه)", value=True)
    result = rotate(img, angle, fit)

elif effect == "Noise":
    sigma = st.sidebar.slider("sigma", 1, 50, 10)
    result = add_gaussian_noise(img, sigma)

else:  # Random Filter
    seed = st.sidebar.number_input("seed (برای تکرارپذیری)", value=0, step=1)
    use_seed = st.sidebar.checkbox("استفاده از seed", value=False)
    if st.sidebar.button("🎲 فیلتر جدید") or True:
        result, applied = apply_random_filter(img, int(seed) if use_seed else None)

col1, col2 = st.columns(2)
col1.subheader("Before")
col1.image(img, channels="BGR", use_container_width=True)
col2.subheader("After")
col2.image(result, channels="BGR", use_container_width=True)

if applied is not None:
    st.write("افکت‌های اعمال‌شده:", " ← ".join(applied) if applied else "هیچ افکتی اعمال نشد")

ok, buf = cv2.imencode(".png", result)
if ok:
    st.sidebar.download_button("دانلود نتیجه", buf.tobytes(), "result.png", "image/png")
