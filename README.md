# 🐯 Big Cat Classifier

A Streamlit web app that classifies images of big cats — **Leopard**, **Lion**, or **Tiger** — using features extracted from **VGG16** and classified with a trained **SVM** model.(Transfer Learning)

---

## 📌 Features

- Upload `.jpg`, `.jpeg`, or `.png` images
- Front-end built with **Streamlit**
- Feature extraction using **VGG16 (without top layer)**
- Classification using **SVM (trained with extracted features)**
- Predicts one of three classes: `leopard`, `lion`, or `tiger`
  
---

## 🧠 Model Details

- **Feature Extractor**: VGG16 (`include_top=False`)
- **Classifier**: SVM (trained using scikit-learn)
- **Classes**:
  - `leopard`
  - `lion`
  - `tiger`

---

## 📷 Input Recommendations

- Use **front profile** images of the cat
- The cat should cover **~70%** of the image frame for best results

---

## 👤 Author

**Akshit**  
GitHub: [@BroTroll](https://github.com/BroTroll)

---
