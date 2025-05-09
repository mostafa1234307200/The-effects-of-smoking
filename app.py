import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.set_page_config(page_title="مدرسة الأردن الأساسية المختلطة", layout="centered")

# إنشاء صف من عمودين: النص والصورة
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<h1 style='text-align: right;'>مدرسة الأردن الأساسية المختلطة</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: right; color: red;'>كيف ستبدو بعد 30 سنة من التدخين؟</h3>", unsafe_allow_html=True)

with col2:
    st.image("no_smoking.png", caption="لا للتدخين", use_column_width=True)

# رفع الصورة من المستخدم
uploaded_file = st.file_uploader("ارفع صورتك (jpg أو png)", type=["jpg", "jpeg", "png"])

# دالة التأثير
def apply_aging_effect(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    dark = cv2.convertScaleAbs(img, alpha=0.6, beta=-50)
    blurred = cv2.GaussianBlur(dark, (9, 9), 3)
    noise = np.random.normal(0, 15, blurred.shape).astype(np.uint8)
    aged = cv2.addWeighted(blurred, 0.9, noise, 0.1, 0)
    aged = cv2.cvtColor(aged, cv2.COLOR_BGR2RGB)
    return aged

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    img_np = np.array(image)

    st.image(img_np, caption="صورتك الأصلية", use_column_width=True)

    aged_image = apply_aging_effect(img_np)
    st.image(aged_image, caption="بعد 30 سنة من التدخين", use_column_width=True)
