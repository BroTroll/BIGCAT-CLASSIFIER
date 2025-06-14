import streamlit as st
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
import joblib
import json
from PIL import Image

svm_model = joblib.load('svm_model.pkl')

with open('class_indices.json', 'r') as f:
    class_indices = json.load(f)

idx_to_class = {v: k for k, v in class_indices.items()}

base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

st.title("🐯 Big Cat Classifier")
st.write("Upload an image of a **leopard**, **lion**, or **tiger** and get the prediction!")
st.markdown("✅ *Use a front-facing image*")
st.markdown("✅ *Face should be clearly visible*")
st.markdown("✅ *Face should cover atleast 40% of the image*")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption='Uploaded Image', use_container_width=True)

    img_resized = img.resize((224, 224))
    img_array = image.img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    features = base_model.predict(img_array)
    features_flat = features.reshape(1, -1)


    prediction = svm_model.predict(features_flat)
    predicted_class = idx_to_class[prediction[0]]

    st.success(f"🎯 Predicted: **{predicted_class.upper()}**")
