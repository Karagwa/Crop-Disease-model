# 🌿 Plant Disease Detection Using CNN + EfficientNet

A deep learning model trained to detect and classify 23 plant diseases (and healthy classes) from leaf images using transfer learning (EfficientNetB0). Built with TensorFlow/Keras and deployed on Kaggle using a T4 GPU.

---

## 🚀 Overview

This project uses a Convolutional Neural Network (CNN) with EfficientNetB0 as a feature extractor to classify plant leaf images into one of 23 classes, including:

- Apple (scab, rot, healthy, etc.)
- Corn (rust, blight, healthy, etc.)
- Tomato (blight, yellow leaf curl virus, mold, etc.)
- Potato, Pepper, and more...

✅ Handles class imbalance  
✅ Achieves **97%+ validation accuracy**  
✅ Includes class-by-class evaluation  
✅ Ready for deployment via Streamlit!

---

## 🧠 Key Features

- **Transfer Learning**: Uses pretrained EfficientNetB0 for fast, accurate results.
- **Class Weighting**: Adjusts for heavy class imbalance (21:1 ratio).
- **Data Augmentation**: Improves generalization on real-world inputs.
- **EarlyStopping + ModelCheckpoint**: Automatically saves the best model and avoids overfitting.
- **Streamlit Demo**: Upload a plant leaf photo and get instant predictions.

---

## 📊 Dataset Summary

- **Total images**: 35,725  
- **Classes**: 23  
- **Imbalance Ratio**: 21.11:1  
- **Source**: https://www.kaggle.com/datasets/karagwaanntreasure/plant-disease-detection/data

---

## 🛠️ Installation

```bash
# Clone the repo (if hosted on GitHub)
git clone https://github.com/karagwa/plant-disease-detector.git
cd plant-disease-detector

# Install dependencies
pip install -r requirements.txt
````

---

## 📁 Project Structure

```
├── plant_disease_model.h5          # Trained model
├── streamlit_app.py                # Streamlit demo app
├── notebook.ipynb                  # Training code on Kaggle
├── README.md                       # You're here!
├── requirements.txt                # Dependencies
└── /Dataset                        # Cleaned dataset
```

---

## 🧪 Training Pipeline

1. **Cleaned** file names for whitespace and formatting issues.
2. **Calculated** class distribution and class weights.
3. **Used EfficientNetB0** with custom dense layers for classification.
4. **Trained** for 20 epochs using:

   * `EarlyStopping` to halt if validation loss plateaus
   * `ModelCheckpoint` to save the best weights based on validation accuracy
5. **Saved model** in `.h5` and `.keras` formats

---

## 📈 Evaluation Results

| Metric          | Value      |
| --------------- | ---------- |
| Accuracy        | **97.09%** |
| F1-Score (avg)  | 96.27%     |
| Macro Precision | 95.95%     |
| Macro Recall    | 96.69%     |

📌 Some minority classes like `Potato___healthy` still showed lower recall, highlighting the impact of imbalance.

---

## 🖼️ Streamlit App Usage

```bash
streamlit run streamlit_app.py
```

**Features:**

* Upload an image of a plant leaf
* Get top 3 predictions with probabilities
* Clean, simple interface

---

## 💾 Model Saving

```python
model.save("plant_disease_model.h5")  # or .keras
```

To download from Kaggle:

* Go to the **"Files" panel** on the right.
* Click the file (or ZIP it).
* Download it manually.

---

## 🔮 Future Work

* Convert model to TFLite for mobile usage.
* Integrate model into a full web dashboard for farmers.
* Add explainability (Grad-CAM, saliency maps).

---

## 📢 Citation

If you use this model or code, kindly cite or link to this repo and the original dataset.

---

## 🧑‍💻 Author

Made with 💚 by \Ann Karagwa
Email: annkaragwa@gmail.com

---

## 📜 License

MIT License – feel free to use and modify.

```

---

